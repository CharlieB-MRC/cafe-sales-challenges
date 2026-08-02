"""
AUTOMATED TESTS for the pos_system project.

You don't need to edit this file! Run it with:
    pytest
from inside this pos_system/ folder, once you've written some code in
menu.py, order.py, and receipt.py. Each test checks one small piece of
behaviour and will tell you exactly what passed (.) or failed (F).

Tip: work through the tests from top to bottom — later tests depend on
earlier code working correctly.
"""

import pytest
from menu import Menu
from order import Order
from receipt import generate_receipt


@pytest.fixture
def menu():
    return Menu()


def test_menu_has_item(menu):
    assert menu.has_item("Coffee") is True
    assert menu.has_item("Pizza") is False


def test_menu_get_price(menu):
    assert menu.get_price("Coffee") == 4.50
    assert menu.get_price("Pizza") is None


def test_menu_list_items(menu):
    items = menu.list_items()
    assert "Coffee" in items
    assert "Muffin" in items


def test_order_add_item(menu):
    order = Order(menu)
    order.add_item("Coffee", 2)
    assert order.items["Coffee"] == 2


def test_order_add_invalid_item_ignored(menu):
    order = Order(menu)
    order.add_item("Pizza", 1)
    assert "Pizza" not in order.items


def test_order_remove_item(menu):
    order = Order(menu)
    order.add_item("Coffee", 2)
    order.remove_item("Coffee", 1)
    assert order.items["Coffee"] == 1


def test_order_subtotal(menu):
    order = Order(menu)
    order.add_item("Coffee", 2)   # 2 x $4.50 = $9.00
    order.add_item("Muffin", 1)   # 1 x $5.00 = $5.00
    assert round(order.get_subtotal(), 2) == 14.00


def test_generate_receipt_includes_total(menu):
    order = Order(menu)
    order.add_item("Coffee", 2)
    order.add_item("Muffin", 1)
    receipt = generate_receipt(order)
    assert "TOTAL" in receipt
    assert "15.4" in receipt  # $14.00 + 10% GST = $15.40
