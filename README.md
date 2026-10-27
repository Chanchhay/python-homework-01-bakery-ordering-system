# Bakery Ordering System

Complete Python console program for the six-page Bakery Ordering System homework.
Requires Python 3.9 or later. No external packages required.

## How to run

Open a terminal inside this folder:

    python bakery_ordering_system.py

On macOS/Linux, you may need to type python3 instead of python.

## Main menu

1. Order Items - select exactly one bakery item each time you enter the bakery menu.
2. View Total - display the current subtotal, or say the order is empty.
3. Checkout - calculate a discount, enter cash, and calculate change.
4. Exit - display the farewell messages and close the program.

Bakery item prices:

| Item | Price |
| --- | ---: |
| Croissant | $10.00 |
| Chocolate Muffin | $2.50 |
| Bread | $2.00 |

There is also a Back to Main Menu option on the item menu.

## Rules

- Apply a 10% discount when the subtotal is $10.00 or more.
- No discount when the subtotal is below $10.00.
- Do not check out an empty order.
- When cash is sufficient, show cash received and change.
- When cash is insufficient, show exactly how much more is needed.
- Invalid choices do not change the subtotal.
- The main menu repeats until Exit is selected.

After successful checkout the paid order is cleared for the next customer.
After insufficient or invalid payment, the order is kept.

## Example

Order a Croissant and Chocolate Muffin:

    Subtotal:         $12.50
    Discount (10%):   $1.25
    ------------------------------
    Final Total:      $11.25
    Enter cash received ($): 20

    ===========PAYMENT============
    Final Total:      $11.25
    Cash Received:    $20.00
    Change:           $8.75
    ==============================

## Run tests

    python -m unittest discover -s tests -v

## Project files

- bakery_ordering_system.py: complete assignment program.
- tests/test_bakery_ordering_system.py: automated tests.
- README.md: these usage instructions.
