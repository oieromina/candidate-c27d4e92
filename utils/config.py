from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Central test configuration for UI and API layers."""

    user_id: str = os.getenv("USER_ID", "candidate-c27d4e92")
    base_url: str = os.getenv("BASE_URL", "https://qae-assignment-tau.vercel.app/")
    browser: str = os.getenv("BROWSER", "chrome")
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"
    explicit_wait: int = int(os.getenv("EXPLICIT_WAIT", "10"))

    @property
    def app_url(self) -> str:
        return f"{self.base_url}/?user-id={self.user_id}"

    @property
    def api_url(self) -> str:
        return f"{self.base_url}/api"


settings = Settings()
