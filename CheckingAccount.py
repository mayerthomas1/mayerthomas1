#https://github.com/Maryville-University-SWDV-630/week-2-coursework-mayerthomas2023


###from Checking_Account import Checking_Account
class CheckingAccount:


    def __init__(self, name, address, accountnumber, balance):


        self.__name = name

        self.__address = address

        self.__accountnumber = accountnumber

        self.__balance = balance


    def creditAccount(self, amount):


        self.__balance = self.__balance + amount


    def debitAccount(self, amount):


        if self.__balance < amount:

            print("Balance (${:.2f}) is too low. Operation is declined in the amount of ${:.2f}".format(
        self.__balance, amount))

        else:

            self.__balance = self.__balance - amount


    def showBalance(self):


        print("The balance of the account {} is ${:.2f}, and belongs to {}.".format(
        self.__accountnumber, self.__balance, self.__name))


###from Checking_Account import Checking_Account

account1 = CheckingAccount("Bart Simpson", "123Fake Street", 12654, 2000.10)

account1.creditAccount(11.11)

account1.debitAccount(22.22)

account1.debitAccount(33.33)

account1.showBalance()
