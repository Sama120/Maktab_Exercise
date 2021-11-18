from datetime import datetime,timedelta
import classes
# Main

# now add info some place

def catch_info_person():
    count = 0
    if count == 0:
        print("now you should enter info owner:\n")
    else:
        print("now you should enter info renter:\n")

    person_dic = {}
    student_list = ['first_name', 'last_name', 'phone_number']
    for d in student_list:
        a = input(f'Enter your {d}:')
        person_dic.update({d: a})
    while True:
        b = input("Enter your id_card:")
        if classes.Person.validation_id_card(b) != "Invalid Email":
            person_dic.update({"id_card": a})
            break
        else:
            print("incorrect id_card!!")
    while True:
        c = input("Enter your address_email:")
        if classes.Person.validation_address_email(c) != "Invalid Email":
            person_dic.update({"address_email": c})
            break
        else:
            print("incorrect email!!")
    count += 1
    return person_dic


def catch_address_place():
    person_dic = {}
    student_list = ['city', 'alley', 'no', 'pob']
    for d in student_list:
        a = input(f'Enter your {d}:')
        person_dic.update({d: a})
    return person_dic


def catch_store_info():
    catch_store_info.area = int(input("enter area:"))
    catch_store_info.phone_number = int(input("enter phone_number:"))
    catch_store_info.type_estate = input("enter type_estate (rent or sell):")
    if catch_store_info.type_estate == 'rent':
        catch_store_info.amount_sell = None
        catch_store_info.amount_rahn = int(input("enter amount_rahn:"))
        catch_store_info.amount_rent = int(input("enter amount_rent:"))
    elif catch_store_info.type_estate == 'sell':
        catch_store_info.amount_sell = int(input("enter amount_sell:"))
        catch_store_info.amount_rahn = None
        catch_store_info.amount_rent = None

def catch_apartment_info():
    catch_apartment_info.num_room = int(input("enter num_room:"))
    catch_apartment_info.num_floor = int(input("enter num_floor:"))
    catch_apartment_info.floor = int(input("enter floor:"))
    catch_apartment_info.parking = int(input("enter parking:"))


def catch_house_info():
    catch_house_info.num_room = int(input("enter num_room:"))
    catch_house_info.num_floor = int(input("enter num_floor:"))
    catch_house_info.area_yard = int(input("enter area_yard:"))


list_store = []
list_apartment = []
list_house = []
while True:
    print("""\n1-add_Store\n12-add_Apartment\n3-add_House\n4-search\n5-done_moamele\n6-edit_info\n7-quit\n""")
    chose_menu = int(input('choose a number: '))

    if chose_menu == 1:
        catch_store_info()
        o = catch_info_person
        r = catch_info_person
        place1 = classes.Store(first_name=o["first_name"],last_name=o['last_name'],
                       address_pace=catch_address_place, area=catch_store_info.area,
                       phone_number=catch_store_info.phone_number, amount_rahn=catch_store_info.amount_rahn
                       ,amount_rent=catch_store_info.amount_rent, amount_sell=catch_store_info.amount_sell,
                       type_estate=catch_store_info.type_estate)
        list_store.append(place1)

    if chose_menu == 2:
        catch_store_info()
        catch_apartment_info()
        place1 = classes.Apartment(owner_info=catch_info_person, renter_info=catch_info_person(),
                           address_pace=catch_address_place, area=catch_store_info.area,
                           phone_number=catch_store_info.phone_number, amount_rahn=catch_store_info.amount_rahn
                           , amount_rent=catch_store_info.amount_rent, amount_sell=catch_store_info.amount_sell,
                           type_estate=catch_store_info.type_estate, floor=catch_apartment_info.floor,
                           parking=catch_apartment_info.parking, num_floor=catch_apartment_info.num_floor,
                           num_room=catch_apartment_info.num_room)

        list_apartment.append(place1)

    if chose_menu == 3:
        catch_store_info()
        catch_house_info()
        place1 = classes.House(owner_info=catch_info_person, renter_info=catch_info_person(),
                       address_pace=catch_address_place, area=catch_store_info.area,
                       phone_number=catch_store_info.phone_number, amount_rahn=catch_store_info.amount_rahn
                       , amount_rent=catch_store_info.amount_rent, amount_sell=catch_store_info.amount_sell,
                       type_estate=catch_store_info.type_estate,
                       parking=catch_house_info.parking, num_floor=catch_house_info.num_floor,
                       num_room=catch_house_info.num_room)

        list_house.append(place1)

    if chose_menu == 4:
        object_real_state = classes.RealEstate()
        print("1-search in store\n 2-search in apartment\n 3-search in house\n")
        chose_search = int(input("which one?"))

        print("1-search base sell\n 2-search base rent\n 3-search base area\n 4-search base amount_rent & rahn\n "
              "5-serach base amount_sell\n")
        chose_base = int(input("choice a number:"))

        if chose_search == 1:
            print(object_real_state.search(list_store,chose_base))

        if chose_search == 2:
            print(object_real_state.search(list_apartment, chose_base))

        if chose_search == 3:
            print(object_real_state.search(list_house, chose_base))

    if chose_menu == 5:
        type_place = input("type_place(store or apartment or house):")
        if type_place == "store":
            for i,f in enumerate(list_store):
                    f.update({"id": i})
            print(list_store)

            if type_place == "apartment":
                for i, f in enumerate(list_apartment):
                    f.update({"id": i})
                    print(list_apartment)

            if type_place == "house":
                for i, f in enumerate(list_house):
                    f.update({"id": i})
                    print(list_house)

        which_one = int(input("which one of list:"))



        num_years = int(input("enter time date_end(how many years:)"))
        date_end = datetime.date.today() + timedelta(years=date_end)
        moamele1 = classes.Moamele(list_store[which_one], customer=catch_info_person())

        chose_type_moamele = input("type moamele(rent or sell):")
        finally_validation = moamele1.validation_rent_sell(chose_type_moamele)
        if finally_validation == True and chose_type_moamele == "rent":
            moamele1.rent(date_end)
        if finally_validation == True and chose_type_moamele == "sell":
            moamele1.sell()
        else:
            print("it's invalid")
