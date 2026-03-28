from __future__ import annotations

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from clients.betting_api import BettingApiClient
from utils.config import settings


@pytest.fixture(scope="session")
def api_client() -> BettingApiClient:
    return BettingApiClient()


@pytest.fixture(scope="function", autouse=True)
def reset_balance(api_client: BettingApiClient):
    """Keep tests independent by restoring initial user state before and after each test."""
    api_client.reset_balance()
    yield
    api_client.reset_balance()


@pytest.fixture(scope="function")
def driver():
    chrome_options = ChromeOptions()
    if settings.headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1440,1200")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()
