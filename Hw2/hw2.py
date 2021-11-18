import time
from datetime import datetime

    # class parent_card
class Card:
    def __init__(self):
        self.wallet = 0

        # calculate count travel that you can go
    def count_travel(self):
        count = self.wallet / 500
        print(f'with this wallet you can go {count} travel. ')

    def __repr__(self):
        return f'wallet:{self.wallet}'


    # class_child_single_travel
class Single_Travel(Card):

    def charge(self):
        self.wallet += 500

    # method deduction_operation
    def deduction_operation(self):
        if self.wallet == 500:
            self.wallet = 0
            print(f'Done! wallet:{self.wallet}')
        else:
            print(f'oops!you used once, wallet:{self.wallet}')

    # class child_credit
class Credit(Card):

    # method_charge
    def charge(self):
        while True:
            value_wallet = int(input("How many do you want to charge(min:500)? "))
            if value_wallet >= 500:
                self.wallet += value_wallet
                break
            else:
                print('you must at least charge 500!')
        print(f'your wallet  successfully charged! wallet:{self.wallet}')

    # method_deduction_operation
    def deduction_operation(self):
        if self.wallet >= 500:
            self.wallet -= 500
            print(self.wallet)
        else:
            print(f"your cash isn't enough, please charge your wallet. wallet:{self.wallet}")

    # class Credit_Time
class Credit_Time(Card):

    def __init__(self):
        super().__init__()
        self.expiration_date = 0
        #self.current_datetime = datetime.now()
        #self.current_datetime = datetime.today() - timedelta(days=1)
        self.current_datetime = datetime(2021, 10, 23, 0, 0)

    # method_charge
    def charge(self):

        # charge_wallet
        while True:
            value_wallet = int(input("How many do you want to charge(min:500)? "))
            if value_wallet >= 500:
                self.wallet += value_wallet
                break
            else:
                print('you must at least charge 500!')

        # check_datetime
        if value_wallet < 5000:
            self.expiration_date = self.current_datetime + timedelta(days=9)
            self.second_expiration = self.expiration_date.timestamp()
        elif value_wallet < 15000:
            self.expiration_date = self.current_datetime + timedelta(days=19)
            self.second_expiration = self.expiration_date.timestamp()
        else:
            self.expiration_date = self.current_datetime + timedelta(days=29)
            self.second_expiration = self.expiration_date.timestamp()
        print(f'your wallet  successfully charged! wallet:{self.wallet} until {self.expiration_date} is valid.,\n')

    # method_deduction_operation
    def deduction_operation(self):
        today_date = time.time()
        #self.second_now = time.time()
        # self.second_now = time.mktime(self.current_datetime.timetuple())

        check1 = bool(self.wallet >= 500)
        check2 = bool(self.second_expiration - today_date >= 0)

        if check1 is True and check2 is True:
            self.wallet -= 500
            print(f'operation is successfully. {self.wallet}')
        else:
            if check1 is False and check2 is True:
                print(f"your cash isn't enough, please charge your wallet. wallet:{self.wallet},\n")
            elif check1 is True and check2 is False:
                print(f'you have {self.wallet} cash but your deadline has expired!{self.expiration_date},\n')
            else:
                print(f"Error for both!! wallet:{self.wallet} ,deadline:{self.expiration_date} ,\n")

    def count_travel(self):
        count = self.wallet / 500
        print(f'with this wallet you can go {count} travel until {self.expiration_date}.,\n')

    def __repr__(self):
        return f'wallet:{self.wallet}, deadline:{self.expiration_date}'

# senario_1
card1 = Single_Travel()
card1.charge()
card1.deduction_operation()
card1.deduction_operation()

# senario_2
card2 = Credit_Time()
card2.charge()
card2.deduction_operation()

# senario_3
card3 = Credit()
print(card3)
card3.charge()
