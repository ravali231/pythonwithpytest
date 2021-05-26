import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver= None
@pytest.fixture()
def setup():
    global driver
    print("Start Browser")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()
    print("Close the Browser")

def test_1(setup):
    driver.get("http://www.google.com")
    print("Test 1 Executed")

def test_2(setup):
    driver.get("http://www.facebook.com")
    print("Test 2 Executed")

def test_3(setup):
    driver.get("http://www.gmail.com")
    print("Test 3 Executed")
