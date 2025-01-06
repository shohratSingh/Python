fprice=2000
bfprice=5000
a1price=10000

hprice=1000
vhprice=2000

tprice=500
actprice=1000

nbus=500
n2bus=800
acsbus=700
acs2bus=1050
acsebus=900
acse2bus=1250

rcab=10
rdcab=8
lcab=16
dlcab=14

laundary=100
import time


print("\t\tMakeMyTrip\t\t\t\t\t\t")

users={'SSR':1234}

print("Welcome to MakeMyTrip's login page :D")
username=input("\nEnter your Username: ")
password=input("Enter your Password:")

if username in users and users[username] == int(password):
    print("Login successful! Redirecting to booking options...")
    time.sleep(2)
    print("\n1.Flights\t2.Hotels\t3.Trains\t4.Buses\t\t5.Cabs")


    option=int(input("\nSelect from the options you want to book.(enter in numeric only): "))

    if option==1:
        print("\nWelcome to our Flight booking portal.")
        flight_type=int(input("\nSelect which type of flight you want?\n\n1.Normal Flight\t\t2.Business Class\t3.A1-class Flight\n "))

        if flight_type==1:
            print("\n1.One Way\t2.Two-Way Trip\t3.Multi-City")
            flight=int(input("\nWhich type of flight you are willing for?(enter you choice in numeric only): "))

            if flight==1:
                print("\n\t\tWelcome to your One-Way trip booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                print(f"\nPaid Amount: {family_count*fprice}")
                print("\n\tCongrats on your Random Location trip booking :) ")

            elif flight==2:
                print("\n\t\tWelcome to your Two-Way trip booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                print(f"\nPaid Amount: {family_count*fprice*2}")
                print("\n\tCongrats on your Random Location for two way trip booking :) ")

            elif flight==3:
                print("\n\t\tWelcome to your Multi-City trip booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                city_count=int(input("\nKindly select how many cities you want to go."))
                print(f"\nPaid Amount: {family_count*fprice*city_count}")
                print("\n\tCongrats on your Random Multi-city trip booking :) ")

            else:
                print("\ninvalid options selected")

        elif flight_type==2:

            print("\n1.One Way\t2.Two-Way Trip\t3.Multi-City")
            flight=int(input("\nWhich type of flight you are willing for?(enter you choice in numeric only): "))
            if flight==1:
                print("\n\t\tWelcome to your One-Way trip booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                print(f"\nPaid Amount: {family_count*bfprice}")
                print("\n\tCongrats on your Random Location trip booking :) ")

            elif flight==2:
                print("\n\t\tWelcome to your Two-Way trip booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                print(f"\nPaid Amount: {family_count*bfprice*2}")
                print("\n\tCongrats on your Random Location for two way trip booking :) ")

            elif flight==3:
                print("\n\t\tWelcome to your Multi-City trip booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                city_count=int(input("\nKindly select how many cities you want to go."))
                print(f"\nPaid Amount: {family_count*bfprice*city_count}")
                print("\n\tCongrats on your Random Multi-city trip booking :) ")

            else:
                print("\ninvalid options selected")
        elif flight_type==3:
            print("\n1.One Way\t2.Two-Way Trip\t3.Multi-City")
            flight=int(input("\nWhich type of flight you are willing for?(enter you choice in numeric only): "))

            if flight==1:
                print("\n\t\tWelcome to your One-Way trip booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                print(f"\nPaid Amount: {family_count*a1price}")
                print("\n\tCongrats on your Random Location trip booking :) ")

            elif flight==2:
                print("\n\t\tWelcome to your Two-Way trip booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                print(f"\nPaid Amount: {family_count*a1price*2}")
                print("\n\tCongrats on your Random Location for two way trip booking :) ")

            elif flight==3:
                print("\n\t\tWelcome to your Multi-City trip booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                city_count=int(input("\nKindly select how many cities you want to go."))
                print(f"\nPaid Amount: {family_count*a1price*city_count}")
                print("\n\tCongrats on your Random Multi-city trip booking :) ")

            else:
                print("\ninvalid options selected")

        else:
            print("invalid selected option")

    elif option==2:
        print("\nWelcome to our Hotel booking services")
        htype=int(input("\nWhich type of Room do you want?(enter in numeric only)\n\n1.Non-AC Rooms 2.AC Rooms\n\n" ))

        if htype==1:
            print("\n1.One-Room\t2.Two-Rooms\t3.Multi-Room")
            hotel=int(input("\nWhich type of Room do you want?(enter your choice in numeric only):  "))

            if hotel==1:
                print("\nWelcome to Non-AC One-Room booking services")
                fcount=int(input("\nEnter the total no. of members for booking(numeric only):  "))
                daycount=int(input("\nEnter numbers of days for booking:(enter in numeric only)  "))
                meal=int(input("\nDo you want to add meal in you stay?\n\n1.Yes \t2No\n\n"))

                if meal==1:
                    food=int(input("\nWhich type of meal do yo want?\n\n1.Veg\t2.Non-Veg\n"))

                    if food==1:
                        print("\nThe Veg Meal price will be added in you booking i.e Rupees 250/person")
                        print(f"\nPayable amount: {(daycount*hprice)+(250*fcount*daycount)}")

                    else:
                        print("\nThe Non-Veg meal price will be added in you booking price i.e. 500/person")
                        print(f"\nPayable amount: {(daycount*hprice)+(500*fcount*daycount)}")

                else:
                    print("\nNo Issue!")
                    print(f"\nPayable amount: {daycount*hprice}")

                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the stay")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the stay!")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")

            elif hotel==2:
                print("\nWelcome to Non-AC Two-Room booking services")
                f2count=int(input("\nEnter the total no. of members for booking(numeric only):  "))
                day2count=int(input("\nEnter numbers of days for booking:(enter in numeric only)  "))
                meal2=int(input("\nDo you want to add meal in you stay?\n\n1.Yes \t2No\n\n"))

                if meal2==1:

                    food=int(input("\nWhich type of meal do yo want?\n\n1.Veg\t2.Non-Veg\n"))

                    if food==1:
                        print("\nThe Veg Meal price will be added in you booking i.e Rupees 250/person")
                        print(f"\nPayable amount: {(day2count*(hprice*2))+(250*f2count*day2count)}")

                    else:
                        print("\nThe Non-Veg meal price will be added in you booking price i.e. 500/person")
                        print(f"\nPayable amount: {(day2count*(hprice*2))+(500*f2count*day2count)}")

                else:
                    print("\nNo Issue!")
                    print(f"\nPayable amount: {day2count*(hprice*2)}")

                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the stay!")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the stay")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")



            elif hotel==3:
                print("\nWelcome to Non-AC Multi-Room booking services")
                rcount=int(input("\nEnter how many room do you want?(enter in numeric only):  "))
                f3count=int(input("\nEnter the total no. of members for booking(numeric only):  "))
                day3count=int(input("\nEnter numbers of days for booking:(enter in numeric only)  "))
                meal3=int(input("\nDo you want to add meal in you stay?\n\n1.Yes \t2No\n\n"))

                if meal3==1:
                    food=int(input("\nWhich type of meal do yo want?\n\n1.Veg\t2.Non-Veg\n"))

                    if food==1:
                        print("\nThe Veg Meal price will be added in you booking i.e Rupees 250/person")
                        print(f"\nPayable amount: {(day3count*(hprice*rcount))+(250*f3count*day3count)}")

                    else:
                        print("\nThe Non-Veg meal price will be added in you booking price i.e. 500/person")
                        print(f"\nPayable amount: {(day3count*(hprice*rcount))+500}")

                else:
                    print("\nNo Issue! Enjoy the stay!")
                    print(f"\nPayable amount: {day3count*(hprice*rcount)}")
                
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the stay")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the stay!")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")


        elif htype==2:

            print("\n1.One-Room\t2.Two-Rooms\t3.Multi-Room")
            hotel2=int(input("\nWhich type of Room do you want?(enter your choice in numeric only):  "))

            if hotel2==1:
                print("\nWelcome to AC One-Room booking services")
                fcount=int(input("\nEnter the total no. of members for booking(numeric only):  "))
                daycount=int(input("\nEnter numbers of days for booking:(enter in numeric only)  "))
                laundry=int(input("\nDo you want Laundry? For Rupees 100 (enter in numeric only)\n1.Yes\t2.No\n"))

                if laundry==1:
                    print("\nThank You for using our service.")
                else:
                    print("No Problem")

                meal=int(input("\nDo you want to add meal in you stay?\n\n1.Yes \t2No\n"))

                if meal==1:
                    food=int(input("\nWhich type of meal do yo want?\n\n1.Veg\t2.Non-Veg\n\n"))

                    if food==1:
                        print("\nThe Veg Meal price will be added in you booking i.e Rupees 250/person")
                        print(f"\nPayable amount: {(daycount*vhprice)+(250*fcount*daycount)+laundary}")
                    else:
                        print("\nThe Non-Veg meal price will be added in you booking price i.e. 500/person")
                        print(f"\nPayable amount: {(daycount*vhprice)+(500*fcount*daycount)+laundary}")

                else:
                    print("\nNo Issue!")
                    print(f"\nPayable amount: {(daycount*vhprice)}")

                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the stay")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the stay!")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")

            elif hotel2==2:

                print("\nWelcome to AC Two-Room booking services")
                fcount=int(input("\nEnter the total no. of members for booking(numeric only):  "))
                daycount=int(input("\nEnter numbers of days for booking:(enter in numeric only)  "))
                laundry=int(input("\nDo you want Laundry? For Rupees 100 (enter in numeric only)\n1.Yes\t2.No\n"))

                if laundry==1:
                    print("\nThank You for using our service.")
                else:
                    print("No Problem")

                meal=int(input("\nDo you want to add meal in you stay?\n\n1.Yes \t2No\n"))

                if meal==1:
                    food=int(input("\nWhich type of meal do yo want?\n\n1.Veg\t2.Non-Veg\n\n"))

                    if food==1:
                        print("\nThe Veg Meal price will be added in you booking i.e Rupees 250/person")
                        print(f"\nPayable amount: {(daycount*(vhprice*2))+(250*fcount*daycount)+laundary}")
                    else:
                        print("\nThe Non-Veg meal price will be added in you booking price i.e. 500/person")
                        print(f"\nPayable amount: {(daycount*(vhprice*2))+(500*fcount*daycount)+laundary}")

                else:
                    print("\nNo Issue!")
                    print(f"\nPayable amount: {(daycount*(vhprice*2))}")

                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the stay!")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")

            elif hotel2==3:

                print("\nWelcome to AC Multi-Room booking services")
                rcount=int(input("\nEnter how many room do you want?(enter in numeric only):  "))
                fcount=int(input("\nEnter the total no. of members for booking(numeric only):  "))
                daycount=int(input("\nEnter numbers of days for booking:(enter in numeric only)  "))
                laundry=int(input("\nDo you want Laundry? For Rupees 100 (enter in numeric only)\n1.Yes\t2.No\n"))

                if laundry==1:
                    print("\nThank You for using our service.")
                else:
                    print("No Problem")

                meal=int(input("\nDo you want to add meal in you stay?\n\n1.Yes \t2No\n"))

                if meal==1:
                    food=int(input("\nWhich type of meal do yo want?\n\n1.Veg\t2.Non-Veg\n\n"))

                    if food==1:
                        print("\nThe Veg Meal price will be added in you booking i.e Rupees 250/person")
                        print(f"\nPayable amount: {(daycount*(vhprice*rcount))+(250*fcount*daycount)+laundary}")
                    else:
                        print("\nThe Non-Veg meal price will be added in you booking price i.e. 500/person")
                        print(f"\nPayable amount: {(daycount*(vhprice*rcount))+(500*fcount*daycount)+laundary}")

                else:
                    print("\nNo Issue!")
                    print(f"\nPayable amount: {(daycount*(vhprice*rcount))}")

                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjot the stay")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the stay!")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")

        else:
            print("invalid option selected")


    elif option==3:

        print("\nWelcome to Indian Railways")
        train_type=int(input("\nSelect which type of train you want to book.\n\n1.Sleeper\t2.AC \n"))
        if train_type==1:
            route=int(input("Select which type of train you want?\n1.One Way\t2.Two-Way Trip\n"))
            
            if route==1:
                print("\nWelcome to your One-Way Non-AC train booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                print(f"\nPayable Amount: {family_count*tprice}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            
            elif route==2:
                print("\nWelcome to your Two-Way Non-AC train booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                print(f"\nPayable Amount: {family_count*tprice*2}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjot the ride")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            else:
                print("Invalid selection")
        
        elif train_type==2:
            route=int(input("Select which type of train you want?\n1.One Way\t2.Two-Way Trip\n"))
            
            if route==1:
                print("\nWelcome to your One-Way ac train booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                print(f"\nPayable Amount: {family_count*actprice}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the ride")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            
            elif route==2:
                print("\nWelcome to your Two-Way AC train booking :) ")
                family_count=int(input("\nEnter the total no. of members for booking(numeric only): "))
                print(f"\nPayable Amount: {family_count*actprice*2}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the ride")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            else:
                print("Invalid selection")
        else:
            print("Invalid Selection")

    elif option==4:
        print("\nWelcome to our Bus booking services")
        bus_type=int(input("\nWhich type of Bus do you want?(enter in numeric only)\n\n1.Non-AC Bus\t2.AC Bus\n\n" ))
        
        if bus_type==1:
            print("Welcome to Uttar Pradesh Non-AC Bus service")
            seat_count=int(input("How many Seats do you want?(enter in numeric value): "))
            board=(input("From: "))
            drop=(input("Destination: "))
            distance=int(input("Estimated distance between boarding and destination (numeric only): "))

            if distance<=200:
                print(f"\nPayable Amount: {( seat_count*nbus)}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the ride")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")

                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            
            elif distance>200:
                print(f"\nPayable Amount: {( seat_count*n2bus)}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))

                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))

                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the ride")
                        else:
                            print("Incorrcet information, transection failed!")

                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")
                                
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            else:
                print("Invalid input!")

        elif bus_type==2:
            print("Welcome to Uttar Pradesh AC Bus service")
            seat_type=int(input("Which type of seat you want?(enter in numeric)\n1.Seater\t2.Sleeper\n"))

            if seat_type==1:
                seat_count=int(input("How many Seats do you want?(enter in numeric value): "))
                board=(input("From: "))
                drop=(input("Destination: "))
                distance=int(input("Estimated distance between boarding and destination (numeric only): "))

                if distance<=200:
                    print(f"\nPayable Amount: {( seat_count*acsbus)}")
                    payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                
                    if payment_method == 1:
                        upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                        if upi.isdigit() and len(upi) == 10:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Invalid UPI,transection failed")

                    elif payment_method == 2:
                        card =(input("Enter your last 6 digit of card: "))
                        if card.isdigit() and len(card) == 6:
                            cvv = (input("Enter you 3 digit CVV number: "))
                            if cvv.isdigit() and len(cvv) == 3:
                                confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                                if confirm_detail==1:
                                    time.sleep(2)
                                    print("Your Payment is Sucessfull, Enjoy the ride")
                                else:
                                    print("Incorrcet information, transection failed!")
                            else:
                                print("Wrong CVV number, transection failed! ")
                        else:
                            print("Card details are incorrect, transection failed!")
                    else:
                        print("Invalid input!")
            
                elif distance>200:
                    print(f"\nPayable Amount: {( seat_count*acs2bus)}")
                    payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                
                    if payment_method == 1:
                        upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                        if upi.isdigit() and len(upi) == 10:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Invalid UPI,transection failed")
                        
                    elif payment_method == 2:
                        card =(input("Enter your last 6 digit of card: "))
                        if card.isdigit() and len(card) == 6:
                            cvv = (input("Enter you 3 digit CVV number: "))
                            if cvv.isdigit() and len(cvv) == 3:
                                confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                                if confirm_detail==1:
                                    time.sleep(2)
                                    print("Your Payment is Sucessfull, Enjoy the ride")
                                else:
                                    print("Incorrcet information, transection failed!")
                            else:
                                print("Wrong CVV number, transection failed! ")
                        else:
                            print("Card details are incorrect, transection failed!")
                    else:
                        print("Invalid input!")
                else:
                    print("Invalid input!")
        

            if seat_type==2:
                seat_count=int(input("How many Seats do you want?(enter in numeric value): "))
                board=(input("From: "))
                drop=(input("Destination: "))
                distance=int(input("Estimated distance between boarding and destination (numeric only): "))

            if distance<=200:
                print(f"\nPayable Amount: {( seat_count*acsebus)}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the ride")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            
            elif distance>200:
                print(f"\nPayable Amount: {( seat_count*acse2bus)}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the ride")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")
                        
                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))
                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            else:
                print("Invalid input!")
        
        else:
            print("Invalid input!")

    elif option==5:
        print("\nWelcome to our Cab booking services")
        cab_type=int(input("\nWhich type of Cab do you want?(enter in numeric only)\n\n1.Regular Cab\t2.Luxury Cab\n\n" ))
        
        if cab_type==1:
            seat_count=int(input("How many Seats do you want?(enter in numeric value): "))
            board=(input("From: "))
            drop=(input("Destination: "))
            distance=int(input("Estimated distance between boarding and destination (numeric only): "))

            if distance<=200:
                print(f"\nPayable Amount: {( seat_count*rcab*distance)}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the ride")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")

                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            
            elif distance>200:
                print(f"\nPayable Amount: {( seat_count*rdcab*distance)}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))

                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))

                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the ride")
                        else:
                            print("Incorrcet information, transection failed!")

                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")
                                
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            else:
                print("Invalid input!")

        elif cab_type==2:
            seat_count=int(input("How many Seats do you want?(enter in numeric value): "))
            board=(input("From: "))
            drop=(input("Destination: "))
            distance=int(input("Estimated distance between boarding and destination (numeric only): "))

            if distance<=200:
                print(f"\nPayable Amount: {( seat_count*lcab*distance)}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))
                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))
                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the ride")
                        else:
                            print("Incorrcet information, transection failed!")
                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")

                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            
            elif distance>200:
                print(f"\nPayable Amount: {( seat_count*dlcab*distance)}")
                payment_method = int(input("Which payment method would you like to use?\n1.UPI\t2.Card\n"))

                if payment_method == 1:
                    upi =(input("Enter your UPI ID(10 digit mobile number only):  "))

                    if upi.isdigit() and len(upi) == 10:
                        confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                        if confirm_detail==1:
                            time.sleep(2)
                            print("Your Payment is Sucessfull, Enjoy the ride")
                        else:
                            print("Incorrcet information, transection failed!")

                    else:
                        print("Invalid UPI,transection failed")

                elif payment_method == 2:
                    card =(input("Enter your last 6 digit of card: "))
                    if card.isdigit() and len(card) == 6:
                        cvv = (input("Enter you 3 digit CVV number: "))
                        if cvv.isdigit() and len(cvv) == 3:
                            confirm_detail=int(input("We are not liable for any information, Are the provided details are correct?(enter in numeric only)\n1.Yes\t2.No\n"))

                            if confirm_detail==1:
                                time.sleep(2)
                                print("Your Payment is Sucessfull, Enjoy the ride")
                            else:
                                print("Incorrcet information, transection failed!")
                                
                        else:
                            print("Wrong CVV number, transection failed! ")
                    else:
                        print("Card details are incorrect, transection failed!")
                else:
                    print("Invalid input!")
            else:
                print("Invalid input!")
        else:
            print("Invalid input")

    else:
        print("Invalid option selected! Try again!")

else:
    print("Invalid Username or Password, Try again!")
