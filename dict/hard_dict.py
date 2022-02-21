# Program to create a dictionary store and store items in it with name, price, quantity, company name.
import json # importing json to preety print our dictionaries

Store = dict()  # empty dictionary store

#  <------------     FUNCTION TO ADD ITEMS INTO STORE    ------------>  #

def ins():
    
    # function to store all code that insert values
    def main_ins():
        if item_name in Store:
            print(f"{item_name} already exist in Store, {item_name} values will get update")
            print() # empty line for formatting

        item_price = int(input(f'Enter the price of {item_name} in Rs\n -->  '))
        item_quan = int(input(f'Enter the quantity of {item_name}\n -->  '))
        item_comp = input(f'Enter the company name or manufacturer name of {item_name}\n -->  ')
        print() # empty line for formatting
        print(f' --->>  "{item_name}" has been added in the Store')
        print() # empty line for formatting

        Store[item_name] = dict([('Price', item_price),('Quantity', item_quan), ('Company Name', item_comp)])
    
    steve_jobs = True # flag for the loop inside function
    
    while steve_jobs:
        item_name = input('Enter the name of item\n -->  ')
        main_ins()
        

        while True:
            more_or_not = input('type yes[Y] to add more items or no[N] to leave or just type number of items you want to add\n -->  ').strip().lower()
            
            if more_or_not.isalpha():
                if more_or_not == 'n' or more_or_not == 'no':
                    steve_jobs = False # the main loop will terminate
                    break # the inner loop will terminate
                elif more_or_not == 'y' or more_or_not == 'yes':
                   break # the inner loop will terminate
                    
                else:
                    print('whooopse didn\'t get it')
               
            elif more_or_not.isdigit():
                more_or_not = int(more_or_not)
                
                for i in range(1, more_or_not + 1):
                    if more_or_not == 1:
                        item_name = input('Enter the name of item\n -->  ')
                    elif i == 1:
                        item_name = input(f'Enter the name of {i}st item\n -->  ')
                    elif i == 2:
                        item_name = input(f'Enter the name of {i}nd item\n -->  ')
                    elif i == 3:
                        item_name = input(f'Enter the name of {i}rd item\n -->  ')
                    elif i > 3:
                        item_name = input(f'Enter the name of {i}th item\n -->  ')
                    main_ins()
                    
                steve_jobs = False
                break

            else:
                print(' :(  whoopse didn\'t understand that please only type numbers or only aplhabet')
                continue
      
#  <------------     FUNCTION TO UPDATE ITEMS OF STORE    ------------>  #  

