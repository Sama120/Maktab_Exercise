from datetime import datetime, timedelta
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'

# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# class_Address
class Address:
    def __init__(self, **kwargs):
        self.city = kwargs['city']
        self.alley = kwargs['alley']
        self.no = kwargs['no']
        self.pob = kwargs['pob']

    def edit_info(self, **kwargs):
        self.__dict__.update((k, v) for k, v in kwargs.items())
        return self

    def __str__(self):
        return self.__dict__
        # return f'Address: No {self.no}, {self.alley} alley, {self.city},{self.pob}'

    # def edit_address(self,dict_updated):
    #     self.city = dict_updated['city']
    #     self.alley = dict_updated['alley']
    #     self.no = dict_updated['no']
    #     self.pob = dict_updated['pob']
    #     return self

#---------------------------------------------------------------------------------------------------
# class_Person
class Person:
    def __init__(self, **kwargs):
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.address_email = kwargs['address_email']
        self.id_card = kwargs['id_card']
        self.phone_number = kwargs['phone_number']

# validate_email
    @staticmethod
    def validation_address_email(address_email):

        if re.fullmatch(regex,address_email):
            return address_email
        else:
            return "Invalid Email"

# validate_id_card
    @staticmethod
    def validation_id_card(id_card):
        if len(id_card) == 10:
            return id_card
        else:
            return "Invalid Id_card"

    def edit_info(self, **kwargs):
        self.__dict__.update((k, v) for k, v in kwargs.items())
        return self

    # def edit_info(self, dict_info):
    #     self.first_name = dict_info['first_name']
    #     self.last_name = dict_info['last_name']
    #     self.address_email = dict_info['address_email']
    #     self.id_card = dict_info['id_card']
    #     self.phone_number = dict_info['phone_number']
    #     print("Edited successfully.")
    def __str__(self):
        return f'Name:{self.first_name}{self.last_name}'


#-------------------------------------------------------------------------------------------------------------
# class store is base class.
class Store(Address, Person):
    def __init__(self, ** kwargs):
        self.owner = super(Person, self).__init__(kwargs['first_name'],kwargs['last_name'],
                                                  kwargs['address_email'],kwargs['id_card'],
                                                  kwargs['phone_number'])
        # self.owner = super(Person, self).__init__(kwargs['first_name_'],kwargs['last_name'],
        #                                           kwargs['address_email'],kwargs['id_card'],
        #                                           kwargs['phone_number'])
        self.renter = super(Person, self).__init__(kwargs['first_name'],kwargs['last_name'],
                                                   kwargs['address_email'],kwargs['id_card'],
                                                   kwargs['phone_number'])

        self.address = super(Address, self).__init__(kwargs['city'], kwargs['alley'], kwargs['no'], kwargs['pob'])

        self.area = kwargs['area']
        self.phone_number = kwargs['phone_number']
        self.status = 'enable'
        self.amount_rahn = kwargs['amount_rahn'] if kwargs['amount_rahn'] != None else None
        self.amount_rent = kwargs['amount_rent'] if kwargs['amount_rent'] != None else None
        self.amount_sell = kwargs['amount_sell'] if kwargs['amount_sell'] != None else None
        self.type_estate = kwargs['type_estate']
        # self.owner = dict_place['owner']
        # self.renter = dict_place['renter']
        # self.address = dict_place['address']
        # self.num_room = dict_place['num_room']
        # self.num_floor = dict_place['num_floor']

# edit_info_place
    def edit_info(self, **kwargs):
        self.__dict__.update((k, v) for k, v in kwargs.items())
        return self

        # def edit_info_place(self, **kwargs):
        # self.owner = kwargs['owner']
        # self.renter = kwargs['renter']
        # self.area = kwargs['area']
        # self.address = kwargs['address']
        # self.phone_number = kwargs['phone_number']
        # self.status = kwargs['status']
        # self.amount = kwargs['amount']
        # self.type_estate = kwargs['type_estate']
        # print("Edited successfully.")
    def __str__(self):
        return self.__dict__
    # def display_info_place(**kwargs):
    #     print(kwargs)

        # print(f'owner:{self.owner} renter:{self.renter} num_room:{self.num_room} area:{self.area} '
        #       f'num_floor:{self.num_floor} address:{self.address} phone_number:{self.phone_number} '
        #       f'status:{self.status} amount:{self.amount} type_estate:{self.type_estate}')

