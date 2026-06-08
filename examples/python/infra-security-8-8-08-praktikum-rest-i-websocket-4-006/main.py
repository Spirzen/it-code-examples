from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime, timezone

import uuid

Base = declarative_base()

class ProductRow(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, default=lambda: f"prod_{uuid.uuid4().hex[:8]}")
    sku = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    price_cents = Column(Integer, nullable=False)
    stock_available = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class ReservationRow(Base):
    __tablename__ = "reservations"
    id = Column(String, primary_key=True, default=lambda: f"res_{uuid.uuid4().hex[:8]}")
    product_id = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    order_ref = Column(String, nullable=False)
    idempotency_key = Column(String, unique=True, nullable=True)
    expires_at = Column(DateTime, nullable=False)

engine = create_engine("sqlite:///./catalog.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
