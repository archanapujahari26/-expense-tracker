<div align="center">

# 💰 Smart Expense Tracker API

*A FastAPI-based REST API for managing personal expenses with validation, reporting, and interactive API documentation.*

![Python](https://img.shields.io/badge/Python-3.13+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![Pytest](https://img.shields.io/badge/Tests-6_Passing-success)
![License](https://img.shields.io/badge/Status-Assessment_Project-orange)

</div>

---

## 📌 Overview

Smart Expense Tracker API is a RESTful backend application built with **FastAPI**. It enables users to manage expenses through a clean and well-documented API while storing data in a lightweight JSON file.

---

## 🚀 Features

- ➕ Add a new expense
- 📋 View all expenses
- 🔍 Filter expenses by category
- 💰 Calculate total expenses
- 📊 Calculate total by category
- 📅 Monthly expense summary
- ❌ Delete an expense
- ✔️ Input validation using Pydantic
- 📖 Interactive Swagger Documentation
- 🧪 Automated API testing

---

## 🛠 Tech Stack

| Technology | Used For |
|------------|----------|
| Python | Programming Language |
| FastAPI | REST API Framework |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |
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

## ⚙️ Installation

```bash
git clone <repository-url>
cd expense-tracker

python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn src.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Run Tests

```bash
python -m pytest
```

Expected Result

```
================== 6 passed ==================
```

---

## 📡 API Endpoints

| Method | Endpoint |
|---------|----------|
| GET | / |
| POST | /expenses |
| GET | /expenses |
| GET | /expenses/category/{category} |
| GET | /expenses/total |
| GET | /expenses/total/{category} |
| GET | /expenses/monthly/{month} |
| DELETE | /expenses/{expense_id} |

---

## 📷 API Preview

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## ✨ Highlights

- Modular project structure
- RESTful API design
- Interactive Swagger documentation
- Pydantic validation
- Proper HTTP status codes
- Error handling
- Automated testing
- Clean, readable code

---

## 👩‍💻 Author

**Archana Pujahari**

B.Tech – Computer Science & Engineering