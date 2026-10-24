from business_rules import (
    calculate_shipment_total,
    format_shipment_line,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
)

shipments = [
    {"buyer": "Uptown Bakery", "bag_price": 14.00, "bags": 10, "partner": False},
    {"buyer": "Vine Cafe", "bag_price": 12.50, "bags": 15, "partner": True},
    {"buyer": "Wren Hotel", "bag_price": 13.00, "bags": 40, "partner": False},
    {"buyer": "Yarrow Cafe", "bag_price": 12.00, "bags": 50, "partner": True},
    {"buyer": "Zenith Grocers", "bag_price": 11.00, "bags": 200, "partner": False},
    {"buyer": "Alder Hotel", "bag_price": 12.00, "bags": 60, "partner": False},
    {"buyer": "Birch Diner", "bag_price": 11.00, "bags": 61, "partner": False},
    {"buyer": "Cove Market", "bag_price": 13.00, "bags": 150, "partner": True},
]


print("Copper Kettle Coffee Roasters - Shipment Report")

prepayment_count = 0
pallet_count = 0

for shipment in shipments:
    total = calculate_shipment_total(
        shipment["bag_price"],
        shipment["bags"],
        shipment["partner"],
    )

    prepayment = requires_prepayment(total)
    pallet = needs_pallet(shipment["bags"], total)

    if prepayment:
        prepayment_count += 1

    if pallet:
        pallet_count += 1

    print(
        format_shipment_line(
            shipment["buyer"],
            total,
            prepayment,
            pallet,
        )
    )

grand_total = total_shipped(shipments)
average_total = grand_total / len(shipments)
largest_buyer = largest_shipment(shipments)

print(f"Shipments: {len(shipments)}")
print(f"Total shipped: ${grand_total:.2f}")
print(f"Average shipment total: ${average_total:.2f}")
print(f"Largest shipment total: {largest_buyer}")
print(f"Prepayments required: {prepayment_count}")
print(f"Pallets needed: {pallet_count}")
