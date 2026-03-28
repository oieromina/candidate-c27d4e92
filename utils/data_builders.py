from decimal import Decimal


def two_decimals(value: str | float | int) -> float:
    """Normalize numeric data the same way business rules describe stake precision."""
    return float(Decimal(str(value)).quantize(Decimal("0.01")))
