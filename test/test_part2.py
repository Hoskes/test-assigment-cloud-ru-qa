import time

import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

from part2.exapmle_page import ExamplePage


@pytest.fixture
def create_page():
    # webdriver.ChromeService(executable_path='static/chromedriver.exe')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    page = ExamplePage(driver)
    page.is_more_info_text_in_css("More information")
    yield page
    driver.quit()

    return {"page":page}

def test_is_title_equals(create_page):
    page = create_page
    time.sleep(1)
    page.is_title_equals("Example")
def test_is_css_more_information(create_page):
    page = create_page
    result_elem :WebElement = page.is_more_info_text_in_css("More information")
    print(result_elem)
    assert result_elem is not None
    assert page.click_more_info_link(result_elem) == "https://www.iana.org/help/example-domains"

