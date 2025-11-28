import pytest
from playwright.sync_api import Page, expect

def test_register_account_ui(page: Page, fastapi_server):
    # 1. Go to register page
    page.goto("http://127.0.0.1:8000/register")
    
    # 2. Fill valid data
    page.fill("#username", "testuiuser")
    page.fill("#email", "testui@example.com")
    page.fill("#first_name", "Test")
    page.fill("#last_name", "UI")
    page.fill("#password", "SecurePass123!")
    page.fill("#confirm_password", "SecurePass123!")
    
    # 3. Click register
    page.click('button[type="submit"]')
    
    # 4. Verify success message (client-side check) or redirect
    # The provided JS redirects to /login on success
    expect(page).to_have_url("http://127.0.0.1:8000/login", timeout=5000)

def test_login_ui_success(page: Page, fastapi_server):
    # (Prerequisite: Ensure user exists or register them first in this test)
    # For simplicity, let's use the UI to register first (or seed DB)
    page.goto("http://127.0.0.1:8000/register")
    page.fill("#username", "loginuser")
    page.fill("#email", "login@example.com")
    page.fill("#first_name", "Login")
    page.fill("#last_name", "User")
    page.fill("#password", "Pass1234!")
    page.fill("#confirm_password", "Pass1234!")
    page.click('button[type="submit"]')
    page.wait_for_url("**/login")

    # 1. Fill login form
    page.fill("#username", "loginuser")
    page.fill("#password", "Pass1234!")
    
    # 2. Submit
    page.click('button[type="submit"]')
    
    # 3. Check redirect to dashboard
    expect(page).to_have_url("http://127.0.0.1:8000/dashboard", timeout=5000)
    
    # 4. Check if welcome message is displayed
    expect(page.locator("#userWelcome")).to_contain_text("Welcome, loginuser!")

def test_login_invalid_credentials(page: Page, fastapi_server):
    page.goto("http://127.0.0.1:8000/login")
    
    page.fill("#username", "nonexistent")
    page.fill("#password", "WrongPass123!")
    page.click('button[type="submit"]')
    
    error_msg = page.locator("#errorMessage")
    expect(error_msg).to_be_visible()
    expect(error_msg).to_contain_text("Invalid username or password")