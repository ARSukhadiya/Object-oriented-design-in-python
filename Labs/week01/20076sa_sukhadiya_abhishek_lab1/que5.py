# Program title
print("Calculate and print the hotel bill")

# Define constants
STD_RM_RATE1 = 155
STD_RM_RATE2 = 160
STD_RM_RATE3_MORE = 165

DLX_RM_RATE1_2 = 195
DLX_RM_RATE3 = 210
DLX_RM_RATE4_MORE = 225

TAX = 0.12
BREAKFAST = 15
PARKING = 25
DISCOUNT_5_MORE_NIGHTS = 0.9

# Get user inputs
room_type = input("Please choose the room type(standard or deluxe): ").lower()
num_nights = int(input("Please enter the number of nights: "))
num_people = int(input("Please enter the number of people: "))
breakfast = input("Would you like breakfast (y/n): ").lower()
parking = input("Do you need parking (y/n): ").lower()

# Figure the room rate
room_rate = None
if room_type == "standard":
    if num_people < 1:
        print("Error: Invalid number of people!")
    elif num_people == 1:
        room_rate = STD_RM_RATE1
    elif num_people == 2:
        room_rate = STD_RM_RATE2
    else:
        room_rate = STD_RM_RATE3_MORE
elif room_type == "deluxe":
    if num_people < 1:
        print("Error: Invalid number of people!")
    elif num_people <= 2:
        room_rate = DLX_RM_RATE1_2
    elif num_people == 3:
        room_rate = DLX_RM_RATE3
    else:
        room_rate = DLX_RM_RATE4_MORE
else:
    print("Error: Invalid room type!")

# Calculate the room charges
if room_rate is not None:
    room_charges = room_rate * num_nights

    if num_nights < 1:
        print("\nError: Invalid number of nights!")

    if num_nights > 5:
        room_charges *= DISCOUNT_5_MORE_NIGHTS

    if breakfast == 'y':
        breakfast_charges = num_people * num_nights * BREAKFAST
    else:
        breakfast_charges = 0
    
    if parking == 'y':
        parking_charges = num_nights * PARKING
    else:
        parking_charges = 0
    

# The detailed hotel bill
subtotal = room_charges + breakfast_charges + parking_charges
total_tax = room_rate * TAX
print("\n\n_____A hotel bill_____")
print("Room charge: ", room_charges)
print("Breakfast charge:", breakfast_charges)
print("Parking charge:", parking_charges)
print("Subtotal:", subtotal)

print("\nTax (12% on room charges):", total_tax)
print("Total amount: ${}".format(subtotal + total_tax))