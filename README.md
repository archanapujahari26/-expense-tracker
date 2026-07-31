# Smart Expense Tracker API

A RESTful API built with **FastAPI** for managing personal expenses. The application allows users to add, retrieve, filter, summarize, and delete expenses. Data is stored locally in a JSON file, making the project lightweight and easy to run without requiring a database.

---

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- View monthly expense summary (Bonus Feature)
- Input validation using Pydantic
- Interactive Swagger/OpenAPI documentation
- Automated API testing with Pytest

---

## Tech Stack

- Python 3
- FastAPI
- Pydantic
- Uvicorn
- Pytest

---

## Project Structure

```text
expense-tracker/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── pytest.ini
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── storage.py
│   └── expenses.json
│
├── tests/
│   └── test_api.py
│
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd expense-tracker
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI development server:

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```
http://127.0.0.1:8000/docs
```

Alternative OpenAPI documentation:

```
http://127.0.0.1:8000/redoc
```

---

## Running the Tests

Run the automated test suite:

```bash
python -m pytest
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome endpoint |
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | Retrieve all expenses |
| GET | `/expenses/category/{category}` | Retrieve expenses by category |
| GET | `/expenses/total` | Calculate total expenses |
| GET | `/expenses/total/{category}` | Calculate total expenses for a category |
| DELETE | `/expenses/{expense_id}` | Delete an expense |
| GET | `/expenses/monthly/{month}` | Monthly expense summary (Bonus Feature) |

---

## Example Request

### Add an Expense

**POST** `/expenses`

```json
{
  "id": 1,
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "date": "2026-07-31"
}
```

### Example Response

```json
{
  "message": "Expense added successfully",
  "expense": {
    "id": 1,
    "title": "Lunch",
    "amount": 250,
    "category": "Food",
    "date": "2026-07-31"
  }
}
```

---

## Testing

The project includes automated tests covering:

- Expense creation
- Retrieve all expenses
- Filter expenses by category
- Calculate total expenses
- Delete an expense
- Monthly expense summary

---

## API Documentation

FastAPI automatically generates interactive API documentation.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## Author

**Archana Pujahari**

B.Tech Computer Science & Engineering