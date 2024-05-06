from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, date=None, category=None, amount=None, description=''):
        self.transaction_id = transaction_id
        self.date = self.validate_date(date)
        self.category = self.validate_category(category)
        self.amount = self.validate_amount(amount)
        self.description = description

    def __str__(self):
        return f"ID: {self.transaction_id}\n" \
               f"Дата: {self.date}\n" \
               f"Категория: {self.category}\n" \
               f"Сумма: {self.amount}\n" \
               f"Описание: {self.description}"

    @staticmethod
    def validate_date(date):
        try:
            datetime.strptime(date, '%d-%m-%Y')
            return date
        except ValueError:
            return ['error_message', "Неверный формат даты. Используйте формат ДД-ММ-ГГГГ."]

    @staticmethod
    def validate_category(category):
        if category.lower() not in ['доход', 'расход']:
            return ['error_message', "Неверная категория. Категория должна быть 'Доход' или 'Расход'."]
        return category

    @staticmethod
    def validate_amount(amount):
        try:
            amount = float(amount)
            if amount <= 0:
                return ['error_message', "Сумма должна быть положительной и больше нуля."]
            return amount
        except ValueError:
            return ['error_message', "Некорректное значение суммы."]

    def get_errors(self):
        errors = []
        for error in [self.date, self.category, self.amount, self.description]:
            if isinstance(error, list) and 'error_message' in error:
                errors.append(error[1])
        return errors

    @staticmethod
    def generate_id(transactions):
        if not transactions:
            return 0
        return max(transaction.transaction_id for transaction in transactions) + 1
