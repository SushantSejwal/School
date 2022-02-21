# Write a Python Program to Input a list of numbers and swap elements at the even location with the elements at the odd location.

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
        lst.append(lst_ele)
    print()
    
print(f'original list -> {lst}')
print()

if len(lst) % 2 ==0:
    range = range(0, len(lst), 2)
else: 
    range = range(0, len(lst)-1, 2)

for i in range:
    lst[i], lst[i+1] = lst[i+1], lst[i]
    
print(f'list after swaping elements positions -> {lst}')

# Output
# Enter element for list or type "quit()" to leave
#  ->  324

# Enter element for list or type "quit()" to leave
#  ->  34

# Enter element for list or type "quit()" to leave
#  ->  2

# Enter element for list or type "quit()" to leave
#  ->  768

# Enter element for list or type "quit()" to leave
#  ->  098

# Enter element for list or type "quit()" to leave
#  ->  23

# Enter element for list or type "quit()" to leave
#  ->  quit()
# original list -> [324, 34, 2, 768, 98, 23]

# list after swaping elements positions -> [34, 324, 768, 2, 23, 98]