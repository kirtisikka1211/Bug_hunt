# import os
# import subprocess
# import sys
# import traceback

# def hangman_game(filename):
#     """
#     Plays a game of Hangman where the player needs to fix bugs in a code snippet.

#     Arguments:
#     filename -- the name of the file with the buggy code
#     """
#     # Initialize the hangman display
#     MAX_TRIES = 3
#     hangman_display = ['O', '|', '/', '\\', '/', '\\']
#     current_try = 0

#     # Start the game loop
#     while current_try < MAX_TRIES:
#         # Display the current code snippet
#         with open(filename, 'r') as file:
#             code = file.read()
#         print('Code:')
#         print(code)
#         print('')

#         # Open the file in a text editor and wait for the editor to close
#         editor_command = os.getenv('EDITOR', 'nano') + ' ' + filename
#         subprocess.call(editor_command, shell=True)

#         # Try to compile and run the edited code
#         try:
#             with open(filename, 'r') as file:
#                 edited_code = file.read()
#             exec(edited_code)
#             print('Congratulations, the code runs without errors!')
#             return
#         except:
#             # Display the hangman character for the current try
#             print('')
#             print("   _____")
#             print("  |     |")
#             print("  |     " + ("O" if current_try > 0 else ""))
#             print("  |    " + ("/|\\" if current_try > 1 else ""))
#             print("  |     " + ("|" if current_try > 1 else ""))
#             print("  |    " + ("/ \\" if current_try > 2 else ""))
#             print("__|__")
#             print()
#             print('')
#             print('Incorrect! You have {} tries left.'.format(MAX_TRIES - current_try - 1))

#             # Increment the try counter and continue the loop
#             current_try += 1

#     # If the player runs out of tries, display the full hangman character
#     print('')
#     print('You ran out of tries! The correct code was:')
#     with open(filename, 'r') as file:
#         code = file.read()
#     print(code)
#     print('')
#     print("   _____")
#     print("  |     |")
#     print("  |     " + ("O" ))
#     print("  |    " + ("/|\\"))
#     print("  |     " + ("|" ))
#     print("  |    " + ("/ \\"))
#     print("__|__")
#     print('')
import os
import subprocess

def hangman_game(filename):
    """
    Plays a game of Hangman where the player needs to fix bugs in a code snippet.

    Arguments:
    filename -- the name of the file with the buggy code
    """
    # Initialize the hangman display
    MAX_TRIES = 3
    hangman_display = ['O', '|', '/', '\\', '/', '\\']
    current_try = 0

    while current_try < MAX_TRIES:
        # Display the current code snippet
        with open(filename, 'r') as file:
            code = file.read()
        
        print('')

        # Prompt the user to choose an editor
        editor_choice = input('to enter press t ')
        if editor_choice == 't':
            # Open the file in the terminal editor and wait for the editor to close
            editor_command = os.getenv('EDITOR', 'nano') + ' ' + filename
            subprocess.call(editor_command, shell=True)
        # elif editor_choice == 'n':
        #     # Open the file in nano and wait for the editor to close
        #     subprocess.call(['nano', filename])
        else:
            print('Invalid editor choice, please choose t ')

        # Try to compile and run the edited code
        try:
            with open(filename, 'r') as file:
                edited_code = file.read()
            exec(edited_code)
            print('Congratulations, the code runs without errors!')
            return
        except:
            # Display the hangman character for the current try
            print('')
            print("   _____")
            print("  |     |")
            print("  |     " + ("O" if current_try > 0 else ""))
            print("  |    " + ("/|\\" if current_try > 1 else ""))
            print("  |     " + ("|" if current_try > 1 else ""))
            print("  |    " + ("/ \\" if current_try > 2 else ""))
            print("__|__")
            print()
            print('')
            print('Incorrect! You have {} tries left.'.format(MAX_TRIES - current_try - 1))

            # Increment the try counter and continue the loop
            current_try += 1

    # If the player runs out of tries, display the full hangman character
    print('')
    print('You ran out of tries!')
    print('')
    print("   _____")
    print("  |     |")
    print("  |     " + ("O" ))
    print("  |    " + ("/|\\"))
    print("  |     " + ("|" ))
    print("  |    " + ("/ \\"))
    print("__|__")
    print('')