def update():

    # function to store all code that update
    def update_all():
        if not (item_name in Store):
            print(f"{item_name}  doesn\'t exist in the Store, {item_name} and it\'s values will get add")
            print() # empty line for formatting

        item_price = int(input(f'Enter the price of {item_name} in Rs\n -->  '))
        item_quan = int(input(f'Enter the quantity of {item_name}\n -->  '))
        item_comp = input(f'Enter the company name or manufacturer name of {item_name}\n -->  ')
        
        Store[item_name] = dict([('Price', item_price),('Quantity', item_quan), ('Company Name', item_comp)])

        print() # empty line for formatting
        print(f' --->>  "{item_name}" has been update')
        print() # empty line for formatting

    def update_price():
        if item_name in Store:
            item_price = int(input(f'Enter the price of {item_name} in Rs\n -->  '))
            Store[item_name]['Price'] = item_price
            print() # empty line for formatting
            print(f' --->>  "{item_name}" price has been update')
            print() # empty line for formatting
        
        else:
            print(f'{item_name} doesn\'t exist in the Store. try adding it')
            

    def update_quantity():
        if item_name in Store:
            item_quan = int(input(f'Enter the quantity of {item_name}\n -->  '))
            Store[item_name]['Quantity'] = item_quan
            print() # empty line for formatting
            print(f' --->>  "{item_name}" quantity has been update')
            print() # empty line for formatting
        
        else:
            print(f'{item_name} doesn\'t exist in the Store. try adding it')

    def update_company():
        if item_name in Store:
            item_comp = input(f'Enter the company name or manufacturer name of {item_name}\n -->  ')
            Store[item_name]['Company Name'] = item_comp
            print() # empty line for formatting
            print(f' --->>  "{item_name}" company name has been update')
            print() # empty line for formatting
        
        else:
            print(f'{item_name} doesn\'t exist in the Store. try adding it')
        
    steve_jobs = True # flag for the loop inside function
    
    while steve_jobs:
        item_name = input('Enter the name of item\n -->  ')
        
        if item_name not in Store:
            update_all()
            
        else:
            what_to_update = input('which item you want to update\n\t1 : for price\n\t2 : for quantity\n\t3 : for company name\n\t4 : for all\n    -->  ').lower().strip()

            if what_to_update == '1' or what_to_update == 'price' or what_to_update == 'rs':
                update_price()
            elif what_to_update == '2' or what_to_update == 'quan' or what_to_update == 'quantity':
                 update_quantity()
            elif what_to_update == '3' or what_to_update == 'company name' or what_to_update == 'comp name':
                update_company()
            elif what_to_update == '4' or what_to_update == 'all':
                update_all()
            
        
        
        while True:
            more_or_not = input('type yes[Y] to update more items or no[N] to leave or just type number of items you want to update\n -->  ').strip().lower()
            
            if more_or_not.isalpha():
                if more_or_not == 'n' or more_or_not == 'no':
                    steve_jobs = False # the main loop will terminate
                    break # the inner loop will terminate
                elif more_or_not == 'y' or more_or_not == 'yes':
                   break # the inner loop will terminate
                    
                else:
                    print('whooopse didn\'t get it')
               
            elif more_or_not.isdigit():
                more_or_not = int(more_or_not)
                
                for i in range(1, more_or_not + 1):
                    if more_or_not == 1:
                        item_name = input('Enter the name of item\n -->  ')
                    elif i == 1:
                        item_name = input(f'Enter the name of {i}st item\n -->  ')
                    elif i == 2:
                        item_name = input(f'Enter the name of {i}nd item\n -->  ')
                    elif i == 3:
                        item_name = input(f'Enter the name of {i}rd item\n -->  ')
                    elif i > 3:
                        item_name = input(f'Enter the name of {i}th item\n -->  ')
                        
                    what_to_update = input('what you want to update\n\t1 : for price\n\t2 : for quantity\n\t3 : for company name\n\t4 : for all\n   -->  ').lower().strip()
        
                    if what_to_update == '1' or what_to_update == 'price' or what_to_update == 'rs':
                        update_price()
                    elif what_to_update == '2' or what_to_update == 'quan' or what_to_update == 'quantity':
                         update_quantity()
                    elif what_to_update == '3' or what_to_update == 'company name' or what_to_update == 'comp name':
                        update_company()
                    elif what_to_update == '4' or what_to_update == 'all':
                        update_all()
                    
                steve_jobs = False
                break

            else:
                print(' :(  whoopse didn\'t understand that please only type numbers or only aplhabet')
                continue

#  <------------     FUNCTION TO DELETE ITEMS FROM STORE    ------------>  #  

def delete():
    # if dictionary is NOT empty then this will run
    if Store:
        steve_jobs = True # flag for the loop inside function

        while steve_jobs:
            item_name = input('Enter the item name that you want to delete \n -->  ')

            if item_name in Store:
                Store.pop(item_name)
                print(f' -->>   {item_name} no more exist in the dictionary Store')
                print() # empty line for formatting
            else:
                print(':( WHoooopppsesseee,  look like the item doesn\'t exist. Try adding it')
                print() # empty line for formatting

            while True:
                more_or_not = input('type yes[Y] to delete more items or no[N] to leave or just type number of items you want to delete\n -->  ').strip().lower()

                if more_or_not.isalpha():
                    if more_or_not == 'n' or more_or_not == 'no':
                        steve_jobs = False
                        break
                    
                    elif more_or_not == 'y' or more_or_not == 'yes':
                        break
                    
                    else:
                        print('whooopse didn\'t get it')
                    
                elif more_or_not.isdigit():
                    more_or_not = int(more_or_not)

                    for i in range(1, more_or_not + 1):
                        if more_or_not == 1:
                            item_name = input('Enter the item name that you want to delete \n -->  ')
                        elif i == 1:
                            item_name = input(f'Enter the {i}st item name that you want to delete \n -->  ')
                        elif i == 2:
                            item_name = input(f'Enter the {i}nd item name that you want to delete \n -->  ')
                        elif i == 3:
                            item_name = input(f'Enter the {i}rd item name that you want to delete \n -->  ')
                        elif i > 3:
                            item_name = input(f'Enter the {i}th item name that you want to delete \n -->  ')

                        if item_name in Store:
                            Store.pop(item_name)
                            print(f' -->>   {item_name} no more exist in the dictionary Store')
                            print() # empty line for formatting
                        else:
                            print(':( WHoooopppsesseee,  look like the item doesn\'t exist. Try adding it')
                            print() # empty line for formatting


                    steve_jobs = False
                    break

                else:
                    print(' :(  whoopse didn\'t understand that please only type numbers or only aplhabet')
                    continue
    else:
        print('the Store has currently no items. first add items then delete')
    

