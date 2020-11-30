class BankAccount:
    def __init__(self, egyenleg):
        self.e = egyenleg

    def deposit(self, money):
        self.e += money
        print(self)
        # print(self.__str__())

    def withdraw(self, money):
        self.e -= money
        print(self)
        # print(self.__str__())

    def __str__(self):
        return 'Egyenlege: {} forint.'.format(self.e)


class MinBankAccount(BankAccount):
    # kezdo egyenleg, minimum korlatozas
    def __init__(self, p1, p2):
        while p2 >= p1:
            p1 = int(input('Kerek egy másik összeget: '))
        super().__init__(p1)
        self.min_value = p2

    def withdraw(self, money):
        if self.e - money < self.min_value:
            print("Nincs elég fedezete!")
        else:
            BankAccount.withdraw(self, money)


b1 = MinBankAccount(2000, 2500)
b1.deposit(200)
b1.withdraw(5000)
