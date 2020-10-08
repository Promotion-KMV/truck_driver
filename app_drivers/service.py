import random
import requests
from random import randint

def random_number_order():
    a = random.randint(100, 999)
    b = random.randint(100, 999)
    c = random.randint(100, 999)
#    d = random.randint(100, 999)
    number = f'{a}-{b}-{c}'
    
    return number

def ok():
	pass