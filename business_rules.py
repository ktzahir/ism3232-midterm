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


def total_shipped(shipments: list) -> float:
    """Calculate the total value of all coffee shipments."""
    total = 0.0

    for shipment in shipments:
        shipment_total = calculate_shipment_total(
            shipment["bag_price"],
            shipment["bags"],
            shipment["partner"],
        )
        total += shipment_total

    return total


def largest_shipment(shipments: list) -> str:
    """Return the buyer with the largest shipment total."""
    if not shipments:
        return ""

    largest_buyer = ""
    largest_total = -1.0

    for shipment in shipments:
        shipment_total = calculate_shipment_total(
            shipment["bag_price"],
            shipment["bags"],
            shipment["partner"],
        )

        if shipment_total > largest_total:
            largest_total = shipment_total
            largest_buyer = shipment["buyer"]

    return largest_buyer


def format_shipment_line(
    buyer: str, total: float, prepayment: bool, pallet: bool
) -> str:
    """Format a shipment as one readable report line."""
    prepayment_text = "yes" if prepayment else "no"
    pallet_text = "yes" if pallet else "no"

    return (
        f"{buyer}: ${total:.2f} | prepayment: {prepayment_text} | pallet: {pallet_text}"
    )
