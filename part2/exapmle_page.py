import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ExamplePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.connect_to_page()

    def connect_to_page(self):
        try:
            self.driver.get("https://example.com")
        except:
            raise Exception("Connection error")

    def is_title_equals(self, title):
        return self.driver.title == title

    def is_more_info_text_in_css(self, text):
        return self.driver.find_element(By.XPATH,"//*[contains(text(), '%s')]" % text)

    def click_more_info_link(self,link:WebElement):
        link.click()
        time.sleep(1)
        return self.get_current_url()

    def get_current_url(self):
        return self.driver.current_url
