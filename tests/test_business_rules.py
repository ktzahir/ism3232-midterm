from business_rules import (
    calculate_bean_cost,
    calculate_shipment_total,
    get_bulk_discount,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
)


def test_calculate_bean_cost():
    """Check the original cost of coffee bags."""
    assert calculate_bean_cost(14.00, 10) == 140.00


def test_discount_below_twenty_bags():
    """Check that small orders receive no discount."""
    assert get_bulk_discount(10) == 0.0


def test_discount_twenty_bags():
    """Check the standard bulk discount."""
    assert get_bulk_discount(20) == 0.09


def test_discount_eighty_bags():
    """Check the largest bulk discount."""
    assert get_bulk_discount(80) == 0.14


def test_partner_discount():
    """Check the extra discount for partner cafes."""
    assert round(get_bulk_discount(40, True), 2) == 0.13


def test_shipment_with_shipping_fee():
    """Check that shipping is added for small orders."""
    assert round(calculate_shipment_total(14.00, 10), 2) == 175.00


def test_shipment_without_shipping_fee():
    """Check that larger orders avoid the shipping fee."""
    assert round(calculate_shipment_total(13.00, 40), 2) == 473.20


def test_prepayment_below_threshold():
    """Check that a shipment below $1500 needs no prepayment."""
    assert requires_prepayment(1499.99) is False


def test_prepayment_at_threshold():
    """Check that a $1500 shipment requires prepayment."""
    assert requires_prepayment(1500.00) is True


def test_pallet_below_bag_threshold():
    """Check that 60 bags do not require a pallet."""
    assert needs_pallet(60, 800.00) is False


def test_pallet_above_both_thresholds():
    """Check that a large shipment requires a pallet."""
    assert needs_pallet(61, 800.00) is True


def test_pallet_below_total_threshold():
    """Check that a shipment below $700 needs no pallet."""
    assert needs_pallet(61, 699.99) is False


def test_total_shipped_two_shipments():
    """Check the combined total of two coffee shipments."""
    shipments = [
        {"bag_price": 14.00, "bags": 10, "partner": False},
        {"bag_price": 13.00, "bags": 40, "partner": False},
    ]

    assert round(total_shipped(shipments), 2) == 648.20


def test_total_shipped_empty_list():
    """Check that an empty shipment list returns zero."""
    assert total_shipped([]) == 0.0


def test_total_shipped_one_partner_shipment():
    """Check the total for one partner cafe shipment."""
    shipments = [
        {"bag_price": 12.00, "bags": 50, "partner": True},
    ]

    assert round(total_shipped(shipments), 2) == 522.00


def test_largest_shipment_two_buyers():
    """Check which buyer has the largest shipment."""
    shipments = [
        {"buyer": "Uptown Bakery", "bag_price": 14.00, "bags": 10, "partner": False},
        {"buyer": "Wren Hotel", "bag_price": 13.00, "bags": 40, "partner": False},
    ]

    assert largest_shipment(shipments) == "Wren Hotel"


def test_largest_shipment_empty_list():
    """Check that an empty list returns an empty string."""
    assert largest_shipment([]) == ""


def test_largest_shipment_tie():
    """Check that the first buyer wins when totals are tied."""
    shipments = [
        {"buyer": "Cafe A", "bag_price": 12.00, "bags": 40, "partner": False},
        {"buyer": "Cafe B", "bag_price": 12.00, "bags": 40, "partner": False},
    ]

    assert largest_shipment(shipments) == "Cafe A"
