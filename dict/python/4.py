# Write a Python Program to Input a list of numbers and test if a number is equal to the sum of the cubes of its digits.
# Find the smallest and largest number from the given list of numbers.

lst = []
is_sushant_awesome = True

while is_sushant_awesome:
    lst_ele = input('Enter element for list or type "quit()" to leave\n ->  ')

    if lst_ele.lower().strip() == 'quit()':
        break
    
    elif lst_ele.isdigit():
        lst_ele = int(lst_ele)
        lst.append(lst_ele)
    else:
        print(f"Enter only numbers")
    print()
    
for number in lst:
    sum_of_cubes = 0
    num = number
    while num > 0:
        num_last = num % 10
        sum_of_cubes = sum_of_cubes + num_last**3
        num = num // 10
        
    if sum_of_cubes == number:
        print(f'the sum of cubes of digits of number {number} is eaual to itself')
    else:
        print(f'the sum of cubes of digits of number {number} is not eaual to itself')
    
    
# Finding the largest number in the list
lar_num = 0
for i in lst:
    if i > lar_num:
        lar_num = i
lar_num_pos = lst.index(lar_num)
print()
print(f'the largest number in the lst is {lar_num} and it\'s index position is {lar_num_pos}')


# Finding the smallest number in the list
sml_num = lar_num
for i in lst:
    if i < sml_num:
        sml_num = i
sml_num_pos = lst.index(sml_num)
print(f'the smallest number in the lst is {sml_num} and it\'s index position is {sml_num_pos}')

# Output
# Enter element for list or type "quit()" to leave
#  ->  324

# Enter element for list or type "quit()" to leave
#  ->  23

# Enter element for list or type "quit()" to leave
#  ->  324

# Enter element for list or type "quit()" to leave
#  ->  54

# Enter element for list or type "quit()" to leave
#  ->  22

# Enter element for list or type "quit()" to leave
#  ->  quit
# Enter only numbers

# Enter element for list or type "quit()" to leave
#  ->  quit()
# the sum of cubes of digits of number 324 is not eaual to itself
# the sum of cubes of digits of number 23 is not eaual to itself 
# the sum of cubes of digits of number 324 is not eaual to itself
# the sum of cubes of digits of number 54 is not eaual to itself
# the sum of cubes of digits of number 22 is not eaual to itself

# the largest number in the lst is 324 and it's index position is 0
# the smallest number in the lst is 22 and it's index position is