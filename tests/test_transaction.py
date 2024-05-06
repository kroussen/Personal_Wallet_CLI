import pytest
from datetime import datetime

from models.transaction import Transaction


@pytest.fixture
def valid_transaction():
    return Transaction(1, '01-01-2022', 'доход', 100, 'Описание')


@pytest.fixture
def invalid_date_transaction():
    return Transaction(1, '2022-01-01', 'доход', 100, 'Описание')


@pytest.fixture
def invalid_category_transaction():
    return Transaction(1, '01-01-2022', 'неизвестная категория', 100, 'Описание')


@pytest.fixture
def invalid_amount_transaction():
    return Transaction(1, '01-01-2022', 'доход', 'invalid_amount', 'Описание')


def test_valid_transaction(valid_transaction):
    assert isinstance(valid_transaction, Transaction)
    assert valid_transaction.transaction_id == 1
    assert valid_transaction.date == '01-01-2022'
    assert valid_transaction.category == 'доход'
    assert valid_transaction.amount == 100
    assert valid_transaction.description == 'Описание'


def test_invalid_date_transaction(invalid_date_transaction):
    assert isinstance(invalid_date_transaction.date, list)
    assert invalid_date_transaction.date[0] == 'error_message'


def test_invalid_category_transaction(invalid_category_transaction):
    assert isinstance(invalid_category_transaction.category, list)
    assert invalid_category_transaction.category[0] == 'error_message'


def test_invalid_amount_transaction(invalid_amount_transaction):
    assert isinstance(invalid_amount_transaction.amount, list)
    assert invalid_amount_transaction.amount[0] == 'error_message'


def test_get_errors(valid_transaction, invalid_date_transaction, invalid_category_transaction, invalid_amount_transaction):
    assert valid_transaction.get_errors() == []
    assert invalid_date_transaction.get_errors() == ["Неверный формат даты. Используйте формат ДД-ММ-ГГГГ."]
    assert invalid_category_transaction.get_errors() == ["Неверная категория. Категория должна быть 'Доход' или 'Расход'."]
    assert invalid_amount_transaction.get_errors() == ["Некорректное значение суммы."]