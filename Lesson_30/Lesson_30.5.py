class Bank:
    def __init__(self,balance1, balance, _deposit, _withdraw):
        self.balance = balance
        self._deposit = _deposit
        self._withdraw = _withdraw
        self.balance1 = balance1
    def check_balance(self, balance1, balance, _deposit):
        balance1 = self.balance + self._deposit
        print(f'Your balance: {self.balance1}')
    def deposit(self, _deposit):
        print(f'You deposit to account: {self._deposit}')
    def withdraw(self, _withdraw, __balance):
        if __balance<_withdraw:
            print('You have not enought money!')
        else:
            print(f'You withdraw from bank: {self._withdraw}')
    def check_balance1(self, balance1, _withdraw):
        balance1 +=  _withdraw
        print(f'Your balance: {self.balance1}')
n = int(input('How much you want to deposit?: '))
m = int(input('How much you want to withdraw?: '))
balance = 0
balance1 = balance + n
account = Bank(balance1, balance, n, m)
account.deposit(n)
account.check_balance(balance1, balance, n)
account.withdraw(m, balance1)
account.check_balance1(balance1, m)
        