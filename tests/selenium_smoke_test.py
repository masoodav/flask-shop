import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture(scope="module")
def driver():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless browser (optional)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set path to ChromeDriver
    service = Service('/path/to/chromedriver')  # Update with your path to chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver

    driver.quit()

def test_homepage_loads(driver):
    driver.get('http://localhost:5000')
    assert 'FlaskShop' in driver.title

def test_navigation(driver):
    driver.get('http://localhost:5000')
    nav_links = driver.find_elements(By.CSS_SELECTOR, 'nav a')
    assert len(nav_links) > 0, "No navigation links found"
    for link in nav_links:
        link.click()
        time.sleep(1)
        assert driver.current_url.startswith('http://localhost:5000'), f"Navigation failed to {link.text}"
