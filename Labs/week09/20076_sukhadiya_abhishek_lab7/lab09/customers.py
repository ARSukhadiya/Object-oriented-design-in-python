class Customer:
    def __init__(self, account_no: str, lastname: str, firstname: str, account_balance: float) -> None:
        self.__account_no = account_no
        self.__lastname = lastname
        self.__firstname = firstname
        self.__account_balance = account_balance

    @property
    def account_no(self) -> int:
        return self.__account_no
    
    @property
    def account_balance(self) -> float:
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, acc_bal) -> None:
        self.__account_balance = acc_bal

    @property
    def lastname(self) -> str:
        return self.__lastname

    @property
    def name(self) -> str:
        return self.__firstname + " " + self.__lastname

    def __str__(self) -> str:        
        return f"{self.__account_no}\t\t\t{self.__lastname}\t\t\t{self.__firstname}\t\t\t{self.__account_balance}"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __value: object) -> bool:
        pass

    def convert_to_list(self) -> list[str]:
        lst = []
        lst.append(self.__account_no)
        lst.append(self.__lastname)
        lst.append(self.__firstname)
        lst.append(self.__account_balance)
        return lst

  