def search():  # fuction to search for dictionary item      
    # if dictionary is NOT empty then this will run
    if Store:
        steve_jobs = True # flag for the loop inside function

        while steve_jobs:
            item_name = input('Enter the name of item that you wanna search\n -->  ')
            if item_name in Store:
                print(f' -->>    {item_name} exist in the dictionary')
                print(f'{item_name} ->  {json.dumps(Store[item_name], indent = 3)}')
                print() # empty line for formatting
            else:
                print(':( WHoooopppsesseee,  look like the item doesn\'t exist. Try adding it')
                print() # empty line for formatting
                
            while True:
                more_or_not = input('type yes[Y] to search more items or no[N] to leave or just type number of items you want to search\n -->  ').strip().lower()

                if more_or_not.isalpha():
                    if more_or_not == 'n' or more_or_not == 'no':
                        steve_jobs = False
                        break
                    
                    elif more_or_not == 'y' or more_or_not == 'yes':
                        break
                    
                    else:
                        print('whooopse didn\'t get it')
                    
                elif more_or_not.isdigit():
                    more_or_not = int(more_or_not)

                    for i in range(1, more_or_not + 1):
                        if more_or_not == 1:
                            item_name = input('Enter the item name that you want to search \n -->  ')
                        elif i == 1:
                            item_name = input(f'Enter the {i}st item name that you want to search \n -->  ')
                        elif i == 2:
                            item_name = input(f'Enter the {i}nd item name that you want to search \n -->  ')
                        elif i == 3:
                            item_name = input(f'Enter the {i}rd item name that you want to search \n -->  ')
                        elif i > 3:
                            item_name = input(f'Enter the {i}th item name that you want to search \n -->  ')
                            
                        if item_name in Store:
                            print(f' -->>    {item_name} exist in the dictionary')
                            print(f'{item_name} ->  {json.dumps(Store[item_name], indent = 3)}')
                            print() # empty line for formatting
                        else:
                            print(':( WHoooopppsesseee,  look like the item doesn\'t exist. Try adding it')
                            print() # empty line for formatting

                    steve_jobs = False
                    break

                else:
                    print(' :(  whoopse didn\'t understand that please only type numbers or only aplhabet')
                    continue
    else:
        print('the Store has currently no items. first add items then search')
    

def display():  # fuction to display dictionary item      
    print(f'Store -> {json.dumps(Store, indent = 4)}')
    print() # empty line for formatting


# Creating flag for while loops, instead of writing True, sushant can be used
sushant = True

while sushant:
    
    what = input('type help[h] for help or function name or number to perform operations or type quit[q] to leave\n -->  ')
    print()
    what = what.lower().strip() # removing white spaace and coverting to lower to reduce errors

    if what == 'quit' or what == 'q' or what == '6':
        break

    elif what == 'help' or what == 'h' or what == '7':
        print("""                <----------    help    ---------->
              
            ->  type 1 or insert or ins to add items into the dictionary Store
            ->  type 2 or update or updt to update items in the dictinary Store    
            ->  type 3 or delete or del to delete items from the dictinary Store    
            ->  type 4 or search or srch to find items in the dictinary Store    
            ->  type 5 or show or disp to show the dictinary Store    
            ->  type 6 or quit or q to quit    
            ->  type 7 or help or h to show this message again    
            
                <-------------------------------->
            """)
    
    elif what == '1' or what == 'insert' or what == 'ins':
        ins()
    
    elif what == '2' or what == 'update' or what == 'updt':
        update()
    
    elif what == '3' or what == 'delete' or what == 'del':
        delete()
    
    elif what == '4' or what == 'search' or what == 'srch':
        search()
    
    elif what == '5' or what == 'show' or what == 'disp':
        display()
    else:
        continue
