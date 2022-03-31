import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setUp():
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    print("Test case Started")
    driver.maximize_window()
    yield
    time.sleep(3)
    driver.close()

def test_Login(setUp):
    driver.get("https://www.facebook.com/")
    time.sleep(5)
    driver.find_element_by_name("email").send_keys("")
    time.sleep(5)
    driver.find_element_by_name("pass").send_keys("")
    time.sleep(10)
    driver.find_element_by_name("login").click()

    print("Test case has successfully completed")
