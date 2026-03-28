from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utils.config import settings


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.explicit_wait)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def click(self, by: By, value: str) -> None:
        self.wait.until(EC.element_to_be_clickable((by, value))).click()

    def type(self, by: By, value: str, text: str, clear_first: bool = True) -> None:
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        if clear_first:
            element.clear()
        element.send_keys(text)

    def text_of(self, by: By, value: str) -> str:
        return self.wait.until(EC.visibility_of_element_located((by, value))).text

    def is_visible(self, by: By, value: str) -> bool:
        try:
            return self.wait.until(EC.visibility_of_element_located((by, value))).is_displayed()
        except Exception:
            return False
