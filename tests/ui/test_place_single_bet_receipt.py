from pages.bet_slip_page import BetSlipPage
from pages.matches_page import MatchesPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_user_can_place_single_bet_and_see_receipt(driver):
    """Automates the core business journey.

    This test was prioritized because it validates the highest-value user flow end to end:
    selection -> stake entry -> placement -> success receipt.
    """
    matches_page = MatchesPage(driver)
    bet_slip = BetSlipPage(driver)

    matches_page.load()
    #matches_page.wait_until_loaded()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, "bet-slip-title")))
    #matches_page.select_first_home_outcome()
    element2 = driver.find_element(By.ID, "odds-premier-league-manutd-chelsea-home")
    element2.click()
    element3 = driver.find_element(By.ID, "bet-slip-stake-input")
    element3.click()
    element3.send_keys("10")
    bet_slip.place_bet()
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modalTitle")))
    element4 = driver.find_element(By.CLASS_NAME, "modalTitle").text.strip()
    print(element4)

    assert element4 == "Bet Placed Successfully!"
    assert bet_slip.is_visible(*bet_slip.BET_ID), "Bet receipt should include Bet ID."
    assert bet_slip.is_visible(*bet_slip.MATCH_DETAILS), "Bet receipt should include match details."
    assert bet_slip.is_visible(*bet_slip.STAKE_LINE), "Bet receipt should include placed stake."
    assert bet_slip.is_visible(*bet_slip.ODDS_LINE), "Bet receipt should include odds at placement."
    assert bet_slip.is_visible(*bet_slip.PAYOUT_LINE), "Bet receipt should include potential payout."
