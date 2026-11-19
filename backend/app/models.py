from datetime import date, datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, Field

Category = Literal[
    "Food & Drink", "Groceries" , "Transport", "Housing", 
    "Utilities", "Travel", "Entertainment", "Shopping", "Health", 
    "Other",
]

class ExpenseCreate(BaseModel):
    amount: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    currency: str = Field(default="USD", min_length=3, max_length=3)
    merchant: str = Field(min_length=1, max_length=100)
    category: Category | None = None
    date: date
    note: str | None = Field(default=None, max_length=500)
    
class ExpenseUpdate(BaseModel):
    amount: Decimal | None = Field(default=None, gt=0, max_digits=10, decimal_places=2)
    currency: str | None = Field(default=None, min_length=3, max_length=3)
    merchant: str | None = Field(default=None, min_length=1, max_length=100)
    category: Category | None = None
    date: datetime.date | None = None
    note: str | None = Field(default=None, max_length=500)