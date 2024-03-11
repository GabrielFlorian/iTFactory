class bankAccount:

    # consctructor
    def __init__(self, accountOwner, IBAN):
        self.accountOwner = accountOwner
        self.IBAN = IBAN
        self.sold = 0
        self.active = False
        self.PIN = 1904
        self.pinAttempts = 0

    def description(self):
        print(f'Account owner: {self.accountOwner}')
        print(f'IBAN: {self.IBAN}')
        print(f'Sold: {self.sold}')
        print(f'Active: {self.active}')
        print(f'PIN attempts: {self.pinAttempts}')
        print('-------------------')

    def activateAccount(self, userPIN):
        print(f'Hello {self.accountOwner}')
        if userPIN == self.PIN:
            print('Card successfully activated!')
            self.active = False
        else:
            print('Incorrect PIN!')
            self.pinAttempts = self.pinAttempts + 1

    def fillCard(self, ammount):
        self.sold += ammount
        print(f'You have deposited {ammount}')
        print(f'Current sold {self.sold}')

    def debitCard(self, ammount):
        if ammount <= self.sold:
            self.sold -= ammount
            print(f'You have spent {self.accountOwner}')
            print(f'Current sold {self.sold}')
        else:
            print('Insufficient funds!')




