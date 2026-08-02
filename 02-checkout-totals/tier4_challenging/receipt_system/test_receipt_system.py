"""
AUTOMATED TESTS for the receipt_system project.

You don't need to edit this file! Run it with:
    pytest
from inside this receipt_system/ folder, once you've written some code in
cart.py and checkout.py. Each test checks one small piece of behaviour and
will tell you exactly what passed (.) or failed (F).

Tip: work through the tests from top to bottom — later tests depend on
earlier code working correctly.
"""

import pytest
from cart import Cart, load_menu
from checkout import Checkout


@pytest.fixture
def menu():
    return load_menu()


def test_cart_add_item(menu):
    cart = Cart(menu)
    cart.add_item("Coffee", 2)
    assert cart.items["Coffee"] == 2


def test_cart_add_invalid_item_ignored(menu):
    cart = Cart(menu)
    cart.add_item("Pizza", 1)
    assert "Pizza" not in cart.items


def test_cart_remove_item(menu):
    cart = Cart(menu)
    cart.add_item("Coffee", 2)
    cart.remove_item("Coffee", 1)
    assert cart.items["Coffee"] == 1


def test_cart_remove_all_deletes_entry(menu):
    cart = Cart(menu)
    cart.add_item("Coffee", 1)
    cart.remove_item("Coffee", 1)
    assert "Coffee" not in cart.items


def test_cart_subtotal(menu):
    cart = Cart(menu)
    cart.add_item("Coffee", 2)   # 2 x $4.50 = $9.00
    cart.add_item("Muffin", 1)   # 1 x $5.00 = $5.00
    assert round(cart.get_subtotal(), 2) == 14.00


def test_checkout_no_discounts(menu):
    cart = Cart(menu)
    cart.add_item("Coffee", 2)
    cart.add_item("Muffin", 1)
    checkout = Checkout(cart)
    # $14.00 + 10% GST = $15.40
    assert round(checkout.calculate_total(), 2) == 15.40


def test_checkout_loyalty_discount(menu):
    cart = Cart(menu)
    cart.add_item("Coffee", 2)
    cart.add_item("Muffin", 1)
    checkout = Checkout(cart, is_loyalty_member=True)
    # $14.00 -> $12.60 after 10% loyalty -> $13.86 with GST
    assert round(checkout.calculate_total(), 2) == 13.86


def test_checkout_voucher_and_loyalty(menu):
    cart = Cart(menu)
    cart.add_item("Coffee", 2)
    cart.add_item("Muffin", 1)
    checkout = Checkout(cart, is_loyalty_member=True, voucher_code="SAVE10")
    # $14.00 -> $12.60 (loyalty) -> $11.34 (voucher) -> $12.47 (GST)
    assert round(checkout.calculate_total(), 2) == 12.47


def test_generate_receipt_includes_total(menu):
    cart = Cart(menu)
    cart.add_item("Coffee", 2)
    cart.add_item("Muffin", 1)
    checkout = Checkout(cart)
    receipt = checkout.generate_receipt()
    assert "TOTAL" in receipt
    assert "15.4" in receipt
