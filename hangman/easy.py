import random
from hangman import hangman_game

# list of file names
file_names = ['easy1.py', 'easy2.py', 'easy3.py', 'easy4.py', 'easy5.py', 'easy6.py',
               'easy8.py', 'easy9.py', 'easy10.py', 'easy11.py', 'easy12.py', 'easy13.py',  'easy15.py', 'easy16.py', 'easy17.py']

# select a random file name from the list
random_file_name = random.choice(file_names)

# call hangman_game with the selected file name
hangman_game(random_file_name)
