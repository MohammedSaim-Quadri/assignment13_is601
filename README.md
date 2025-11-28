# IS601 Module 13: JWT Authentication & E2E Testing

This project implements a FastAPI-based calculation application with **JWT (JSON Web Token) authentication**. It includes a full front-end interface for user registration and login, along with automated End-to-End (E2E) testing using **Playwright**.

---

## Docker Hub Repository

**[Link to Docker Hub Repository](https://hub.docker.com/r/saimquadri/601_module13)**

---

## Features Implemented

### 1. JWT Authentication (Back-End)
- [cite_start]**`/register` Endpoint:** Hashes passwords using bcrypt, validates user data with Pydantic, checks for duplicates, and stores users in PostgreSQL[cite: 57, 122].
- [cite_start]**`/login` Endpoint:** Validates credentials and returns a JWT access token upon success[cite: 58, 126].
- **Security:** Protected routes require a valid Bearer token in the header.

### 2. Front-End Interface
- [cite_start]**Register Page (`register.html`):** Client-side validation for email format and password complexity (min length, special chars)[cite: 278, 290].
- [cite_start]**Login Page (`login.html`):** secure login form that stores the JWT in `localStorage` upon success[cite: 254, 265].
- [cite_start]**Dashboard:** A protected area that requires authentication to view[cite: 200].

### 3. Automated Testing & CI/CD
- [cite_start]**Playwright E2E Tests:** Automated browser testing for positive (successful login/register) and negative (invalid input) scenarios[cite: 322, 327].
- [cite_start]**CI/CD Pipeline:** GitHub Actions workflow that spins up a database, runs tests, and pushes the image to Docker Hub on success[cite: 464, 471].

---

## Project Setup

### 1. Clone and Configure
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Environment Setup (Python)
Ensure you have Python 3.10+ installed.

```bash

# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Install Playwright Browsers
Required for running E2E tests.

```bash
playwright install
```

### 4. Database Setup
Ensure you have a PostgreSQL database running. You can use Docker Compose:

```bash
docker-compose up -d
```
Update your .env file or environment variables to match your DB credentials.

## Running the Application
To run the application locally with the front-end:

Start the Server:

```bash
uvicorn app.main:app --reload
Access the Front-End: Open your browser and navigate to:

Home: http://127.0.0.1:8000/

Login: http://127.0.0.1:8000/login

Register: http://127.0.0.1:8000/register

Dashboard: http://127.0.0.1:8000/dashboard
```
## Running Tests
### 1. Run All Tests (Unit + Integration + E2E)
```bash
pytest
```
### 2. Run Only E2E (Playwright) Tests
To specifically test the UI flows (Login/Register validation):

```bash

pytest tests/e2e
```
Note: Ensure the server is running or the test fixture is configured to spin up the TestClient correctly.

### 3. Run Only Unit/Integration Tests
```bash

pytest tests/unit tests/integration
```

## CI/CD Pipeline
This repository uses GitHub Actions for Continuous Integration and Deployment.

- Trigger: Pushes to the main branch.

- Test: Sets up Python, installs dependencies (including Playwright), runs all tests against a service container database.

- Deploy: If tests pass, builds the Docker image and pushes it to Docker Hub