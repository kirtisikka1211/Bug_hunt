
import random
from hangman import hangman_game

# list of file names
file_names = ['medium1.py','medium2.py','medium3.py','medium4.py','medium5.py','medium6.py',
              'medium7.py','medium8.py','medium9.py','medium10.py']

# select a random file name from the list
random_file_name = random.choice(file_names)

# call hangman_game with the selected file name
hangman_game(random_file_name)
