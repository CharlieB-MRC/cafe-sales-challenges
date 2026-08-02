"""
AUTOMATED TESTS for the loyalty_system project.

You don't need to edit this file! Run it with:
    pytest
from inside this loyalty_system/ folder, once you've written some code in
customer.py and database.py. Each test checks one small piece of
behaviour and will tell you exactly what passed (.) or failed (F).

Tip: work through the tests from top to bottom — later tests depend on
earlier code working correctly.
"""

import pytest
from customer import Customer
from database import CustomerDatabase


def test_customer_starts_with_given_points():
    c = Customer("Priya Nair", "priya@example.com", 45)
    assert c.points == 45


def test_customer_add_points():
    c = Customer("Priya Nair", "priya@example.com", 45)
    c.add_points(10)
    assert c.points == 55


def test_customer_redeem_points_success():
    c = Customer("Priya Nair", "priya@example.com", 45)
    result = c.redeem_points(20)
    assert result is True
    assert c.points == 25


def test_customer_redeem_points_not_enough():
    c = Customer("Priya Nair", "priya@example.com", 45)
    result = c.redeem_points(500)
    assert result is False
    assert c.points == 45


def test_customer_tier_bronze():
    c = Customer("A", "a@example.com", 50)
    assert c.get_tier() == "Bronze"


def test_customer_tier_silver():
    c = Customer("B", "b@example.com", 150)
    assert c.get_tier() == "Silver"


def test_customer_tier_gold():
    c = Customer("C", "c@example.com", 300)
    assert c.get_tier() == "Gold"


@pytest.fixture
def db():
    return CustomerDatabase()


def test_database_loads_customers(db):
    assert len(db.customers) == 5


def test_database_find_customer(db):
    found = db.find_customer("sam@example.com")
    assert found is not None
    assert found.name == "Sam Tran"


def test_database_find_customer_missing(db):
    assert db.find_customer("nobody@example.com") is None


def test_database_register_new_customer(db):
    before = len(db.customers)
    db.register_customer("Nadia Kim", "nadia@example.com")
    assert len(db.customers) == before + 1


def test_database_register_existing_customer_no_duplicate(db):
    before = len(db.customers)
    db.register_customer("Sam Tran", "sam@example.com")
    assert len(db.customers) == before


def test_database_top_customers(db):
    top = db.top_customers(2)
    assert len(top) == 2
    assert top[0].points >= top[1].points
    assert top[0].name == "Jordan Lee"