#--------------------------------------------edit------------------------------------------------
    if chose_menu == 6:
        print("1-edit address\n 2-edit info_person\n 3-edit info_store\n "
              "4-edit info_apartment\n "
              "5-edit info_house\n")
        type_edit = int(input("which one?"))
    #----------------------------------------edit_address------------------------------------
        list_edit = {}
        if type_edit == 1:
            def same_address():
                a = input("which ones you want edited: 1-city 2-alley 3-no 4-pob").split('')

                count = 0
                while True:
                    if "1" in a:
                        edited_city = input("enter city:")
                        list_edit.update(city=edited_city)
                        count +=1
                    if "2" in a:
                        edited_alley = input("enter alley:")
                        list_edit.update(alley=edited_alley)
                        count += 1
                    if "3" in a:
                        edited_no = input("enter no:")
                        list_edit.update(no=edited_no)
                        count += 1
                    if "4" in a:
                        edited_pob = input("enter pob:")
                        list_edit.update(pob=edited_pob)
                        count += 1
                    else:
                        break
                if count == 4:
                    return classes.Address.edit_info(list_edit[0],list_edit[1],list_edit[2],list_edit[3])
                if count == 3:
                    return classes.Address.edit_info(list_edit[0],list_edit[1],list_edit[2])
                if count == 2:
                    return classes.Address.edit_info(list_edit[0], list_edit[1])
                if count == 1:
                   return classes.Address.edit_info(list_edit[0])

        print("done edited!")
