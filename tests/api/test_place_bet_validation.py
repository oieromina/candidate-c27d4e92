
def test_place_bet_rejects_more_than_two_decimal_places(api_client):
    """Validates a high-risk money rule directly at the API layer.

    Stake precision errors are easy to miss in the UI and can cause payout or accounting defects,
    so this was chosen as a fast, deterministic API check.
    """
    matches_response = api_client.get_matches()
    assert matches_response.status_code == 200, "Precondition failed: match catalog was not returned."

    first_match_id = matches_response.json()[0]["id"]
    payload = {
        "matchId": first_match_id,
        "selection": "HOME",
        "stake": 10.123,
    }

    response = api_client.place_bet(payload)

    assert response.status_code == 422, (
        f"Expected semantic validation failure for precision rule, got {response.status_code}: {response.text}"
    )
