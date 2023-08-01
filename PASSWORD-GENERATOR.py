import socket 
import sys
import os
from colorama import Fore as color
from time import sleep
import random
import string



bold = '\033[1m'
endbold = '\033[0m'

def banner():
    print(bold+color.RED+'''
        
         # #       #             # # #       
        #   #       #           #  #  #      PASSWORD GENERATOR
       #     #       #         #   #   #      
      #       #       #       #    #    #    
     #         #       #     #     #     #   
    #           #       #   #      #      #  
   #             #       # #       #       # 

     '''+endbold)

    print(bold+color.WHITE+'''
    
         -----------------------
        ⚒  PASSWORD GENERATOR  ⚒  
         -----------------------
         
     '''+endbold)  
    sleep(1)

os.system('clear')
banner()



def password_Generator():

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")  
    age = int(input("Enter your age: "))
    birth_date = input("Enter your birth date in YYYYMMDD format: ")

    numbers = random.sample(range(10), 4)
    letters = random.sample(string.ascii_letters, 6)

    special_chars = ["@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "="]

    password = first_name + last_name + str(age) + birth_date + "".join(map(str, numbers)) + "".join(letters)

    for i in range(5):
        password += str(random.choice(special_chars))

    password += "".join([random.choice([char.upper(), char.lower()]) for char in password])

    password = ''.join(random.sample(password,len(password))) 

    with open('password.txt', 'w') as f:
            f.write(password + '\n')

    print('\n' + password)

password_Generator()