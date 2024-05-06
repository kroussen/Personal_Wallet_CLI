# Personal_Wallet_CLI

Пример:

```
    from managers.transaction_manager import TransactionManager
    from managers.file_manager import FileManager
    from models.transaction import Transaction
    
    manager = TransactionManager()
    
    transaction_id = Transaction.generate_id(manager.transactions)
    transaction = Transaction(transaction_id=transaction_id, 
                              date='01-01-2000',
                              category='доход',
                              amount=1000,
                              description='описание')
                              
    manager.add_transaction(transaction) 
    
    print(transaction)
    
    Вывод:
    ID: 0
    Дата: 01-01-2000
    Категория: доход
    Сумма: 1000
    Описание: описание
```


Исполняемый файл - *app.py*

При исполнении кода, создается файл json, хранящий в себе
записи вида:

```
[
 {
    'transaction_id': 0,
    'date': '28-09-1999',
    'category': 'расход',
    'amount': 1000,
    'description': 'описание'
 }
]
```
Параметр **description** опционален  
Валидные категории - 'доход', 'расход'


class Transaction(*transaction_id: int = 0, date: str = None, category: str = None, amount: Union[float, str] = None,
                 description: str = ''*)

        :param transaction_id: Уникальный идентификатор транзакции.
        :param date: Дата транзакции в формате 'ДД-ММ-ГГГГ'.
        :param category: Категория транзакции ('доход' или 'расход').
        :param amount: Сумма транзакции.
        :param description: Описание транзакции.

    Методы:

        --> def validate_date(date: str) -> Union[str, List[str]]
        Проверяет строку даты.

        :param date: Строка даты.
        return: Дата в формате 'ДД-ММ-ГГГГ' или список [error_message, message], если дата неверного формата.


        --> def validate_category(category: str) -> Union[str, List[str]]:
        Проверяет категорию транзакции.

        :param category: Категория транзакции.
        return: Категория транзакции или список [error_message, message], если категория неверна.
        

        --> def validate_amount(amount: Union[float, str]) -> Union[float, List[str]]
        Проверяет и форматирует сумму транзакции.

        :param amount: Сумма транзакции.
        return: Сумма транзакции или список [error_message, message], если сумма неверна.
        

        --> def get_errors(self) -> List[str]
        Возвращает список ошибок объекта транзакции.

        :return: Список ошибок объекта транзакции.


        --> def generate_id(transactions: List['Transaction']) -> int
        Генерирует уникальный идентификатор для новой транзакции на основе последней записи транкзации.

        :param transactions: Список существующих транзакций.
        :return: Уникальный идентификатор для новой транзакции.
        

        --> def is_valid_id(index: str, transactions: List['Transaction']) -> bool
        Проверяет, является ли индекс допустимым идентификатором транзакции.

        :param index: Индекс для проверки.
        :param transactions: Список существующих транзакций.
        :return: True, если индекс допустим, иначе False.


class TransactionManager(*transactions: List[Transaction]*)

        :param transactions: Список существующикх объектов транзакций

    Методы:

        --> def add_transaction(self, transaction: Transaction) -> None
        Добавляет новую транзакцию в список транзакций и сохраняет его в файл.

        :param transaction: Объект транзакции для добавления.
        :type transaction: Transaction
        :return: None
        
        
        --> def edit_transaction(self, index: int, new_transaction: Transaction) -> None
        Редактирует существующую транзакцию в списке транзакций по указанному индексу и сохраняет его в файл.

        :param index: Индекс транзакции для редактирования.
        :type index: int
        :param new_transaction: Новая транзакция для замены существующей.
        :type new_transaction: Transaction
        :return: None
        

        --> def search_transactions(self, category: Optional[str] = None, date: Optional[str] = None,
                            amount: Optional[Union[float, str]] = None) -> List[Transaction]
        Поиск транзакций по заданным критериям.

        :param category: Категория транзакции для поиска.
        :type category: str or None
        :param date: Дата транзакции для поиска.
        :type date: str or None
        :param amount: Сумма транзакции для поиска.
        :type amount: float or str or None
        :return: Список найденных транзакций.
        :rtype: List[Transaction]
        

        --> def calculate_balance(self) -> Dict[str, float]
        Вычисляет баланс доходов и расходов.

        :return: Словарь с балансом, доходами и расходами.
        :rtype: Dict[str, float]
        

        --> def get_balance(self) -> Dict[str, float]
        Возвращает текущий баланс.

        :return: Словарь с текущим балансом, доходами и расходами.
        :rtype: Dict[str, float]
        



python app.py

Действия:

После запуска скрипта вам будет предложено меню со следующими опциями:

    1. Добавить новую транзакцию: Позволяет добавить новую транзакцию, указав дату, категорию, сумму и описание.
    2. Редактировать существующую транзакцию: Позволяет отредактировать существующую транзакцию, указав её индекс и новые данные.
    3. Поиск транзакций: Позволяет выполнять поиск транзакций по категории, дате или сумме.
    4. Посмотреть баланс: Отображает текущий баланс.
    5. Посмотреть доходы: Показывает общий доход.
    6. Посмотреть расходы: Показывает общие расходы.
    0. Выход: Завершает программу.

Формат ввода:

    Дата: Введите дату транзакции в формате ДД-ММ-ГГГГ.
    Категория: Укажите категорию транзакции (доход/расход).
    Сумма: Введите сумму транзакции.
    Описание: Укажите описание транзакции.