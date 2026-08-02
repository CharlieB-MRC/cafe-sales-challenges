"""
AUTOMATED TESTS for the inventory_system project.

You don't need to edit this file! Run it with:
    pytest
from inside this inventory_system/ folder, once you've written some code in
inventory.py, alerts.py, and reorder.py. Each test checks one small piece
of behaviour and will tell you exactly what passed (.) or failed (F).

Tip: work through the tests from top to bottom — later tests depend on
earlier code working correctly.
"""

import pytest
from inventory import Inventory
from alerts import get_low_stock_items, build_alert_messages
from reorder import calculate_reorder_amounts


@pytest.fixture
def inventory():
    return Inventory()


def test_inventory_loads_items(inventory):
    items = inventory.list_items()
    assert "Coffee Beans" in items
    assert "Napkins" in items


def test_get_item(inventory):
    item = inventory.get_item("Coffee Beans")
    assert item.quantity == 12
    assert inventory.get_item("Pizza") is None


def test_restock(inventory):
    inventory.restock("Coffee Beans", 10)
    assert inventory.get_item("Coffee Beans").quantity == 22


def test_sell_never_goes_negative(inventory):
    inventory.sell("Tea Bags", 100)
    assert inventory.get_item("Tea Bags").quantity == 0


def test_sell_normal_amount(inventory):
    inventory.sell("Milk", 5)
    assert inventory.get_item("Milk").quantity == 15


def test_get_low_stock_items(inventory):
    low_items = get_low_stock_items(inventory)
    low_names = [item.name for item in low_items]
    assert "Sugar Sachets" in low_names
    assert "Oat Milk" in low_names
    assert "Milk" not in low_names


def test_build_alert_messages(inventory):
    messages = build_alert_messages(inventory)
    assert any("Sugar Sachets" in message for message in messages)
    assert any("LOW STOCK" in message for message in messages)


def test_calculate_reorder_amounts(inventory):
    amounts = calculate_reorder_amounts(inventory)
    # Sugar Sachets: quantity=2, target_stock=25 -> order 23
    assert amounts["Sugar Sachets"] == 23
    # Oat Milk: quantity=3, target_stock=15 -> order 12
    assert amounts["Oat Milk"] == 12
    # Healthy items should not appear at all
    assert "Milk" not in amounts


def test_save_and_reload(tmp_path, inventory):
    inventory.sell("Coffee Beans", 2)
    save_path = tmp_path / "saved_inventory.csv"
    inventory.save(str(save_path))

    reloaded = Inventory(data_path=str(save_path))
    assert reloaded.get_item("Coffee Beans").quantity == 10
