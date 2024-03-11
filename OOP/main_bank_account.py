from OOP.bank_account import bankAccount

account1 = bankAccount('Marica Gabriel', 'RO125215')
account2 = bankAccount('Buncea Alexandru', 'RO2515235')

account1.activateAccount(1903)
account2.activateAccount(1904)

account1.fillCard(24141)
account2.fillCard(30000)

account1.debitCard(50000)
account2.debitCard(400)

account1.description()
account2.description()