#-------------------------------------------------------------------------------------------------------------
class Apartment(Store):
    def __init__(self, floor, parking, num_floor, num_room, **kwargs):
        super(Store, self).__init__(kwargs)
        self.num_room = num_room
        self.num_floor = num_floor
        self.floor = floor
        self.parking = parking

    # def display_info_place(self):
    #     super(Place, self).display_info_place(owner=self.owner, rentre=self.renter, num_room=self.num_room,
    #                                           area=self.area, num_floor=self.num_floor, floor=self.floor,
    #                                           address=self.address,
    #                                           phone_number=self.phone_number, status=self.status, amount=self.amount,
    #                                           type_estate=self.type_estate, parking=self.parking)
    #
    # def edit_info_place(self, floor, parking, num_floor, num_room, dict_place):
    #     super(Place, self).edit_info_place(dict_place)
    #     self.num_room = num_room
    #     self.num_floor = num_floor
    #     self.floor = floor
    #     self.parking = parking
    #     print("Edited successfully")

#-------------------------------------------------------------------------------------------------------------
class House(Store):

    def __init__(self, area_yard, num_floor, num_room, **kwargs):
        super(Store, self).__init__(kwargs)
        self.num_room = num_room
        self.num_floor = num_floor
        self.area_yard = area_yard

    # def display_info_place(self):
    #     super(Place, self).display_info_place(owner=self.owner, rentre=self.renter, num_room=self.num_room,
    #                                           area=self.area, num_floor=self.num_floor, address=self.address,
    #                                           phone_number=self.phone_number, status=self.status, amount=self.amount,
    #                                           type_estate=self.type_estate, area_yard=self.area_yard)
    #
    # def edit_info_place(self, area_yard, num_floor, num_room, dict_place):
    #     super(Place, self).edit_info_place(dict_place)
    #     self.num_room = num_room
    #     self.num_floor = num_floor
    #     self.area_yard = area_yard
    #     print("Edited successfully")

#-------------------------------------------------------------------------------------------------------------
# class Store(Place):
#
#     def display_info_place(self):
#         super(Place, self).display_info_place(owner=self.owner, rentre=self.renter,
#                                               area=self.area, address=self.address,
#                                               phone_number=self.phone_number, status=self.status, amount=self.amount,
#                                               type_estate=self.type_estate)

#---------------------------------------------------------------------------------------------------------------
class RealEstate(Store):

    def search(self,dict_allinfo_place,choice):
        while True:
            self.list1 = []
            # search_by_sell
            if choice == 1:
                for i in dict_allinfo_place:
                    if i['type_estate'] == "sell":
                        self.list1.append(i)
                    # if re.search(i['type_estate'] == "sell", i):

            # search_by_rent
            elif choice == 2:
                for i in dict_allinfo_place:
                    if i['type_estate'] == "rent":
                        self.list1.append(i)

            # search_by_area
            elif choice == 3:
                vorodi1 = int(input("enter max_area:"))
                for i in dict_allinfo_place:
                    if i['area'] <= vorodi1:
                        self.list1.append(i)

                   # d = dict((k, v) for k, v in d.items() if v >= 10)
                   # box1= {k: v for (k, v) in dict_allinfo_place.items() if v > vorodi1}
                    # if re.search(['area'] <= vorodi1, dict_allinfo_place):
                    #     list1.append(i)

            # search_by_amount_rent & rahn
            elif choice == 4:
                vorodi1 = int(input("enter max_amount_rent:"))
                vorodi2 = int(input("enter max_amount_rahn:"))
                for i in dict_allinfo_place:
                    if i['amount_rent'] <= vorodi1 and i['amount_rahn'] <= vorodi2:
                        self.list1.append(i)
                # for i in dict_allinfo_place:
                #     self.list1.append(dict_allinfo_place, key=lambda i: i["mount"] < vorodi1)

                # for i in dict_allinfo_place:
                #     if re.search('amount', dict_allinfo_place):
                #         list1.append(i)
                # vorodi2 = int(input("enter max_money:"))
                # for i in list1:
                #     if re.search(['amount'] < vorodi2,dict_allinfo_place):

            # search_by_amount_sell
            elif choice == 5:
                vorodi1 = int(input("enter max_amount_sell:"))
                for i in dict_allinfo_place:
                    if i['amount_sell'] <= vorodi1:
                        self.list1.append(i)

            return self.list1
#----------------------------------------------------------------------------------------------------
#class_moamele
class Moamele(Person):

    def __init__(self,objectOfStore,**kwargs):
        self.customer = super(Person,self).__init__(kwargs['customer'])
        self.objectOfStore = objectOfStore
        self.owner = objectOfStore['owner']
        self.date_start = datetime.date.today()
        self.date_end = None


# method_rent
    def rent(self,date_end):
        self.objectOfStore.renter = self.customer
        self.date_end = date_end



    def sell(self):
        self.objectOfStore.owner = self.customer
        self.objectOfStore.renter = None



    def validation_rent_sell(self,choice_whichOne_place):
        if self.objectOfStore.type_estate == choice_whichOne_place['type_estate']:
            return True
        else:
            return False

    def disable_place(self):
        self.objectOfStore.status = 'disable'


    def __str__(self):
        return f'owner:{self.owner} buyer:{self.customer} renter:{self.objectOfStore.renter}.'



#---------------------------------------------------------------------------------------------------------



