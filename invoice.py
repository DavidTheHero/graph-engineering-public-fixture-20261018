"""Integer-cent invoice discounts; no external dependencies."""


def discounted_total(subtotal_cents: int, discount_percent: int) -> int:
    """Subtract the percentage discount, rounding discount cents down."""
    if subtotal_cents < 0:
        raise ValueError("subtotal must be nonnegative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount percentage must be between zero and one hundred")
    return subtotal_cents - subtotal_cents * discount_percent // 100
