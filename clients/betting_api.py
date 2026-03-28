from __future__ import annotations

from typing import Any
import requests

from utils.config import settings


class BettingApiClient:
    """Thin HTTP client for the betting API.

    Chosen to keep tests readable and centralize request defaults.
    """

    def __init__(self) -> None:
        self.base_api_url = settings.api_url
        self.session = requests.Session()
        self.session.headers.update({"x-user-id": settings.user_id})

    def get_matches(self) -> requests.Response:
        return self.session.get(f"{self.base_api_url}/matches", timeout=20)

    def get_balance(self) -> requests.Response:
        return self.session.get(f"{self.base_api_url}/balance", timeout=20)

    def place_bet(self, payload: dict[str, Any], method: str = "POST") -> requests.Response:
        return self.session.request(
            method=method,
            url=f"{self.base_api_url}/place-bet",
            json=payload,
            timeout=20,
        )

    def reset_balance(self) -> requests.Response:
        return self.session.post(f"{self.base_api_url}/reset-balance", timeout=20)
