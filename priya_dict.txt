#DICTIONARY store book name and price 

books = {}

def add():
    name = input("enter book name : ")
    price = int(input("enter book price : "))
    books[name] = price
    print("New book record added into dicitionary")

def modify():
    name=input("enter book name whose price you want to update : ")
    price=int(input("enter changed price of book : "))
    books[name]=price
    print("Book record update")

def delete():
    name=input("enter book name you want to delete : ")
    books.pop(name)
    print("record deleted")

def see():
    print("Book Name\t Price")
    for i in books:
        print(i,'\t\t',books[i])

def search(): 
    name=input("enter book name you want to search : ")
    for i in books:
        if i==name:
            print("Book found")
            print(i,'  :  ',books[i])
            break
    else:
          print("Book not found")

#Main Program

while True:
    print()
    print("\t ########## Choices ##########")
    print("\tenter 1 to add book name and price in the dictionary")
    print("\tenter 2 to see all books")
    print("\tenter 3 to change book information")
    print("\tenter 4 to find a book")
    print("\tenter 5 to a delete a book")
    print("\tenter 6 to exit")
    print("\t #############################")
    print()
    choice = int(input("enter your choice : "))


    if choice == 1:
        add()
    elif choice == 2:
        see()
    elif choice == 3:
        modify()
    elif choice == 4:
        search()
    elif choice == 5:
        delete()
    elif choice == 6:
        break
    else:
        print ("wrong choice")
        continue