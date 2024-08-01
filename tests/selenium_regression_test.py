import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless")
    service = Service('/path/to/chromedriver')  # Adjust the path to the chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_homepage_loads(driver):
    driver.get('http://localhost:5000')
    assert 'FlaskShop' in driver.title
    assert driver.find_element(By.TAG_NAME, 'h1').is_displayed()

def test_navigation_links(driver):
    driver.get('http://localhost:5000')
    nav_links = driver.find_elements(By.CSS_SELECTOR, 'nav a')
    assert len(nav_links) > 0, "No navigation links found"
    for link in nav_links:
        link.click()
        assert driver.current_url.startswith('http://localhost:5000')
        driver.back()

def test_login_page(driver):
    driver.get('http://localhost:5000/login')
    assert 'Login' in driver.title
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    assert username_field.is_displayed()
    assert password_field.is_displayed()
    assert login_button.is_displayed()

def test_registration_page(driver):
    driver.get('http://localhost:5000/register')
    assert 'Register' in driver.title
    email_field = driver.find_element(By.NAME, 'email')
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')
    register_button = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    assert email_field.is_displayed()
    assert username_field.is_displayed()
    assert password_field.is_displayed()
    assert register_button.is_displayed()

def test_product_page(driver):
    driver.get('http://localhost:5000/products')
    assert 'Products' in driver.title
    products = driver.find_elements(By.CSS_SELECTOR, '.product-item')
    assert len(products) > 0, "No products found"
