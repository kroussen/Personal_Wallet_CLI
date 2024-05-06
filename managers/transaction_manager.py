from managers.file_manager import FileManager
from typing import List, Optional, Union, Dict
from models.transaction import Transaction


class TransactionManager:
    def __init__(self) -> None:
        self.transactions: List[Transaction] = FileManager.load_transactions()

    def add_transaction(self, transaction: Transaction) -> None:
        """
        Добавляет новую транзакцию в список транзакций и сохраняет его в файл.

        :param transaction: Объект транзакции для добавления.
        :type transaction: Transaction
        :return: None
        """
        self.transactions.append(transaction)
        FileManager.save_transactions(self.transactions)

    def edit_transaction(self, index: int, new_transaction: Transaction) -> None:
        """
        Редактирует существующую транзакцию в списке транзакций по указанному индексу и сохраняет его в файл.

        :param index: Индекс транзакции для редактирования.
        :type index: int
        :param new_transaction: Новая транзакция для замены существующей.
        :type new_transaction: Transaction
        :return: None
        """
        self.transactions[int(index)] = new_transaction
        FileManager.save_transactions(self.transactions)

    def search_transactions(self, category: Optional[str] = None, date: Optional[str] = None,
                            amount: Optional[Union[float, str]] = None) -> List[Transaction]:
        """
        Поиск транзакций по заданным критериям.

        :param category: Категория транзакции для поиска.
        :type category: str or None
        :param date: Дата транзакции для поиска.
        :type date: str or None
        :param amount: Сумма транзакции для поиска.
        :type amount: float or str or None
        :return: Список найденных транзакций.
        :rtype: List[Transaction]
        """
        result = []
        for transaction in self.transactions:
            if (category is None or transaction.category.lower() == category.lower()) or \
                    (date is None or transaction.date == date) or \
                    (amount is None or transaction.amount == amount):
                result.append(transaction)
        return result

    def calculate_balance(self) -> Dict[str, float]:
        """
        Вычисляет баланс доходов и расходов.

        :return: Словарь с балансом, доходами и расходами.
        :rtype: Dict[str, float]
        """
        income = 0
        expense = 0
        for transaction in self.transactions:
            if transaction.category.lower() == 'доход':
                income += transaction.amount
            elif transaction.category.lower() == 'расход':
                expense += transaction.amount
        balance = income - expense
        return {'balance': balance, 'income': income, 'expense': expense}

    def get_balance(self) -> Dict[str, float]:
        """
        Возвращает текущий баланс.

        :return: Словарь с текущим балансом, доходами и расходами.
        :rtype: Dict[str, float]
        """
        budget = self.calculate_balance()
        return budget
