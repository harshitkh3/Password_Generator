import random
import string

letters = string.ascii_letters
digits = string.digits
special = string.punctuation
dig_ip=True
spc_ip=True

#Password generator logic
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

#Handle the digit and special character choice    
def handle_ip(dig,spc):
    ans=[]
    if (dig=='y' or dig=='Y'):
     ans.append(True)
    else:
     ans.append(False)
    if (spc=='y' or spc=='Y'):
        ans.append(True)
    else:
        ans.append(False)
    return ans

        
#User Input
num=int(input('Enter the minimum length of the password : '))
dig_ip=input("Do you want digits in your password (y/n) : ")
spc_ip=input("Do you want special characters in your password (y/n) : ")
handle_ip(dig_ip,spc_ip)

handlr=handle_ip(dig_ip,spc_ip)

ans=pass_gen(num,handlr[0],handlr[1])
print('The generated password is :')
print(ans)

