# AI Usage Notes

## AI Tools Used

- ChatGPT

---

## 1. AI-Generated vs. Self-Written Code

ChatGPT was used as a development assistant throughout the implementation of this project. Specifically, it helped with:

- Generating the initial FastAPI project structure.
- Providing example implementations for API endpoints.
- Suggesting request validation using Pydantic.
- Assisting with the initial Pytest test cases.
- Helping draft the README documentation.
- Recommending improvements to project organization, API documentation, and code quality.

I reviewed, integrated, modified, and tested all generated code before including it in the final project. The final implementation, project structure, and engineering decisions reflect my own understanding and verification of the code.

---

## 2. Validation, Testing, and Changes

I validated and improved the AI-generated suggestions by:

- Running the application locally using Uvicorn.
- Testing every API endpoint through the FastAPI Swagger UI.
- Executing automated tests using Pytest throughout development.
- Fixing import and module resolution issues.
- Correcting JSON serialization and data handling issues.
- Refactoring the project by separating the application into modular files (`main.py`, `routes.py`, `models.py`, and `storage.py`).
- Adding proper HTTP status codes, request validation, and error handling.
- Improving the OpenAPI/Swagger documentation with titles, summaries, descriptions, and endpoint tags.
- Adding Python type hints and function docstrings to improve readability and maintainability.
- Formatting the code using Black to maintain a consistent coding style.
- Implementing the optional Monthly Summary endpoint after validating its functionality.

The completed application was verified through manual endpoint testing and automated tests before final submission.

---

## 3. AI Suggestions Not Used

Not every AI suggestion was accepted without modification. After reviewing the generated code, I chose to:

- Keep response messages directly within the route handlers instead of moving them into a separate constants file because it kept the implementation simpler and more appropriate for the size of the project.
- Simplify some suggested refactoring ideas to maintain readability while preserving clean project organization.
- Validate every proposed change before incorporating it into the final implementation.

AI served as a development assistant for brainstorming, debugging, and code review. All code included in the final submission was reviewed, tested, and refined before being accepted.