from banco import Banco
import time


class Terminal:

    @staticmethod
    def inicio():
        func = Banco(input("Enter card number: "), input("Enter PIN: "))
        loop = True
        while loop:
            op = input('1- Realizar operação| 2- Sair:')
            if op == '1':
                if func.card_pin == func.input_pin:
                    print('1-DEPOSIT/2-WITHDRAW/3-DISPLAY')
                    op = input("Enter desired action: ")
                    action = ''
                    if op == '1':
                        action = 'DEPOSIT'
                    elif op == '2':
                        action = 'WITHDRAW'
                    elif op == '3':
                        action = 'DISPLAY'
                    func.make_transaction(action, func.card_balance)
                else:
                    print("Incorrect pin!")
            elif op == '2':
                loop = False
                print('Saindo...')
                time.sleep(0.5)