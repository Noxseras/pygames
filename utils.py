import os


# Clear Screen, cross platform
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
