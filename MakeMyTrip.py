fprice=2000
bfprice=5000
a1price=10000
hprice=1000
vhprice=2000
tprice=500
actprice=1000
cprice=250 
lcprice=500
laundary=100

print("\t\t\t\tmake my trip\t\t\t\t\t\t")

print("\n1.Flights\t2.Hotels\t3.Trains\t4.Buses\t\t5.Cabs")        


option=int(input("\nSelect from the options you want to book.(enter in numeric only): "))

if option==1:
    print("\nWelcome to our Flight booking portal, we are happy:) to serve you our services.")    
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
            
            print("\nWe are not liable for any incorrect details.")
            confirm_detail=int(input("Are the provided details are correct?(enter in numeric only)\n\n1.Yes\t2.No\n\n"))

            if confirm_detail==1:
               print("\nAmount Paid! Booking Confirmed!")
               print("Thank you for choosing our hotel booking service! Enjoy the stay :) ")

            else:
                print("\nBooking cancelled due to incorrect details, Please try again :(")
            
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
            
            print("\nWe are not liable for any incorrect details.")
            confirm_detail=int(input("Are the provided details are correct?(enter in numeric only)\n\n1.Yes\t2.No\n\n"))

            if confirm_detail==1:
               print("\nAmount Paid! Booking Confirmed!")
               print("Thank you for choosing our hotel booking service! Enjoy the stay :)")

            else:
                print("\nBooking cancelled due to incorrect details, Please try again :(")
            

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
            print("\nWe are not liable for any incorrect details.")

            confirm_detail=int(input("Are the provided details are correct?(enter in numeric only)\n\n1.Yes\t2.No\n\n"))

            if confirm_detail==1:
               print("\nAmount Pai! Booking Confirmed!")
               print("Thank you for choosing our hotel booking service! Enjoy the stay :)")

            else:
                print("\nBooking cancelled due to incorrect details, Please try again :(")

        else:
            print("\nInvalid option selected")

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
            
            print("\nWe are not liable for any incorrect details.")

            confirm_detail=int(input("Are the provided details are correct?(enter in numeric only)\n\n1.Yes\t2.No\n\n"))
            if confirm_detail==1:
               print("\nAmount Piad! Booking Confirmed!")
               print("Thank you for choosing our hotel booking service! Enjoy the stay :) ")

            else:
                print("\nBooking cancelled due to incorrect details, Please try again :(")
            
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
            
            print("\nWe are not liable for any incorrect details.")

            confirm_detail=int(input("Are the provided details are correct?(enter in numeric only)\n\n1.Yes\t2.No\n\n"))
            if confirm_detail==1:
               print("\nAmount Piad! Booking Confirmed!")
               print("Thank you for choosing our hotel booking service! Enjoy the stay :) ")

            else:
                print("\nBooking cancelled due to incorrect details, Please try again :(")

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
            
            print("\nWe are not liable for any incorrect details.")
            confirm_detail=int(input("Are the provided details are correct?(enter in numeric only)\n\n1.Yes\t2.No\n\n"))
            if confirm_detail==1:
               print("\nAmount Piad! Booking Confirmed!")
               print("Thank you for choosing our hotel booking service! Enjoy the stay :) ")

            else:
                print("\nBooking cancelled due to incorrect details, Please try again :(")
    
    else:
        print("invalid option selected")

elif option==3:

    print("\nWelcome to Indian Railways")
    train_type=int(input("\nSelect which type of train you want to book.\n\n1.Sleeper\t2.AC \n"))
    if train_type==1:
        pdetails=int(input("Enter the no. of tickets you want to book: "))
        