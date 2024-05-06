import json
import os
from models.transaction import Transaction


class FileManager:
    @staticmethod
    def save_transactions(transactions, filename='transactions.json'):
        with open(filename, 'w') as file:
            json.dump([transaction.__dict__ for transaction in transactions], file, ensure_ascii=False)

    @staticmethod
    def load_transactions(filename='transactions.json'):
        transactions = []
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                json.dump([], file)
            return transactions
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                transactions.append(Transaction(**item))
        return transactions
