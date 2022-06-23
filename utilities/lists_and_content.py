"""For lists and resources for randomising content
"""
from random import randint, shuffle
import copy

def ip_address(length:int = 4)->str:
    return '.'.join([str(randint(0, 255)) for i in range(length)])

names = ('Boris', 'Charles', 'Angela', 'Jeremy', 'Dianne', 'Xandra', 'Xavier', 'Rasputin', 'Olga', 'Helga', 'Niamh')
filenames = ('todo', 'shopping', 'people', 'artichokes', 'videos', 'shoes')