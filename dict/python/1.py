# Write a Python Program to find the largest/smallest number in a list/tuple and displaying the position of that number

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
        print('Enter only numbers')
    print()

print(f'list -> {lst}')
        
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
#  ->  23

# Enter element for list or type "quit()" to leave
#  ->  65

# Enter element for list or type "quit()" to leave
#  ->  quit()
# list -> [23, 65]

# the largest number in the lst is 65 and it's index position is 1
# the smallest number in the lst is 23 and it's index position is 0