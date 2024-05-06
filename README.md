# Personal_Wallet_CLI

������:

```
    from managers.transaction_manager import TransactionManager
    from managers.file_manager import FileManager
    from models.transaction import Transaction
    
    manager = TransactionManager()
    
    transaction_id = Transaction.generate_id(manager.transactions)
    transaction = Transaction(transaction_id=transaction_id, 
                              date='01-01-2000',
                              category='�����',
                              amount=1000,
                              description='��������')
                              
    manager.add_transaction(transaction) 
    
    print(transaction)
    
    �����:
    ID: 0
    ����: 01-01-2000
    ���������: �����
    �����: 1000
    ��������: ��������
```


����������� ���� - *app.py*

��� ���������� ����, ��������� ���� json, �������� � ����
������ ����:

```
[
 {
    'transaction_id': 0,
    'date': '28-09-1999',
    'category': '������',
    'amount': 1000,
    'description': '��������'
 }
]
```
�������� **description** ����������  
�������� ��������� - '�����', '������'


class Transaction(*transaction_id: int = 0, date: str = None, category: str = None, amount: Union[float, str] = None,
                 description: str = ''*)

        :param transaction_id: ���������� ������������� ����������.
        :param date: ���� ���������� � ������� '��-��-����'.
        :param category: ��������� ���������� ('�����' ��� '������').
        :param amount: ����� ����������.
        :param description: �������� ����������.

    ������:

        --> def validate_date(date: str) -> Union[str, List[str]]
        ��������� ������ ����.

        :param date: ������ ����.
        return: ���� � ������� '��-��-����' ��� ������ [error_message, message], ���� ���� ��������� �������.


        --> def validate_category(category: str) -> Union[str, List[str]]:
        ��������� ��������� ����������.

        :param category: ��������� ����������.
        return: ��������� ���������� ��� ������ [error_message, message], ���� ��������� �������.
        

        --> def validate_amount(amount: Union[float, str]) -> Union[float, List[str]]
        ��������� � ����������� ����� ����������.

        :param amount: ����� ����������.
        return: ����� ���������� ��� ������ [error_message, message], ���� ����� �������.
        

        --> def get_errors(self) -> List[str]
        ���������� ������ ������ ������� ����������.

        :return: ������ ������ ������� ����������.


        --> def generate_id(transactions: List['Transaction']) -> int
        ���������� ���������� ������������� ��� ����� ���������� �� ������ ��������� ������ ����������.

        :param transactions: ������ ������������ ����������.
        :return: ���������� ������������� ��� ����� ����������.
        

        --> def is_valid_id(index: str, transactions: List['Transaction']) -> bool
        ���������, �������� �� ������ ���������� ��������������� ����������.

        :param index: ������ ��� ��������.
        :param transactions: ������ ������������ ����������.
        :return: True, ���� ������ ��������, ����� False.


class TransactionManager(*transactions: List[Transaction]*)

        :param transactions: ������ ������������� �������� ����������

    ������:

        --> def add_transaction(self, transaction: Transaction) -> None
        ��������� ����� ���������� � ������ ���������� � ��������� ��� � ����.

        :param transaction: ������ ���������� ��� ����������.
        :type transaction: Transaction
        :return: None
        
        
        --> def edit_transaction(self, index: int, new_transaction: Transaction) -> None
        ����������� ������������ ���������� � ������ ���������� �� ���������� ������� � ��������� ��� � ����.

        :param index: ������ ���������� ��� ��������������.
        :type index: int
        :param new_transaction: ����� ���������� ��� ������ ������������.
        :type new_transaction: Transaction
        :return: None
        

        --> def search_transactions(self, category: Optional[str] = None, date: Optional[str] = None,
                            amount: Optional[Union[float, str]] = None) -> List[Transaction]
        ����� ���������� �� �������� ���������.

        :param category: ��������� ���������� ��� ������.
        :type category: str or None
        :param date: ���� ���������� ��� ������.
        :type date: str or None
        :param amount: ����� ���������� ��� ������.
        :type amount: float or str or None
        :return: ������ ��������� ����������.
        :rtype: List[Transaction]
        

        --> def calculate_balance(self) -> Dict[str, float]
        ��������� ������ ������� � ��������.

        :return: ������� � ��������, �������� � ���������.
        :rtype: Dict[str, float]
        

        --> def get_balance(self) -> Dict[str, float]
        ���������� ������� ������.

        :return: ������� � ������� ��������, �������� � ���������.
        :rtype: Dict[str, float]
        



python app.py

��������:

����� ������� ������� ��� ����� ���������� ���� �� ���������� �������:

    1. �������� ����� ����������: ��������� �������� ����� ����������, ������ ����, ���������, ����� � ��������.
    2. ������������� ������������ ����������: ��������� ��������������� ������������ ����������, ������ � ������ � ����� ������.
    3. ����� ����������: ��������� ��������� ����� ���������� �� ���������, ���� ��� �����.
    4. ���������� ������: ���������� ������� ������.
    5. ���������� ������: ���������� ����� �����.
    6. ���������� �������: ���������� ����� �������.
    0. �����: ��������� ���������.

������ �����:

    ����: ������� ���� ���������� � ������� ��-��-����.
    ���������: ������� ��������� ���������� (�����/������).
    �����: ������� ����� ����������.
    ��������: ������� �������� ����������.