# Write a Python Program to Input a list/tuple of elements, search for a given element in the list/tuple and frequency 
# and position of search element.

lst = []
is_sushant_awesome = True

while is_sushant_awesome:
    lst_ele = input('Enter element for list or type "quit()" to leave\n ->  ')

    if lst_ele.lower().strip() == 'quit()':
        break
    
    else:
        lst.append(lst_ele)
    print()
 
srch = input('Enter the element you want to search in the list\n ->  ')

if srch in lst:
    srch_count = lst.count(srch)
    srch_pos = lst.index(srch)
    print(f"{srch} has appeared in the list {srch_count} times and at {srch_pos} index position")

else:
    print(f"{srch} doesn't exist in the list {lst}")    

# Output
# Enter element for list or type "quit()" to leave
#  ->  234

# Enter element for list or type "quit()" to leave
#  ->  345

# Enter element for list or type "quit()" to leave
#  ->  23

# Enter element for list or type "quit()" to leave
#  ->  56

# Enter element for list or type "quit()" to leave
#  ->  2424

# Enter element for list or type "quit()" to leave
#  ->  quit()
# Enter the element you want to search in the list
#  ->  23
# 23 has appeared in the list 1 times and at 2 index position