from managers.file_manager import FileManager


class TransactionManager:
    def __init__(self):
        self.transactions = FileManager.load_transactions()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def edit_transaction(self, index, new_transaction):
        if 0 <= index < len(self.transactions):
            self.transactions[index] = new_transaction
        else:
            raise IndexError("Недопустимый индекс транзакции")

    def search_transactions(self, category=None, date=None, amount=None):
        result = []
        for transaction in self.transactions:
            if (category is None or transaction.category.lower() == category.lower()) or \
                    (date is None or transaction.date == date) or \
                    (amount is None or transaction.amount == amount):
                result.append(transaction)
        return result

    def calculate_balance(self):
        income = 0
        expense = 0
        for transaction in self.transactions:
            if transaction.category.lower() == 'доход':
                income += transaction.amount
            elif transaction.category.lower() == 'расход':
                expense += transaction.amount
        balance = income - expense
        return balance, income, expense

    def display_balance(self):
        balance, income, expense = self.calculate_balance()
        print(f"Текущий баланс: {balance}")
        print(f"Доходы: {income}")
        print(f"Расходы: {expense}")
