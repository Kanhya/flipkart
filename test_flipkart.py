import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture
def setUp():
    global product,driver
    product = input("enter the product to be searched")
    driver = webdriver.chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

    def test_searchProducts(setup):
        driver.get("http://www.flipkart.com/")
        time.sleep(1)
        driver.find_element_by_xpath("\\html/body/div/[2]/div/div/button").click()
        time.sleep(1)
        driver.find.element_by_name("q").send_keys(product)
        time.sleep(1)
        driver.find_element_by_class_name("L0Z3Pu").click()


