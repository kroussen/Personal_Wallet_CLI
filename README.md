# Personal_Wallet_CLI

Example:

```
    from managers.transaction_manager import TransactionManager
    from managers.file_manager import FileManager
    from models.transaction import Transaction
    
    manager = TransactionManager()
    
    transaction_id = Transaction.generate_id(manager.transactions)
    transaction = Transaction(transaction_id=transaction_id, 
                              date='01-01-2000',
                              category='income',
                              amount=1000,
                              description='desc')
                              
    manager.add_transaction(transaction) 
    
    print(transaction)
    
    output:
    ID: 0
    Date: 01-01-2000
    Category: income
    Amount: 1000
    Description: desc
```


Executable file - *app.py*

When the code is executed, a JSON file is created, storing entries of the following format:

```
[
 {
    'transaction_id': 0,
    'date': '28-09-1999',
    'category': 'expense',
    'amount': 1000,
    'description': 'desc'
 }
]
```
Parameter *description* is optional.
Valid categories are 'income' and 'expense'.


class Transaction(*transaction_id: int = 0, date: str = None, category: str = None, amount: Union[float, str] = None,
                 description: str = ''*)

        :param transaction_id: Unique identifier of the transaction.
:param date: Date of the transaction in the format 'DD-MM-YYYY'.
:param category: Category of the transaction ('income' or 'expense').
:param amount: Amount of the transaction.
:param description: Description of the transaction.

Methods:

    --> def validate_date(date: str) -> Union[str, List[str]]:
    Checks the date string.

    :param date: Date string.
    :return: Date in the format 'DD-MM-YYYY' or a list [error_message, message] if the date is invalid.


    --> def validate_category(category: str) -> Union[str, List[str]]:
    Checks the transaction category.

    :param category: Transaction category.
    :return: Transaction category or a list [error_message, message] if the category is invalid.
    

    --> def validate_amount(amount: Union[float, str]) -> Union[float, List[str]]:
    Validates and formats the transaction amount.

    :param amount: Transaction amount.
    :return: Transaction amount or a list [error_message, message] if the amount is invalid.
    

    --> def get_errors(self) -> List[str]:
    Returns a list of errors for the transaction object.

    :return: List of errors for the transaction object.


    --> def generate_id(transactions: List['Transaction']) -> int:
    Generates a unique identifier for a new transaction based on the last transaction record.

    :param transactions: List of existing transactions.
    :return: Unique identifier for a new transaction.
    

    --> def is_valid_id(index: str, transactions: List['Transaction']) -> bool:
    Checks if the index is a valid transaction identifier.

    :param index: Index to check.
    :param transactions: List of existing transactions.
    :return: True if the index is valid, False otherwise.


class TransactionManager(*transactions: List[Transaction]*)

       :param transactions: List of existing transaction objects.

Methods:

    --> def add_transaction(self, transaction: Transaction) -> None:
    Adds a new transaction to the list of transactions and saves it to a file.

    :param transaction: Transaction object to add.
    :type transaction: Transaction
    :return: None
    
    
    --> def edit_transaction(self, index: int, new_transaction: Transaction) -> None:
    Edits an existing transaction in the list of transactions at the specified index and saves it to a file.

    :param index: Index of the transaction to edit.
    :type index: int
    :param new_transaction: New transaction to replace the existing one.
    :type new_transaction: Transaction
    :return: None
    

    --> def search_transactions(self, category: Optional[str] = None, date: Optional[str] = None,
                        amount: Optional[Union[float, str]] = None) -> List[Transaction]:
    Searches for transactions based on specified criteria.

    :param category: Transaction category to search for.
    :type category: str or None
    :param date: Transaction date to search for.
    :type date: str or None
    :param amount: Transaction amount to search for.
    :type amount: float or str or None
    :return: List of found transactions.
    :rtype: List[Transaction]
    

    --> def calculate_balance(self) -> Dict[str, float]:
    Calculates the balance of income and expenses.

    :return: Dictionary with balance, income, and expenses.
    :rtype: Dict[str, float]
    

    --> def get_balance(self) -> Dict[str, float]:
    Returns the current balance.

    :return: Dictionary with the current balance, income, and expenses.
    :rtype: Dict[str, float]
        



python app.py

Actions:

After running the script, you will be presented with a menu with the following options:

    1. Add a new transaction: Allows you to add a new transaction by specifying the date, category, amount, and description.
    2. Edit an existing transaction: Allows you to edit an existing transaction by specifying its index and new data.
    3. Search transactions: Allows you to search for transactions by category, date, or amount.
    4. View balance: Displays the current balance.
    5. View income: Shows the total income.
    6. View expenses: Shows the total expenses.
    0. Exit: Terminates the program.

Input Format:

    Date: Enter the transaction date in the format DD-MM-YYYY.
    Category: Specify the transaction category (income/expense).
    Amount: Enter the transaction amount.
    Description: Provide a description of the transaction.