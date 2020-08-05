import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def wait_for_anykey():
    input('\nany key to continue')
