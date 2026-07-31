from datetime import datetime

from fastapi import APIRouter, HTTPException, status

from .models import Expense
from .storage import load_expenses, save_expenses

router = APIRouter()


@router.get(
    "/",
    tags=["Home"],
    summary="Home",
    description="Returns the welcome message of the Smart Expense Tracker API.",
)
def home() -> dict:
    """
    Return the welcome message of the Smart Expense Tracker API.
    """
    return {"message": "Welcome to Smart Expense Tracker API"}


@router.post(
    "/expenses",
    tags=["Expenses"],
    summary="Add a new expense",
    description="Creates a new expense and stores it in the local JSON file.",
    status_code=status.HTTP_201_CREATED,
)
def add_expense(expense: Expense) -> dict:
    """
    Add a new expense and save it to the local JSON file.
    """
    expenses = load_expenses()

    expenses.append(expense.model_dump(mode="json"))

    save_expenses(expenses)

    return {"message": "Expense added successfully", "expense": expense}


@router.get(
    "/expenses",
    tags=["Expenses"],
    summary="View all expenses",
    description="Returns all stored expenses.",
)
def get_expenses() -> list:
    """
    Retrieve all stored expenses.
    """
    return load_expenses()


@router.get(
    "/expenses/category/{category}",
    tags=["Expenses"],
    summary="Filter expenses by category",
    description="Returns all expenses that belong to the specified category.",
)
def get_expenses_by_category(category: str) -> list:
    """
    Retrieve all expenses that belong to the specified category.
    """
    expenses = load_expenses()

    filtered = [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()
    ]

    return filtered


@router.get(
    "/expenses/total",
    tags=["Reports"],
    summary="Calculate total expenses",
    description="Returns the total amount of all recorded expenses.",
)
def get_total_expenses() -> dict:
    """
    Calculate the total amount of all recorded expenses.
    """
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    return {"total": total}


@router.get(
    "/expenses/total/{category}",
    tags=["Reports"],
    summary="Calculate total expenses by category",
    description="Returns the total amount spent for a specific category.",
)
def get_total_by_category(category: str) -> dict:
    """
    Calculate the total amount spent for a specific expense category.
    """
    expenses = load_expenses()

    total = sum(
        expense["amount"]
        for expense in expenses
        if expense["category"].lower() == category.lower()
    )

    return {"category": category, "total": total}


@router.delete(
    "/expenses/{expense_id}",
    tags=["Expenses"],
    summary="Delete an expense",
    description="Deletes an expense using its unique ID.",
    status_code=status.HTTP_200_OK,
)
def delete_expense(expense_id: int) -> dict:
    """
    Delete an expense using its unique ID.
    """
    expenses = load_expenses()

    updated_expenses = [
        expense
        for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )

    save_expenses(updated_expenses)

    return {"message": "Expense deleted successfully"}


@router.get(
    "/expenses/monthly/{month}",
    tags=["Reports"],
    summary="Get monthly expense summary",
    description="Returns the total expenses for a given month.",
)
def get_monthly_summary(month: str) -> dict:
    """
    Calculate the total expenses for the specified month (YYYY-MM).
    """
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Month must be in YYYY-MM format",
        )

    expenses = load_expenses()

    total = sum(
        expense["amount"]
        for expense in expenses
        if expense["date"].startswith(month)
    )

    return {"month": month, "total": total}