#----------------------------edit_2--------------------------------------------
        if type_edit == 2:
            def same():
                a = input("which ones you want edited: 1-first_name 2-last_name 3-address_email 4-id_card"
                          "5-phone_number").split('')

                count = 0
                while True:
                    if "1" in a:
                        edited_first_name = input("enter first_name:")
                        list_edit.update(first_name=edited_first_name)
                        count +=1
                    if "2" in a:
                        edited_last_name = input("enter last_name:")
                        list_edit.update(last_name=edited_last_name)
                        count += 1
                    if "3" in a:
                        edited_address_email = input("enter address_email:")
                        list_edit.update(address_email=edited_address_email)
                        count += 1
                    if "4" in a:
                        edited_id_card = input("enter id_card:")
                        list_edit.update(id_card=edited_id_card)
                        count += 1
                    if "5" in a:
                        edited_phone_number = input("enter phone_number:")
                        list_edit.update(phone_number=edited_phone_number)
                        count += 1
                    else:
                        break
                if count == 5:
                    return classes.Person.edit_info(list_edit[0],list_edit[1],list_edit[2],list_edit[3],list_edit[4])
                if count == 4:
                    return classes.Person.edit_info(list_edit[0],list_edit[1],list_edit[2],list_edit[3])
                if count == 3:
                    return classes.Person.edit_info(list_edit[0],list_edit[1],list_edit[2])
                if count == 2:
                    return classes.Person.edit_info(list_edit[0], list_edit[1])
                if count == 1:
                    return classes.Person.edit_info(list_edit[0])
        print("done edited!")
        #------------------------------------------edit info_store----------------------------------

        if type_edit == 3:

            a = input("which ones you want edited: 1-info_owner 2-info_renter 3-address"
                          "4-area 5-phone_number 6-status 7-amount_rahn 8-amount_rent"
                          "9-amount_sell 10-type_estate").split('')


            def same_store():
                same_store.count = 0
                while True:
                    if "1" in a:
                        edited_owner = same()
                        list_edit.update(owner_info=edited_owner)
                        same_store.count += 1
                    if "2" in a:
                        edited_renter = same()
                        list_edit.update(renter_info=edited_renter)
                        same_store.count += 1
                    if "3" in a:
                        edited_address = input("enter address:")
                        list_edit.update(address=edited_address)
                        same_store.count += 1
                    if "4" in a:
                        edited_area = input("enter area:")
                        list_edit.update(area=edited_area)
                        same_store.count += 1
                    if "5" in a:
                        edited_phone_number = input("enter phone_number:")
                        list_edit.update(phone_number=edited_phone_number)
                        same_store.count += 1
                    if "6" in a:
                        edited_status = input("enter status:")
                        list_edit.update(status=edited_status)
                        same_store.count += 1
                    if "7" in a:
                        edited_amount_rahn = input("enter amount_rahn:")
                        list_edit.update(amount_rahn=edited_amount_rahn)
                        same_store.count += 1
                    if "8" in a:
                        edited_amount_rent = input("enter amount_rent:")
                        list_edit.update(amount_rent=edited_amount_rent)
                        same_store.count += 1
                    if "9" in a:
                        edited_amount_sell = input("enter amount_sell:")
                        list_edit.update(amount_sell=edited_amount_sell)
                        same_store.count += 1
                    if "10" in a:
                        edited_type_estate = input("enter type_estate:")
                        list_edit.update(type_estate=edited_type_estate)
                        same_store.count += 1
                    else:
                        break


            same_store()
            if same_store.count == 10:
                classes.Store.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4],
                                          list_edit[5], list_edit[6], list_edit[7], list_edit[8], list_edit[9])
            if same_store.count == 9:
                classes.Store.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4],
                                          list_edit[5], list_edit[6], list_edit[7], list_edit[8])
            if same_store.count == 8:
                classes.Store.edit_info(list_edit[0], list_edit[1], list_edit[2],list_edit[3], list_edit[4],
                                          list_edit[5], list_edit[6], list_edit[7])
            if same_store.count == 7:
                classes.Store.edit_info(list_edit[0], list_edit[1],list_edit[3], list_edit[4],
                                          list_edit[5], list_edit[6])
            if same_store.count == 6:
                classes.Store.edit_info(list_edit[0], list_edit[1],list_edit[3], list_edit[4],
                                          list_edit[5])
            if same_store.count == 5:
                classes.Store.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4])
            if same_store.count == 4:
                classes.Store.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3])
            if same_store.count == 3:
                classes.Store.edit_info(list_edit[0], list_edit[1], list_edit[2])
            if same_store.count == 2:
                classes.Store.edit_info(list_edit[0], list_edit[1])
            if same_store.count == 1:
                classes.Store.edit_info(list_edit[0])
        print("done edited!")
        # ------------------------------------------edit info_apartment----------------------------------

        if type_edit == 4:
            a = input("which ones you want edited: 1-info_owner 2-info_renter 3-address"
                      "4-area 5-phone_number 6-status 7-amount_rahn 8-amount_rent"
                      "9-amount_sell 10-type_estate 11-num_room 12-num_floor 13-floor "
                      "14-parking").split('')
            same_store()
            count = same_store.count
            while True:
                if "11" in a:
                    edited_num_room = input("enter num_room:")
                    list_edit.update(num_room=edited_num_room)
                    count += 1
                if "12" in a:
                    edited_num_floor = input("enter num_floor:")
                    list_edit.update(num_floor=edited_num_floor)
                    count += 1
                if "13" in a:
                    edited_floor = input("enter floor:")
                    list_edit.update(floor=edited_floor)
                    count += 1
                if "14" in a:
                    edited_parking = input("enter parking:")
                    list_edit.update(parking=edited_parking)
                    count += 1

                else:
                    break
            if count == 14:
                classes.Apartment.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6], list_edit[7], list_edit[8], list_edit[9]
                                        , list_edit[10], list_edit[11], list_edit[12], list_edit[13])
            if count == 13:
                classes.Apartment.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6], list_edit[7], list_edit[8]
                                        , list_edit[9], list_edit[10], list_edit[11], list_edit[12])
            if count == 12:
                classes.Apartment.edit_info(list_edit[0], list_edit[1], list_edit[2],list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6], list_edit[7]
                                        , list_edit[8], list_edit[9], list_edit[10], list_edit[11])
            if count == 11:
                classes.Apartment.edit_info(list_edit[0], list_edit[1], list_edit[2],list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6], list_edit[7], list_edit[8],
                                        list_edit[9], list_edit[10])
            if count == 10:
                classes.Apartment.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6], list_edit[7], list_edit[8], list_edit[9])
            if count == 9:
                classes.Apartment.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6], list_edit[7], list_edit[8])
            if count == 8:
                classes.Apartment.edit_info(list_edit[0], list_edit[1], list_edit[2],list_edit[3], list_edit[4],
                                            list_edit[5], list_edit[6], list_edit[7])
            if count == 7:
                classes.Apartment.edit_info(list_edit[0], list_edit[1],list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6])
            if count == 6:
                classes.Apartment.edit_info(list_edit[0], list_edit[1],list_edit[3], list_edit[4],
                                            list_edit[5])
            if count == 5:
                classes.Apartment.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4])
            if count == 4:
                classes.Apartment.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3])
            if count == 3:
                classes.Apartment.edit_info(list_edit[0], list_edit[1], list_edit[2])
            if count == 2:
                classes.Apartment.edit_info(list_edit[0], list_edit[1])
            if count == 1:
                classes.Apartment.edit_info(list_edit[0])
        print("done edited!")
        #---------------------------------------------------edit_house------------------------------
        if type_edit == 5:
            a = input("which ones you want edited: 1-info_owner 2-info_renter 3-address"
                      "4-area 5-phone_number 6-status 7-amount_rahn 8-amount_rent"
                      "9-amount_sell 10-type_estate 11-num_room 12-num_floor 13-yard ").split('')
            same_store()
            count = same_store.count
            while True:
                if "11" in a:
                    edited_num_room = input("enter num_room:")
                    list_edit.update(num_room=edited_num_room)
                    count += 1
                if "12" in a:
                    edited_num_floor = input("enter num_floor:")
                    list_edit.update(num_floor=edited_num_floor)
                    count += 1
                if "13" in a:
                    edited_yard = input("enter yard:")
                    list_edit.update(yard=edited_yard)
                    count += 1
                else:
                    break

            if count == 13:
                classes.House.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6], list_edit[7], list_edit[8]
                                        , list_edit[9], list_edit[10], list_edit[11], list_edit[12])
            if count == 12:
                classes.House.edit_info(list_edit[0], list_edit[1], list_edit[2],list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6], list_edit[7]
                                        , list_edit[8], list_edit[9], list_edit[10], list_edit[11])
            if count == 11:
                classes.House.edit_info(list_edit[0], list_edit[1], list_edit[2],list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6], list_edit[7], list_edit[8],
                                        list_edit[9], list_edit[10])
            if count == 10:
                classes.House.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6], list_edit[7], list_edit[8], list_edit[9])
            if count == 9:
                classes.House.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6], list_edit[7], list_edit[8])
            if count == 8:
                classes.House.edit_info(list_edit[0], list_edit[1], list_edit[2],list_edit[3], list_edit[4],
                                            list_edit[5], list_edit[6], list_edit[7])
            if count == 7:
                classes.House.edit_info(list_edit[0], list_edit[1],list_edit[3], list_edit[4],
                                        list_edit[5], list_edit[6])
            if count == 6:
                classes.House.edit_info(list_edit[0], list_edit[1],list_edit[3], list_edit[4],
                                            list_edit[5])
            if count == 5:
                classes.House.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3], list_edit[4])
            if count == 4:
                classes.House.edit_info(list_edit[0], list_edit[1], list_edit[2], list_edit[3])
            if count == 3:
                classes.House.edit_info(list_edit[0], list_edit[1], list_edit[2])
            if count == 2:
                classes.House.edit_info(list_edit[0], list_edit[1])
            if count == 1:
                classes.House.edit_info(list_edit[0])
        print("done edited!")

    if chose_menu == 7:
        break
