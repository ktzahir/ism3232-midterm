
# Terminal Record: Copper Kettle Coffee Roasters

## 1. Building the project

```bash
cd ~
mkdir ism3232-midterm
cd ism3232-midterm
pwd
git init
git status
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pytest ruff
python3 -m pip freeze > requirements.txt
mkdir tests
touch business_rules.py main.py tests/__init__.py tests/test_business_rules.py
touch commands.md README.md .gitignore
printf ".venv/\n__pycache__/\n.pytest_cache/\n.ruff_cache/\n" > .gitignore
git add .
git commit -m "Initialize midterm project structure"
git remote add origin https://github.com/ktzahir/ism3232-midterm.git
git remote -v
git push -u origin main
git remote set-url origin https://github.com/ktzahir/ISM3232-midterm-.git
git remote -v
git push -u origin main
git remote set-url origin https://github.com/ktzahir/ism3232-midterm.git
git remote -v
git status
```

## 2. The virtual environment

```bash
which python3
```

```text
/Users/tajbir/ism3232-midterm/.venv/bin/python3
```

The output shows my virtual environment is active because the Python path points to the `.venv/bin/` directory inside my midterm project.

## 3. The project structure

```bash
tree -L 2
```

```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The __pycache__ folder is on my computer but not on GitHub because Python creates it automatically, and I added it to .gitignore.

## 4. Every function and test

```bash
rg 'def '
```

```text
business_rules.py
15:def calculate_bean_cost(bag_price: float, bags: int) -> float:
20:def get_bulk_discount(bags: int, partner: bool = False) -> float:
35:def calculate_shipment_total(
50:def requires_prepayment(total: float) -> bool:
55:def needs_pallet(bags: int, total: float) -> bool:
60:def total_shipped(shipments: list) -> float:
75:def largest_shipment(shipments: list) -> str:
97:def format_shipment_line(

tests/test_business_rules.py
13:def test_calculate_bean_cost():
18:def test_discount_below_twenty_bags():
23:def test_discount_twenty_bags():
28:def test_discount_eighty_bags():
33:def test_partner_discount():
38:def test_shipment_with_shipping_fee():
43:def test_shipment_without_shipping_fee():
48:def test_prepayment_below_threshold():
53:def test_prepayment_at_threshold():
58:def test_pallet_below_bag_threshold():
63:def test_pallet_above_both_thresholds():
68:def test_pallet_below_total_threshold():
73:def test_total_shipped_two_shipments():
83:def test_total_shipped_empty_list():
88:def test_total_shipped_one_partner_shipment():
97:def test_largest_shipment_two_buyers():
107:def test_largest_shipment_empty_list():
112:def test_largest_shipment_tie():
122:def test_format_shipment_line_no_flags():
128:def test_format_shipment_line_both_flags():
134:def test_pallet_at_total_threshold():
139:def test_partner_discount_below_minimum():
144:def test_discount_just_below_eighty():
149:def test_shipping_fee_just_below_threshold():
154:def test_shipping_fee_at_threshold():
159:def test_pallet_total_just_above_threshold():
164:def test_pallet_bags_just_above_threshold():
```

 functions I created for the program and the tests I wrote to check that they work.


## 5. Which files print

```bash
rg -l 'print'
```

```text
main.py
```

Only main.py has print statements because it displays the shipment report. The functions in business_rules.py just return the values.


## 6. The commit history

```bash
git log --oneline
```

```text
c1f6373 (HEAD -> main, origin/main) Add final boundary tests for shipment rules
4e251c2 Add coffee shipment report and summaries
9e891a2 Add shipment report formatting and tests
f5e91dc Add shipment totals and largest shipment tests
2ac2d38 Add prepayment and pallet rules with tests
c857f7c Add coffee pricing functions and initial pytest tests
3ac9fc9 Initialize midterm project structure
```

A I have 7 commits showing the different steps I took to build my midterm project.