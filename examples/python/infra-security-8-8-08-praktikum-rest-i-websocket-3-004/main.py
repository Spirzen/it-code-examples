from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class ProductCreate(BaseModel):
    sku: str = Field(min_length=1, max_length=64)
    name: str = Field(min_length=1, max_length=200)
    price: Decimal = Field(gt=0)
    stock_available: int = Field(ge=0, alias="stockAvailable")

    model_config = ConfigDict(populate_by_name=True)

class ProductResponse(BaseModel):
    id: str
    sku: str
    name: str
    price: Decimal
    stock_available: int = Field(alias="stockAvailable")
    created_at: datetime = Field(alias="createdAt")

    model_config = ConfigDict(populate_by_name=True, by_alias=True)
