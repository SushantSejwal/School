# Write a Python Program to Create a hotel dictionary (bookingid, clientname, date, roomno) delete a value based on bookingid.

import json

hotel = {}
is_sushant_awesome = 'well yes'

while is_sushant_awesome:
    
    # If dictionary is empty then this will run
    if not hotel:
        # asking user to add information or leave
        yes_or_no = input("Hotel is empty. If you want to add information then type yes[y] or type no[N] to leave\n ->  ").lower().strip()
        print() # empty line

    # If dictionary is not empty then this will run
    elif hotel:    
        yes_or_no = input("\nIf you want to add more entries to the Hotel then type yes[y] or type no[N] to leave\n ->  ").lower().strip()
        print() # empty line
        
    else: 
        print('Whoppse try again')
        
    # Breaking break
    if yes_or_no == 'no' or yes_or_no == 'n':
        break
        
    elif yes_or_no == 'yes' or yes_or_no == 'y':

        booking_ID = input('Enter booking ID\n ->  ')
        client_name = input(f'Enter Name of Client\n ->  ')
        booking_date = input(f'Enter the booking date\n ->  ')
        room_no = int(input(f'Enter {client_name} room number\n ->  '))

        # adding item to dict
        hotel[booking_ID] = dict([('Name',client_name), ('Date',booking_date), ('Room',room_no)])
        
    else: 
        print('Whoppse try again')
        
print(f"Hotel -> {json.dumps(hotel, indent=4)}")

id_to_del = input('Enter the ID you want to delete\n ->  ')

if id_to_del in hotel:
    hotel.pop(id_to_del)
    print(f"booking detail with ID {id_to_del} has been deleted")

else:
    print(f"anything with ID {id_to_del} doesn't exit in the Hotel")
    
# Output
# Hotel is empty. If you want to add information then type yes[y] or type no[N] to leave
#  ->  y

# Enter booking ID
#  ->  1
# Enter Name of Client
#  ->  SS
# Enter the booking date
#  ->  15/4/2022
# Enter SS room number
#  ->  2

# If you want to add more entries to the Hotel then type yes[y] or type no[N] to leave
#  ->  n

# Hotel -> {
#     "1": {
#         "Name": "SS",       
#         "Date": "15/4/2022",
#         "Room": 2
#     }
# }
# Enter the ID you want to delete
#  ->  1
# booking detail with ID 1 has been deleted