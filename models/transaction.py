from datetime import datetime
from typing import List, Union


class Transaction:
    def __init__(self, transaction_id: int = 0, date: str = None, category: str = None, amount: Union[float, str] = None,
                 description: str = ''):
        """
        Создает новый объект транзакции.

        :param transaction_id: Уникальный идентификатор транзакции.
        :param date: Дата транзакции в формате 'ДД-ММ-ГГГГ'.
        :param category: Категория транзакции ('доход' или 'расход').
        :param amount: Сумма транзакции.
        :param description: Описание транзакции.
        """
        self.transaction_id = transaction_id
        self.date = self.validate_date(date)
        self.category = self.validate_category(category)
        self.amount = self.validate_amount(amount)
        self.description = description

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта транзакции.

        :return: Строковое представление объекта транзакции.
        """
        return f"ID: {self.transaction_id}\n" \
               f"Дата: {self.date}\n" \
               f"Категория: {self.category}\n" \
               f"Сумма: {self.amount}\n" \
               f"Описание: {self.description}"

    @staticmethod
    def validate_date(date: str) -> Union[str, List[str]]:
        """
        Проверяет и форматирует строку даты.

        :param date: Строка даты.
        :return: Дата в формате 'ДД-ММ-ГГГГ' или список [error_message, message], если дата неверного формата.
        """
        try:
            datetime.strptime(date, '%d-%m-%Y')
            return date
        except ValueError:
            return ['error_message', "Неверный формат даты. Используйте формат ДД-ММ-ГГГГ."]

    @staticmethod
    def validate_category(category: str) -> Union[str, List[str]]:
        """
        Проверяет категорию транзакции.

        :param category: Категория транзакции.
        :return: Категория транзакции или список [error_message, message], если категория неверна.
        """
        if category.lower() not in ['доход', 'расход']:
            return ['error_message', "Неверная категория. Категория должна быть 'Доход' или 'Расход'."]
        return category

    @staticmethod
    def validate_amount(amount: Union[float, str]) -> Union[float, List[str]]:
        """
        Проверяет и форматирует сумму транзакции.

        :param amount: Сумма транзакции.
        :return: Сумма транзакции или список [error_message, message], если сумма неверна.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                return ['error_message', "Сумма должна быть положительной и больше нуля."]
            return amount
        except ValueError:
            return ['error_message', "Некорректное значение суммы."]

    def get_errors(self) -> List[str]:
        """
        Возвращает список ошибок объекта транзакции.

        :return: Список ошибок объекта транзакции.
        """
        errors = []
        for error in [self.date, self.category, self.amount, self.description]:
            if isinstance(error, list) and 'error_message' in error:
                errors.append(error[1])
        return errors

    @staticmethod
    def generate_id(transactions: List['Transaction']) -> int:
        """
        Генерирует уникальный идентификатор для новой транзакции.

        :param transactions: Список существующих транзакций.
        :return: Уникальный идентификатор для новой транзакции.
        """
        if not transactions:
            return 0
        return max(int(transaction.transaction_id) for transaction in transactions) + 1

    @staticmethod
    def is_valid_id(index: str, transactions: List['Transaction']) -> bool:
        """
        Проверяет, является ли индекс допустимым идентификатором транзакции.

        :param index: Индекс для проверки.
        :param transactions: Список существующих транзакций.
        :return: True, если индекс допустим, иначе False.
        """
        try:
            if 0 <= int(index) < len(transactions):
                return True
            return False
        except ValueError:
            return False
