# Q.  Write a Python Program to Create a dictionary of employee information (empid,empname,empsal,empmobile), input five values from the user and display the employee who is getting salary less than or equal to Rs. 50000.

# Empty dict emp_information. information will be added by user
emp_information = {}

emp_sal_above_50_k = False  # flag for employee salary

# Creating flag
is_sushant_awesome = 'any doubt'

while is_sushant_awesome:
    
    # If dictionary is empty then this will run
    if not emp_information:
        # asking user to add information or leave
        yes_or_no = input("Employee Information dictionary is empty. If you want to add information then type yes[y] or type no[N] to leave\n =>  ")
        print() # empty line

    # If dictionary is not empty then this will run
    elif emp_information:    
        yes_or_no = input("\nIf you want to add more entries to the employee dictionary then type yes[y] or type no[N] to leave\n =>  ")
        print() # empty line
        
    else: 
        print('Whoppse try again')
        
    # Breaking break
    if yes_or_no.lower().strip() == 'no' or yes_or_no.lower().strip() == 'n':
        break
        
    elif yes_or_no.lower().strip() == 'yes' or yes_or_no.lower().strip() == 'y':

        emp_name = input('Enter empoyee Name\n =>  ')
        emp_id = input(f'Enter {emp_name} ID\n =>  ')
        emp_sal = int(input(f'Enter {emp_name} Salary\n =>  '))

        if emp_sal <= 50_000:
            emp_sal_above_50_k = True # creating a flag for after use if some one has a salary <= 50K
            
        emp_mob_no = int(input(f'Enter {emp_name} Mobile Number\n =>  '))
        # Checking mobile number
        if len(str(emp_mob_no)) > 10 or len(str(emp_mob_no)) < 10:
            print('Mobile no. shouold be of 10 digits only')
            emp_mob_no = int(input(f'Enter {emp_name} Mobile Number\n =>  '))

        # adding item to dict
        emp_information[emp_name] = dict([('ID',emp_id), ('Salary',emp_sal), ('Mobile No.',emp_mob_no)])
        
    else: 
        print('Whoppse try again')

# printiing an empty line for clear code or a little bit formatting
print()

if emp_sal_above_50_k:
    print('Employee who\'s salary is less or eqaul to 50K are =>')
    
    for key in emp_information:
        
        if emp_information[key]['Salary'] <= 50_000:
            print(f'{key} => {emp_information[key]}')
            
elif not emp_sal_above_50_k:
    print('No one has a Salary equal or less than 50K')
    
else:
    print('Awesome Sushant') #This will never print😞


