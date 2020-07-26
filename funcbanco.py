

class Funcbanco:
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    DISPLAY = "DISPLAY"
    amount = 0
    card_balance = 0
    @staticmethod
    def deposit_money(amount, card_balance):
        """Deposit given amount of money to the account."""
        card_balance += amount
        # save new balance to the database
        return card_balance

    @staticmethod
    def withdraw_money(amount, card_balance):
        """Withdraw given amount of money from the account."""
        card_balance -= amount
        # save new balance to the database
        return card_balance

    @staticmethod
    def log_transaction(action, money, card_balance):
        if action in (Funcbanco.DEPOSIT, Funcbanco.WITHDRAW):
            print(action + ": $", money)
        print("Current balance:", card_balance)

    @staticmethod
    def move_money(action, money, card_balance):
        if action == 'DEPOSIT':
            return Funcbanco.deposit_money(money, card_balance)
        elif action == 'WITHDRAW':
            return Funcbanco.withdraw_money(money, card_balance)
        elif action == 'DISPLAY':
            return card_balance

    @staticmethod
    def get_amount_of_money(action):
        if action == 'DISPLAY':
            return 0.0
        money = input("Enter the sum of money to " + action + ": ")
        return float(money)