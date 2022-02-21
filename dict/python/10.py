# Write a Python program to implement the random function random, randint, Randrange using random module.

import random

print('''
The random() method returns a random floating number between 0 and 1.
The randint() method returns an integer number selected element from the specified range. This method is an alias for randrange(start, stop+1).
The randrange() method returns a randomly selected element from the specified range.
''')

# A game using functions from random module
print('    ####    <--> Snake(🐍) <-->    <--> Water(🌊) <-->    <--> Gun(🔫) <-->     ####    ')
print()

awesome = "Sushant"

while awesome:
    choice = input("Choose from Snake[S], Water[W] and Gun[G] or type quit[Q] to leave\n ->  ").strip().lower()
    comp_choice = ['s','w','g']
    random_num = random.randrange(0,3)
    comp_choice = comp_choice[random_num]

    if choice == 'quit' or choice == 'q':
        break
    
    # time when user will win
    elif (choice == 'snake' or choice == 's') and (comp_choice == 'w'):
        print('your choice -> Snake')
        print('computer\'s choice -> Water')
        print(' - you win - ')
        
    elif (choice == 'water' or choice == 'w') and (comp_choice == 'g'):
        print('your choice -> Water')
        print('computer\'s choice -> Gun')
        print(' - you win - ')
        
    elif (choice == 'gun' or choice == 'g') and (comp_choice == 's'):
        print('your choice -> Gun')
        print('computer\'s choice -> Snake')
        print(' - you win - ')
        
    # time when user will loose
    elif (choice == 'snake' or choice == 's') and (comp_choice == 'g'):
        print('your choice -> Snake')
        print('computer\'s choice -> Snake')
        print(' - you loose - ')
        
    elif (choice == 'water' or choice == 'w') and (comp_choice == 's'):
        print('your choice -> Water')
        print('computer\'s choice -> Snake')
        print(' - you loose - ')
        
    elif (choice == 'gun' or choice == 'g') and (comp_choice == 'w'):
        print('your choice -> Gun')
        print('computer\'s choice -> Water')
        print(' - you loose - ')
        
    else:
        print('WHOOPSE didn\'t understand')
    print()
  
# Output
# The random() method returns a random floating number between 0 and 1.
# The randint() method returns an integer number selected element from the specified range. This method is an alias for randrange(start, stop+1).
# The randrange() method returns a randomly selected element from the specified range.

#     ####    <--> Snake(🐍) <-->    <--> Water(🌊) <-->    <--> Gun(🔫) <-->     ####    

# Choose from Snake[S], Water[W] and Gun[G] or type quit[Q] to leave
#  ->  w
# your choice -> Water
# computer's choice -> Snake
#  - you loose - 

# Choose from Snake[S], Water[W] and Gun[G] or type quit[Q] to leave
#  ->  s
# your choice -> Snake
# computer's choice -> Water
#  - you win - 

# Choose from Snake[S], Water[W] and Gun[G] or type quit[Q] to leave
#  ->  g
# your choice -> Gun        
# computer's choice -> Snake
#  - you win -

# Choose from Snake[S], Water[W] and Gun[G] or type quit[Q] to leave
#  ->  q