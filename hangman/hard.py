
import random
from hangman import hangman_game

# list of file names
file_names = ['hard1.py','hard2.py','hard3.py','hard4.py','hard5.py','hard16.py',
              'hard7.py','hard18.py','hard9.py','hard10.py']

# select a random file name from the list
random_file_name = random.choice(file_names)

# call hangman_game with the selected file name
hangman_game(random_file_name)
