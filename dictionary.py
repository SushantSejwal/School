# Program to create a dictionary store and store items in it with name, price, quantity, company name.
import json # importing json to preety print our dictionaries

Store = dict()  # empty dictionary store


#  <----    CREATING FUNCTIONS FOR MODIFING DICTIONARY    ---->  #
def ins():  # function to add items in the dictionary

    item_name = input('Enter the name of item\n -->  ')

    if item_name in Store:
        print(f"{item_name} already exist in dictionary Store, {item_name} values will get update")
        print() # empty line for formatting
    
    item_price = int(input(f'Enter the price of {item_name} in Rs\n -->  '))
    item_quan = int(input(f'Enter the quantity of {item_name}\n -->  '))
    item_comp = input(f'Enter the company name or manufacturer name of {item_name}\n -->  ')
    print() # empty line for formatting

    Store[item_name] = dict([('Price', item_price),('Quantity', item_quan), ('Company Name', item_comp)])
        

def update():  # fuction to update dictionary item 
    
    item_name = input('Enter the name of item\n -->  ')

    if not (item_name in Store):
        print(f"{item_name}  doesn\'t exist in dictionary Store, {item_name} and it\'s values will get insert")
        print() # empty line for formatting

    item_price = int(input(f'Enter the price of {item_name} in Rs\n -->  '))
    item_quan = int(input(f'Enter the quantity of {item_name}\n -->  '))
    item_comp = input(f'Enter the company name or manufacturer name of {item_name}\n -->  ')
    print() # empty line for formatting

    Store[item_name] = dict([('Price', item_price),('Quantity', item_quan), ('Company Name', item_comp)])


def delete():  # fuction to delete dictionary item

    item_name = input('Enter the item name that you want to delete \n -->  ')

    if item_name in Store:
        Store.pop(item_name)
        print(f'{item_name} no more exist in the dictionary Store')
        print() # empty line for formatting
    else:
        print(':( WHoooopppsesseee,  look like the item doesn\'t exist. Try adding it')
        print() # empty line for formatting
    

def search():  # fuction to search for dictionary item      

    item_name = input('Enter the name of item that you wanna search\n -->  ')
    if item_name in Store:
        print(f'{item_name} exist in the dictionary')
        print(f'{item_name} ->  {json.dumps(Store[item_name], indent = 3)}')
        print() # empty line for formatting
    else:
        print(':( WHoooopppsesseee,  look like the item doesn\'t exist. Try adding it')
        print() # empty line for formatting
    

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
