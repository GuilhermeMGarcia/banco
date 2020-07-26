class Banco:
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    DISPLAY = "DISPLAY"
    card_balance = 0
    card_pin = '123456'
    card_number = []
    input_pin = []

    def __init__(self, card_number, input_pin):
        self.card_number = card_number
        self.input_pin = input_pin
        Banco.card_number.append(self.card_number)
        Banco.input_pin.append(self.input_pin)

    @staticmethod
    def deposit_money(amount, card_balance):
        """Deposit given amount of money to the account."""
        card_balance += amount
        Banco.card_balance = card_balance
        # save new balance to the database
        return card_balance

    @staticmethod
    def withdraw_money(amount, card_balance):
        """Withdraw given amount of money from the account."""
        card_balance -= amount
        Banco.card_balance = card_balance
        # save new balance to the database
        return card_balance

    @staticmethod
    def log_transaction(action, money, card_balance):
        if action in (Banco.DEPOSIT, Banco.WITHDRAW):
            print(action + ": $", money)
        print("Current balance:", card_balance)

    @staticmethod
    def move_money(action, money, card_balance):
        if action == Banco.DEPOSIT:
            return Banco.deposit_money(money, card_balance)
        elif action == Banco.WITHDRAW:
            return Banco.withdraw_money(money, card_balance)
        elif action == Banco.DISPLAY:
            return card_balance

    @staticmethod
    def get_amount_of_money(action):
        if action == Banco.DISPLAY:
            return 0.0
        money = input("Enter the sum of money to " + action + ": ")
        return float(money)

    @staticmethod
    def make_transaction(action, card_balance):
        money = Banco.get_amount_of_money(action)
        card_balance = Banco.move_money(action, money, card_balance)
        Banco.log_transaction(action, money, card_balance)
