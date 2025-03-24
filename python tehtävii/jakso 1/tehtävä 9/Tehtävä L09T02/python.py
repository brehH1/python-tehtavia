class Account:
    def __init__(self, initial_balance: float = 0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._balance = initial_balance
    
    @property
    def balance(self) -> float:
        return self._balance
    
    def add(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Amount to add cannot be negative.")
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Amount to withdraw cannot be negative.")
        if amount > self._balance:
            raise ValueError(f"Sorry, you have only {self._balance}€, the withdrawal cannot be completed.")
        self._balance -= amount
        return self._balance


def create_account(initial_balance: float = 0) -> Account:
    return Account(initial_balance)


def handle_add(account: Account) -> None:
    try:
        amount = float(input("How many euros will be added? "))
        account.add(amount)
    except ValueError as e:
        print(f"Error: {e}")


def handle_withdraw(account: Account) -> None:
    try:
        amount = float(input("How many euros will be withdrawn? "))
        account.withdraw(amount)
    except ValueError as e:
        print(f"Error: {e}")


def main():
    account = create_account(2000)
    print("Bank account created.")
    print(f"Bank account balance: {account.balance}€")
    
    handle_add(account)
    print(f"Bank account balance: {account.balance}€")
    
    handle_withdraw(account)
    print(f"Bank account balance: {account.balance}€")
    
    handle_withdraw(account)


if __name__ == "__main__":
    main()