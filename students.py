# Write a Python Program to Create a dictionary with the roll number, name and marks of n students in a class and 
# display the names of students who have marks above 75.

# Creating  awesome flag
is_sushant_awesome = "may be"
marks_above_75 = False

Class_sd = {}

while is_sushant_awesome:
    
    # this will run when there will be no element in dict class_sd
    if not Class_sd:
        yes_no = input('The Dictionary Class is empty. do wanna enter students data in that, type yes[y] to enter or no[n] to leave\n =>  ')
        print() # printing a empty line for formatting output

    elif Class_sd:
        yes_no = input('Do wanna enter more students data in Dictionary Class, type yes[y] to enter or no[n] to leave\n =>  ')
        print() # printing a empty line for formatting output


    yes_no = yes_no.lower().strip()
    
    if yes_no == 'no' or yes_no =='n':
        break

    elif yes_no == 'yes' or yes_no == 'y':
        std_name = input('Enter the name of student\n =>  ')
        std_roll = input(f'Enter the roll number of {std_name}\n =>  ')
        std_marks = int(input(f'Enter marks of {std_name} out of 100\n =>  '))
        if std_marks > 75:
            marks_above_75 = True
        if std_marks > 100 or std_marks < 0:
            std_marks = int(input('WHOOPSE Enter marks between 0 to 100\n =>  '))
        

        Class_sd[std_name] = dict([('Roll No',std_roll),('Marks',std_marks)])
        print() # Empty line for formatting
        
    else:
        print('WHOOPPSEE try again')
        continue


if marks_above_75:
    print('Students who get marks above 75 are :')
    for names in Class_sd:
        if Class_sd[names]['Marks'] > 75:
            print(f' Name - {names}, marks - {Class_sd[names]["Marks"]}')

else:
    print('There\'s no one in the class who got marks above 75')
