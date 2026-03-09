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
    pwd=[]
    c_dig=False
    c_sp=False
    criteria=False

    if hasdigits==True:
        pwd.append(random.choice(digits))
    if hasspecial==True:
        pwd.append(random.choice(special))
    while len(pwd)<dig:
        pwd.append(random.choice(char))
    
    random.shuffle(pwd)

    return "".join(pwd)
    
# def handle_ip(dig_ip,spc_ip):
#     if (dig_ip=='y' or dig_ip=='Y'):
#      dig_ip=True
#     else:
#      dig_ip==False
#     if (spc_ip=='y' or spc_ip=='Y'):
#         spc_ip=True
#     else:
#         spc_ip==False

        


num=int(input('Enter the minimum length of the password : '))
dig_ip=input("Do you want digits in your password (y/n) : ")
spc_ip=input("Do you want special characters in your password (y/n) : ")
if (dig_ip=='y' or dig_ip=='Y'):
    dig_ip=True
else:
    dig_ip=False
if (spc_ip=='y' or spc_ip=='Y'):
    spc_ip=True
else:
    spc_ip=False
ans=pass_gen(num,dig_ip,spc_ip)
print('The generated password is :')
print(ans)

