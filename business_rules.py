# Coffee shipment business constants
BULK_MIN_BAGS = 20
LARGE_ORDER_BAGS = 80

STANDARD_DISCOUNT = 0.09
LARGE_ORDER_DISCOUNT = 0.14
PARTNER_EXTRA_DISCOUNT = 0.04
SHIPPING_FEE = 35.00
FREE_SHIPPING_THRESHOLD = 250.00
PREPAYMENT_THRESHOLD = 1500.00
PALLET_MIN_BAGS = 60
PALLET_TOTAL_THRESHOLD = 700.00


def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Calculate the original cost before discounts."""
    return bag_price * bags


def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Return the discount rate for a coffee shipment."""
    if bags >= LARGE_ORDER_BAGS:
        discount = LARGE_ORDER_DISCOUNT
    elif bags >= BULK_MIN_BAGS:
        discount = STANDARD_DISCOUNT
    else:
        discount = 0.0

    if partner and bags >= BULK_MIN_BAGS:
        discount += PARTNER_EXTRA_DISCOUNT

    return discount


def calculate_shipment_total(
    bag_price: float, bags: int, partner: bool = False
) -> float:
    """Calculate the final shipment total after discounts and shipping."""
    bean_cost = calculate_bean_cost(bag_price, bags)
    discount = get_bulk_discount(bags, partner)

    discounted_cost = bean_cost * (1 - discount)

    if discounted_cost < FREE_SHIPPING_THRESHOLD:
        discounted_cost += SHIPPING_FEE

    return discounted_cost


def requires_prepayment(total: float) -> bool:
    """Return whether a shipment requires prepayment."""
    return total >= PREPAYMENT_THRESHOLD


def needs_pallet(bags: int, total: float) -> bool:
    """Return whether a shipment needs a freight pallet."""
    return bags > PALLET_MIN_BAGS and total > PALLET_TOTAL_THRESHOLD
