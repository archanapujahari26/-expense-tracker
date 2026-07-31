# 💰 Smart Expense Tracker API

A modern **RESTful Expense Tracker API** built with **FastAPI** that helps users manage personal expenses efficiently. The application supports creating, viewing, filtering, summarizing, and deleting expenses while storing data locally in a JSON file.

---

## ✨ Features

- ✅ Add a new expense
- ✅ View all expenses
- ✅ Filter expenses by category
- ✅ Calculate total expenses
- ✅ Calculate total expenses by category
- ✅ Monthly expense summary
- ✅ Delete an expense
- ✅ Input validation using Pydantic
- ✅ Interactive Swagger/OpenAPI documentation
- ✅ Automated API testing with Pytest

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| FastAPI | REST API Framework |
| Uvicorn | ASGI Server |
| Pydantic | Data Validation |
| Pytest | API Testing |

---

## 📂 Project Structure

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
└── tests/
    └── test_api.py
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/archanapujahari26/expense-tracker.git
cd expense-tracker
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn src.main:app --reload
```

Open the API documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## 🧪 Run Tests

Execute all automated tests:

```bash
python -m pytest
```

Expected Output:

```text
==================== 6 passed ====================
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Home |
| POST | `/expenses` | Add Expense |
| GET | `/expenses` | View All Expenses |
| GET | `/expenses/category/{category}` | Filter by Category |
| GET | `/expenses/total` | Total Expenses |
| GET | `/expenses/total/{category}` | Total by Category |
| GET | `/expenses/monthly/{month}` | Monthly Expense Summary |
| DELETE | `/expenses/{expense_id}` | Delete Expense |

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

- Swagger UI → `/docs`
- ReDoc → `/redoc`

---

## ✅ Testing

The project includes automated API tests using **Pytest** to verify:

- Expense creation
- Fetching all expenses
- Category filtering
- Total expense calculation
- Monthly summary
- Expense deletion

---

## 👩‍💻 Author

**Archana Pujahari**

B.Tech – Computer Science & Engineering

---

## 📄 License

This project was developed as part of a software engineering assessment and is intended for educational and evaluation purposes.