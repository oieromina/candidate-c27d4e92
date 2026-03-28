from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import settings


class MatchesPage(BasePage):
    """Represents the main match list page.

    Locators are intentionally generic because the app is unknown at interview time.
    They can be hardened once stable test ids are available.
    """

    FIRST_MATCH_CARD = (By.CSS_SELECTOR, "[data-testid='match-card'], .match-card")
    FIRST_HOME_ODDS = (
        By.CSS_SELECTOR,
        "[data-testid='match-card'] [data-testid='odds-home'], .match-card button:nth-of-type(1)",
    )

    def load(self) -> None:
        self.open(settings.app_url)

    def wait_until_loaded(self) -> None:
        self.wait.until(lambda d: len(d.find_elements(*self.FIRST_MATCH_CARD)) > 0)

    def select_first_home_outcome(self) -> None:
        self.click(*self.FIRST_HOME_ODDS)
