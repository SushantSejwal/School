# Write a Python Program to Create a dictionary of Library information (bookid, bookname, bookprice, bookauthor), 
# input five values from the user and display the library, also change some values by searching the bookname in this dictionary.

import json

lib = {}
is_sushant_awesome = 'well yes'

while is_sushant_awesome:
    
    # If dictionary is empty then this will run
    if not lib:
        # asking user to add information or leave
        yes_or_no = input("Library is empty. If you want to add information then type yes[y] or type no[N] to leave\n ->  ").lower().strip()
        print() # empty line

    # If dictionary is not empty then this will run
    elif lib:    
        yes_or_no = input("\nIf you want to add more entries to the Library then type yes[y] or type no[N] to leave\n ->  ").lower().strip()
        print() # empty line
        
    else: 
        print('Whoppse try again')
        
    # Breaking break
    if yes_or_no == 'no' or yes_or_no == 'n':
        break
        
    elif yes_or_no == 'yes' or yes_or_no == 'y':

        book_ID = input('Enter ID of book\n ->  ')
        book_name = input(f'Enter name of book for ID {book_ID}\n ->  ')
        book_author = input(f'Enter {book_name} author name\n ->  ')
        book_price = int(input(f'Enter {book_name} Price\n ->  '))

        # adding item to dict
        lib[book_ID] = dict([('Name',book_name), ('Author',book_author), ('Price',book_price)])
        
    else: 
        print('Whoppse try again')

print(f"Library -> {json.dumps(lib, indent=4)}")

if lib:
    while True:
        yes_no = input('do you want to modify some books values. yes[Y] or no[N]\n ->  ').strip().lower()
        if yes_no == 'yes' or yes_no == 'y':
            
            any_value_modified = False
            book_srch = input("Enter the ID of the book you want to Modify\n ->  ")

            if book_srch in lib:
                what_to_change = input("What you want to change\n - press 1 for Name\n - press 2 for Author\n - press 3 for Price\n  ->  ").strip().lower()

                if what_to_change == '1' or what_to_change == 'name':
                    new_book_name = input(f'Enter new Name for book of ID \'{book_srch}\'\n ->  ')
                    lib[book_srch]['Name'] = new_book_name
                    any_value_modified = True

                elif what_to_change == '2' or what_to_change == 'author':
                    new_book_author = input(f'Enter new Author name for book of ID \'{book_srch}\'\n ->  ')
                    lib[book_srch]['Author'] = new_book_author
                    any_value_modified = True

                elif what_to_change == '3' or what_to_change == 'price':
                    new_book_price = input(f'Enter new Price for book of ID \'{book_srch}\'\n ->  ')
                    lib[book_srch]['Price'] = new_book_price
                    any_value_modified = True

                else:
                    print('whoopse try again')
                
                if any_value_modified:
                    print(f"modified book with ID '{book_srch}' -> {json.dumps(lib[book_srch], indent=4)}")

            else:
                print(f"book with ID '{book_srch}' doesn't exist in the book")
                    
        elif yes_no == 'no' or yes_no == 'n':
            break
        else:
            print('whhoooppppsssseee didn\'t understand.')

else:
    print('Library is empty, Enter some books')
    
# Output
# Library is empty. If you want to add information then type yes[y] or type no[N] to leave
#  ->  y

# Enter ID of book
#  ->  1
# Enter name of book for ID 1
#  ->  Awesome
# Enter Awesome author name
#  ->  SD  
# Enter Awesome Price
#  ->  9876

# If you want to add more entries to the Library then type yes[y] or type no[N] to leave
#  ->  n

# Library -> {
#     "1": {
#         "Name": "Awesome",
#         "Author": "SD",
#         "Price": 9876
#     }
# }
# do you want to modify some books values. yes[Y] or no[N]
#  ->  n