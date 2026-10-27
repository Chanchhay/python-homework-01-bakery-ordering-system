"""Bakery Ordering System - run with: python bakery_ordering_system.py."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

# Decimal avoids floating-point rounding errors with money.
ITEMS = {
    "1": ("Croissant", Decimal("10.00")),
    "2": ("Chocolate Muffin", Decimal("2.50")),
    "3": ("Bread", Decimal("2.00")),
}
CENT = Decimal("0.01")
ZERO = Decimal("0.00")


def money(amount: Decimal) -> str:
    return "$" + f"{amount:.2f}"


def show_main_menu() -> None:
    print("=" * 32)
    print("    WELCOME TO OUR BAKERY")
    print("=" * 32)
    print("1. Order Items")
    print("2. View Total")
    print("3. Checkout")
    print("4. Exit")
    print("=" * 32)


def order_item(subtotal: Decimal) -> Decimal:
    """Select one bakery item, then return to the main menu."""
    print("\n==========BAKERY MENU==========")
    for number, (name, price) in ITEMS.items():
        print(f"{number}. {name:<20}{money(price)}")
    print("4. Back to Main Menu")
    print("=" * 31)
    choice = input("Select an item: ").strip()
    if choice in ITEMS:
        name, price = ITEMS[choice]
        subtotal += price
        print(f"{name} added successfully!")
        print(f"Current Subtotal: {money(subtotal)}")
    elif choice != "4":
        print("Invalid item selection!")
        print("Subtotal remains unchanged.")
        print(f"Current Subtotal: {money(subtotal)}")
    return subtotal


def view_total(subtotal: Decimal) -> None:
    print("\n==========YOUR ORDER==========")
    if subtotal == ZERO:
        print("Your order is empty")
    else:
        print(f"Current Subtotal: {money(subtotal)}")
    print("=" * 30)


def calculate_discount(subtotal: Decimal) -> Decimal:
    """10% discount on a subtotal of $10.00 or more."""
    if subtotal >= Decimal("10.00"):
        return (subtotal * Decimal("0.10")).quantize(CENT, rounding=ROUND_HALF_UP)
    return ZERO


def checkout(subtotal: Decimal) -> Decimal:
    print("\n===========CHECKOUT===========")
    if subtotal == ZERO:
        print("Your order is empty.")
        print("Please order something first.")
        print("=" * 30)
        return subtotal

    discount = calculate_discount(subtotal)
    final_total = subtotal - discount
    print(f"Subtotal:         {money(subtotal)}")
    if discount:
        print(f"Discount (10%):   {money(discount)}")
    else:
        print(f"Discount:         {money(discount)}")
    print("-" * 30)
    print(f"Final Total:      {money(final_total)}")

    cash_text = input("Enter cash received ($): ").strip()
    try:
        cash = Decimal(cash_text)
        if not cash.is_finite() or cash < ZERO or cash != cash.quantize(CENT):
            raise InvalidOperation
    except (InvalidOperation, ValueError):
        print("Invalid cash amount! Please enter a non-negative amount in dollars and cents.")
        return subtotal

    print("\n===========PAYMENT============")
    if cash >= final_total:
        print(f"Final Total:      {money(final_total)}")
        print(f"Cash Received:    {money(cash)}")
        print(f"Change:           {money(cash - final_total)}")
        print("=" * 30)
        return ZERO  # Reset the completed order for the next purchase.

    print("Insufficient Payment!")
    print(f"You need {money(final_total - cash)} more.")
    print("=" * 30)
    return subtotal


def main() -> None:
    subtotal = ZERO
    while True:
        print()
        show_main_menu()
        option = input("Select an option: ").strip()
        if option == "1":
            subtotal = order_item(subtotal)
        elif option == "2":
            view_total(subtotal)
        elif option == "3":
            subtotal = checkout(subtotal)
        elif option == "4":
            print("Thank you for visiting our Bakery!")
            print("Have a wonderful day!")
            break
        else:
            print("Invalid option! Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
