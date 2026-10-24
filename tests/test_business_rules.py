from business_rules import (
    calculate_bean_cost,
    calculate_shipment_total,
    get_bulk_discount,
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
