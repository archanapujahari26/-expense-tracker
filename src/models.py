from pydantic import BaseModel, Field
from datetime import date


class Expense(BaseModel):
    id: int
    title: str
    amount: float = Field(gt=0)
    category: str
    date: date

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "Lunch",
                "amount": 250,
                "category": "Food",
                "date": "2026-07-31",
            }
        }
    }
