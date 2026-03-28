from pages.bet_slip_page import BetSlipPage
from pages.matches_page import MatchesPage


def test_user_can_place_single_bet_and_see_receipt(driver):
    """Automates the core business journey.

    This test was prioritized because it validates the highest-value user flow end to end:
    selection -> stake entry -> placement -> success receipt.
    """
    matches_page = MatchesPage(driver)
    bet_slip = BetSlipPage(driver)

    matches_page.load()
    matches_page.wait_until_loaded()
    matches_page.select_first_home_outcome()

    bet_slip.enter_stake("10")
    bet_slip.place_bet()

    assert bet_slip.receipt_is_displayed(), "Expected success receipt modal to appear after placement."
    assert bet_slip.is_visible(*bet_slip.BET_ID), "Bet receipt should include Bet ID."
    assert bet_slip.is_visible(*bet_slip.MATCH_DETAILS), "Bet receipt should include match details."
    assert bet_slip.is_visible(*bet_slip.STAKE_LINE), "Bet receipt should include placed stake."
    assert bet_slip.is_visible(*bet_slip.ODDS_LINE), "Bet receipt should include odds at placement."
    assert bet_slip.is_visible(*bet_slip.PAYOUT_LINE), "Bet receipt should include potential payout."
