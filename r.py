elif hoption == 2:
    print("\n\t\tWelcome to your two-room hotel booking")
    room_type = int(input("\nDo you want:\n1. Normal Room\n2. VIP AC Room\nEnter choice for both rooms (1 or 2): "))
    
    if room_type == 1:
        print("\nYou have selected Normal Room option")
        nights = int(input("\nEnter the number of nights you want to book for both rooms: "))
        payable_amount_per_room = hprice * nights
        total_payable_amount = payable_amount_per_room * 2
        print(f"\nTotal payable amount for both Normal Rooms ({nights} night(s)): {total_payable_amount}")
        
        confirm_info = input(f"\nIs the information correct for both rooms? (we are not responsible for any date/location mismatch):\nRoom Type: Normal Room\nNo. of Nights: {nights}\nTotal Payable Amount: {total_payable_amount}\n(Y/N): ").lower()
        
        if confirm_info == "y":
            rooms_confirmed = True
        else:
            print("\nPlease login again and correct your details. Booking Cancelled.")
            rooms_confirmed = False
    
    elif room_type == 2:
        print("\nYou have selected VIP AC Room for both rooms.")
        nights = int(input("\nEnter the number of nights you want to book for both rooms: "))
        payable_amount_per_room = vhprice * nights
        total_payable_amount = payable_amount_per_room * 2
        print(f"\nTotal payable amount for both VIP AC Rooms ({nights} night(s)): {total_payable_amount}")
        
        confirm_info = input(f"\nIs the information correct for both rooms? (we are not responsible for any date/location mismatch):\nRoom Type: VIP AC Room\nNo. of Nights: {nights}\nTotal Payable Amount: {total_payable_amount}\n(Y/N): ").lower()
        
        if confirm_info == "y":
            rooms_confirmed = True
        else:
            print("\nPlease login again and correct your details. Booking Cancelled.")
            rooms_confirmed = False
    
    else:
        print("\nInvalid choice for room type.")
        rooms_confirmed = False

    if rooms_confirmed:
        print(f"\nTotal payable amount for both rooms: {total_payable_amount}")
        
        confirm_info_all = input(f"\nIs the information correct? (we are not responsible for any date/location mismatch):\nRoom Type: {'Normal Room' if room_type == 1 else 'VIP AC Room'}\nNo. of Nights: {nights}\nTotal Payable Amount: {total_payable_amount}\n(Y/N): ").lower()
        
        if confirm_info_all == "y":
            print("\nChoose your payment method:")
            print("1. Card Payment")
            print("2. UPI Payment")
            payment_method = int(input("\nEnter your choice (1 or 2): "))
            
            if payment_method == 1:
                print("\nYou have chosen Card Payment.")
                card_number = input("Enter your card number (12 digits): ")
                card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                card_cvv = input("Enter your card CVV (3 digits): ")
                
                if len(card_cvv) == 3 and card_cvv.isdigit():
                    print(f"\nCard Number: {card_number}")
                    print(f"Card Expiry Date: {card_expiry}")
                    print(f"Card CVV: {card_cvv}")
                    confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                    
                    if confirm_card == "y":
                        print("\nProcessing card payment...")
                        time.sleep(1)
                        print("Payment successful. Your booking is confirmed!")
                    else:
                        print("\nPayment closed.")
                
                else:
                    print("\nInvalid CVV. It must be exactly 3 digits.")
            
            elif payment_method == 2:
                print("\nYou have chosen UPI Payment.")
                upi_id = input("Enter your UPI ID: ")
                upi_pin = input("Enter your UPI PIN (6 digits): ")
                
                if len(upi_pin) == 6 and upi_pin.isdigit():
                    confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                    
                    if confirm_upi == "y":
                        print("\nProcessing UPI payment...")
                        time.sleep(1)
                        print("\nPayment successful. Your booking is confirmed!")
                    else:
                        print("\nPayment closed")
                
                else:
                    print("\nInvalid UPI PIN. It must be exactly 6 digits.")
            
            else:
                print("\nInvalid payment method choice. Please try again.")
        else:
            print("\nBooking cancelled due to incorrect information.")
    else:
        print("\nBooking cancelled due to invalid room information.")