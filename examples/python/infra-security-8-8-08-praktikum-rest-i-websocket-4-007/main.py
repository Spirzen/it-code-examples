from fastapi import FastAPI, Depends, HTTPException, Header, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from .db import SessionLocal, init_db, ProductRow, ReservationRow
from .schemas import ProductCreate, ProductResponse, ReservationCreate, ReservationResponse
from .mapping import to_product_response

API_KEY = "dev-catalog-key-change-me"  # в проде — из переменной окружения

app = FastAPI(title="OrderDesk Catalog", version="1.0.0")

@app.on_event("startup")
def startup():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def require_api_key(x_api_key: str | None = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

@app.get("/api/v1/products")
def list_products(page: int = 1, page_size: int = 20, db: Session = Depends(get_db)):
    rows = db.query(ProductRow).offset((page - 1) * page_size).limit(page_size).all()
    return [to_product_response(r) for r in rows]

@app.post("/api/v1/products", status_code=201)
def create_product(body: ProductCreate, db: Session = Depends(get_db)):
    row = ProductRow(
        sku=body.sku,
        name=body.name,
        price_cents=int(body.price * 100),
        stock_available=body.stock_available,
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return to_product_response(row)

@app.post("/api/v1/reservations", status_code=201, dependencies=[Depends(require_api_key)])
def create_reservation(
    body: ReservationCreate,
    db: Session = Depends(get_db),
    idempotency_key: str = Header(alias="Idempotency-Key"),
):
    existing = db.query(ReservationRow).filter_by(idempotency_key=idempotency_key).first()
    if existing:
        return _reservation_to_dto(existing)

    product = db.query(ProductRow).filter_by(id=body.product_id).first()
    if not product or product.stock_available < body.quantity:
        raise HTTPException(
            status_code=409,
            detail=f"Insufficient stock for {body.product_id}",
        )

    product.stock_available -= body.quantity
    res = ReservationRow(
        product_id=body.product_id,
        quantity=body.quantity,
        order_ref=body.order_ref,
        idempotency_key=idempotency_key,
        expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
    )
    db.add(res)
    db.commit()
    db.refresh(res)
    return _reservation_to_dto(res)

def _reservation_to_dto(row: ReservationRow) -> ReservationResponse:
    return ReservationResponse(
        reservationId=row.id,
        productId=row.product_id,
        quantity=row.quantity,
        expiresAt=row.expires_at,
    )
