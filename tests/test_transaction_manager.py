import pytest
from datetime import datetime
from unittest.mock import patch

from managers.transaction_manager import TransactionManager
from models.transaction import Transaction


@pytest.fixture
def temp_file(tmp_path):
    temp_file_path = tmp_path / 'test_transaction.json'
    yield temp_file_path


def test_add_transaction(temp_file):
    with patch('managers.file_manager.FileManager.save_transactions') as mock_save_transactions:
        manager = TransactionManager()
        initial_transactions_count = len(manager.transactions)

        transaction_id = Transaction.generate_id(manager.transactions)
        transaction = Transaction(transaction_id, datetime.now().strftime('%d-%m-%Y'), 'доход', 100, 'Test transaction')
        manager.add_transaction(transaction)

        assert len(manager.transactions) == initial_transactions_count + 1
        assert mock_save_transactions.called


def test_edit_transaction(temp_file):
    with patch('managers.file_manager.FileManager.save_transactions') as mock_save_transactions:
        manager = TransactionManager()

        transaction_id = Transaction.generate_id(manager.transactions)
        transaction1 = Transaction(transaction_id, datetime.now().strftime('%d-%m-%Y'), 'доход', 100,
                                   'Test transaction 1')
        manager.add_transaction(transaction1)

        transaction_id = Transaction.generate_id(manager.transactions)
        transaction2 = Transaction(transaction_id, datetime.now().strftime('%d-%m-%Y'), 'расход', 50,
                                   'Test transaction 2')
        manager.add_transaction(transaction2)

        new_transaction = Transaction(transaction_id, datetime.now().strftime('%d-%m-%Y'), 'расход', 75,
                                      'Updated transaction 1')
        manager.edit_transaction(0, new_transaction)

        assert manager.transactions[0].amount == 75
        assert mock_save_transactions.called


def test_search_transactions(temp_file):
    with patch('managers.file_manager.FileManager.save_transactions') as mock_save_transactions:
        manager = TransactionManager()

        transaction_id = Transaction.generate_id(manager.transactions)
        transaction1 = Transaction(transaction_id, datetime.now().strftime('%d-%m-%Y'), 'доход', 100,
                                   'Test transaction 1')
        manager.add_transaction(transaction1)

        transaction_id = Transaction.generate_id(manager.transactions)
        transaction2 = Transaction(transaction_id, datetime.now().strftime('%d-%m-%Y'), 'расход', 50,
                                   'Test transaction 2')
        manager.add_transaction(transaction2)

        assert len(manager.search_transactions(category='доход', date='', amount=0)) == 1
        assert len(manager.search_transactions(date=datetime.now().strftime('%d-%m-%Y'), category='', amount=0)) == 2
        assert len(manager.search_transactions(amount=100, category='', date='')) == 1


def test_calculate_balance(temp_file):
    with patch('managers.file_manager.FileManager.save_transactions') as mock_save_transactions:
        manager = TransactionManager()

        transaction_id = Transaction.generate_id(manager.transactions)
        transaction1 = Transaction(transaction_id, datetime.now().strftime('%d-%m-%Y'), 'доход', 100,
                                   'Test transaction 1')
        manager.add_transaction(transaction1)

        transaction_id = Transaction.generate_id(manager.transactions)
        transaction2 = Transaction(transaction_id, datetime.now().strftime('%d-%m-%Y'), 'расход', 50,
                                   'Test transaction 2')
        manager.add_transaction(transaction2)

        assert manager.calculate_balance() == {'balance': 50, 'income': 100, 'expense': 50}


def test_get_balance(temp_file):
    with patch('managers.file_manager.FileManager.save_transactions') as mock_save_transactions:
        manager = TransactionManager()

        transaction_id = Transaction.generate_id(manager.transactions)
        transaction1 = Transaction(transaction_id, datetime.now().strftime('%d-%m-%Y'), 'доход', 100,
                                   'Test transaction 1')
        manager.add_transaction(transaction1)

        transaction_id = Transaction.generate_id(manager.transactions)
        transaction2 = Transaction(transaction_id, datetime.now().strftime('%d-%m-%Y'), 'расход', 50,
                                   'Test transaction 2')
        manager.add_transaction(transaction2)

        assert manager.get_balance() == {'balance': 50, 'income': 100, 'expense': 50}
