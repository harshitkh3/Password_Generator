import random
import string

letters = string.ascii_letters
digits = string.digits
special = string.punctuation

def pass_gen (dig,hasdigits=True,hasspecial=True):
    char=letters
    if(hasdigits):
        char+=digits
    if(hasspecial):
        char+=special
    pwd=""
    c_dig=False
    c_sp=False
    criteria=False

    while not criteria or len(pwd)<dig:
        nexc=random.choice(char)
        pwd+=nexc
        if nexc in digits:
            c_dig=True
        if nexc in special:
            c_dig=True
        



pass_gen(5,True,True)

