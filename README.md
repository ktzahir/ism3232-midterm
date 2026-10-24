
# ISM3232 Midterm: Copper Kettle Coffee Roasters

**Name:** Kazi Zahir
**Version:** ZETA
**Date:** October 24, 2026

## What This Program Does
This program helps Copper Kettle Coffee Roasters keep track of their coffee shipments and calculate how much each order costs. It checks for discounts, shipping fees, and whether an order needs prepayment or a pallet. At the end, it prints a report showing each shipment and the overall totals.



## Business Rules
Bean Cost: The program multiplies the price per bag by how many bags are ordered to get the total cost.

Bulk Discounts: Orders under 20 bags don't get a discount. Orders between 20 and 79 bags get 9% off, while orders with 80 or more bags get 14% off. Partners also get an extra 4% off if they order at least 20 bags.

Shipping: If the total after discounts is under $250, there is a $35 shipping fee. Orders that reach $250 or more get free shipping.

Prepayment: If a shipment costs $1,500 or more, the customer has to pay before the order is shipped.

Pallets: An order needs a pallet if it has more than 60 bags and the total is over $700.

Shipment Report: The program goes through each shipment, calculates the costs, and shows the total amount shipped, average cost, and largest shipment.
## How to Run
To run the program, open the project folder in VS Code and use the terminal. First, set up the virtual environment and install the packages needed for the project.

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

Once everything is set up, run the program using:

python3 main.py

This will print the shipment report with the costs, discounts, and totals for each order.


## How to Test
 used pytest and Ruff to test my program and check for errors.

ruff format --check .
ruff check .
pytest -v

Ruff checks the code formatting and looks for possible issues. Pytest runs the tests to make sure the business rules work correctly. All 27 tests passed.


## Files in This Repository
business_rules.py: Contains the functions that calculate shipment costs, discounts, and other business rules.

main.py: Runs the program and prints the shipment report.

tests/test_business_rules.py: Contains the 27 tests used to check the functions.

tests/__init__.py Marks the tests folder as a Python package.

requirements.txt: Lists the Python packages needed for the project.

.gitignore: Keeps unnecessary files and folders, like the virtual environment and Python cache files, off GitHub.

commands.md: Shows the terminal commands I used while working on the project.

README.md: Explains what the project does and how to run and test it.
## AI Use Statement
i did not use AI in this midterm. 