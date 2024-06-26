from models.transaction import Transaction
from managers.transaction_manager import TransactionManager
from managers.file_manager import FileManager

if __name__ == "__main__":
    manager = TransactionManager()

    while True:
        print("1. Добавить новую транзакцию")
        print("2. Редактировать существующую транзакцию")
        print("3. Поиск транзакций")
        print("4. Вывод баланса")
        print("5. Вывод доходов")
        print("6. Вывод расходов")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            date = input("Введите дату транзакции в формате ДД-ММ-ГГГГ: ")
            category = input("Введите категорию транзакции (доход/расход): ")
            amount = input("Введите сумму транзакции: ")
            description = input("Введите описание транзакции: ")

            transaction_id = Transaction.generate_id(manager.transactions)
            transaction = Transaction(transaction_id, date, category, amount, description)

            errors = transaction.get_errors()
            if errors:
                print(errors)
                continue

            manager.add_transaction(transaction)
            FileManager.save_transactions(manager.transactions)

            print("Транзакция добавлена успешно.")

        elif choice == "2":
            index = input("Введите индекс транзакции для редактирования: ")
            date = input("Введите новую дату транзакции в формате ДД-ММ-ГГГГ: ")
            category = input("Введите новую категорию транзакции (доход/расход): ")
            amount = input("Введите новую сумму транзакции: ")
            description = input("Введите новое описание транзакции: ")
            new_transaction = Transaction(index, date, category, amount, description)

            if not new_transaction.is_valid_id(index, manager.transactions):
                print('Транзакции с таким ID не найдено')
                continue

            errors = new_transaction.get_errors()
            if errors:
                print(errors)
                continue

            manager.edit_transaction(int(index), new_transaction)
            print("Транзакция отредактирована успешно.")

        elif choice == "3":
            category = input("Введите категорию транзакции для поиска (или оставьте пустым): ")
            date = input("Введите дату транзакции для поиска в формате ДД-ММ-ГГГГ (или оставьте пустым): ")
            amount = input("Введите сумму транзакции для поиска (или оставьте пустым): ")
            if amount:
                amount = float(amount)
            transactions = manager.search_transactions(category, date, amount)
            if transactions:
                for transaction in transactions:
                    print(transaction)
            else:
                print("Транзакции не найдены.")
        elif choice == "4":
            print(f'Баланс: {manager.get_balance()["balance"]}')
        elif choice == "5":
            print(f'Доходы: {manager.get_balance()["income"]}')
        elif choice == "6":
            print(f'Расходы: {manager.get_balance()["expense"]}')
        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
