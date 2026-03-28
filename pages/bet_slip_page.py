from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BetSlipPage(BasePage):
    STAKE_INPUT = (By.CSS_SELECTOR, "input[name='stake'], input[type='number']")
    PLACE_BET_BUTTON = (By.XPATH, "//button[contains(., 'Place Bet') or contains(., 'Placing')]" )
    RECEIPT_MODAL = (By.CSS_SELECTOR, "[role='dialog'], .modal")
    RECEIPT_TITLE = (By.XPATH, "//*[contains(text(), 'Bet Receipt') or contains(text(), 'Success')]")
    BET_ID = (By.XPATH, "//*[contains(text(), 'Bet ID')]")
    MATCH_DETAILS = (By.XPATH, "//*[contains(text(), 'vs')]")
    STAKE_LINE = (By.XPATH, "//*[contains(text(), 'Stake')]")
    ODDS_LINE = (By.XPATH, "//*[contains(text(), 'Odds')]")
    PAYOUT_LINE = (By.XPATH, "//*[contains(text(), 'Payout') or contains(text(), 'Potential payout')]")
    CLOSE_RECEIPT = (By.XPATH, "//button[contains(., 'Close') or contains(., 'Done') or contains(., 'OK')]")

    def enter_stake(self, stake: str) -> None:
        self.type(*self.STAKE_INPUT, text=stake)

    def place_bet(self) -> None:
        self.click(*self.PLACE_BET_BUTTON)

    def receipt_is_displayed(self) -> bool:
        return self.is_visible(*self.RECEIPT_MODAL)

    def close_receipt(self) -> None:
        self.click(*self.CLOSE_RECEIPT)
