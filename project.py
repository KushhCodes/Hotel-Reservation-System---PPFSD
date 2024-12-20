def show_rooms():
    print("\n1. Single Room - Rs. 1500\n2. Double Room - Rs. 3000\n3. Executive Suite - Rs. 7500\n4. Premium Suite - Rs. 10000")

def book_room():
    name = input("\nName: ")
    try:
        nights = int(input("Nights: "))
        room_type = int(input("Room (1-4): "))
    except:
        print("Invalid input")
        return

    rooms = ["Single Room", "Double Room", "Executive Suite", "Premium Suite"]
    rates = [1500, 3000, 7500, 10000]

    if 1 <= room_type <= 4:
        total = rates[room_type - 1] * nights
        print(f"\nBooking: {name}, {rooms[room_type - 1]}, Nights: {nights}, Total: Rs. {total}\n")
    else:
        print("Invalid room choice")

def cancel_booking():
    print(f"\nBooking cancelled for {input('Name: ')}\n")

while True:
    print("\n1. Show Rooms\n2. Book Room\n3. Cancel Room\n4. Exit")
    try:
        choice = int(input("Choice: "))
    except:
        print("Invalid input")
        continue

    if choice == 1:
        show_rooms()
    elif choice == 2:
        book_room()
    elif choice == 3:
        cancel_booking()
    elif choice == 4:
        print("Goodbye")
        break
    else:
        print("Invalid choice")