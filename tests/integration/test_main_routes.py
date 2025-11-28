import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """Test the root HTML endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_health_check():
    """Test the health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_login_page_render():
    """Test GET /login renders HTML."""
    response = client.get("/login")
    assert response.status_code == 200
    assert "Login" in response.text

def test_register_page_render():
    """Test GET /register renders HTML."""
    response = client.get("/register")
    assert response.status_code == 200
    assert "Register" in response.text

def test_dashboard_page_render():
    """Test GET /dashboard renders HTML."""
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert "Dashboard" in response.text

def test_swagger_ui_login_flow(db_session, fake_user_data):
    """
    Test the form-data login endpoint used by Swagger UI.
    This covers the `login_form` function in main.py.
    """
    from app.models.user import User
    
    # Create user
    fake_user_data["password"] = "SecurePass123!"
    User.register(db_session, fake_user_data)
    db_session.commit()

    # Attempt login with form data
    response = client.post(
        "/auth/token",
        data={
            "username": fake_user_data["username"],
            "password": "SecurePass123!"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_swagger_ui_login_fail(db_session):
    """Test login failure for Swagger UI flow."""
    response = client.post(
        "/auth/token",
        data={
            "username": "nonexistent",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 401