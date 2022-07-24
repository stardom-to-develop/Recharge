# Library
import random as rd
from time import sleep as sp
from os import system as UI

# Welcome Message

UI("clear")
print("\n\n\n\n")
num_banner = rd.randint(1,10)
UI(f"cat banner/banner{num_banner}.txt")
# The user enters the slide type
print(f"\n\n\n\033[;32;mChoose the type of chip\naccording to the number corresponding to it")
print(f"\n\033[;31;m[\033[;37;m1\033[;31;m] \033[;35;mZain Iraq")
print(f"\n\033[;31;m[\033[;37;m2\033[;31;m] \033[;31;mAsiacell")
print(f"\n\033[;31;m[\033[;37;m3\033[;31;m] \033[;34;mKorek Telecom")
print(f"\n\033[;31;m[\033[;37;m99\033[;31;m] \033[;31;m HELP")
print(f"\n\033[;31;m[\033[;37;m00\033[;31;m] \033[;37;m EXIT")
enter = True
name_card = ""
while enter:
    try:
        name_card = float(input("\033[;32;m|\n|\n---->\033[;35;m"))
        enter = False
    except ValueError:
        print("Invalid entry (Enter a valid number)!!")
        enter = True
    if name_card == 1:
        enter = False
    elif name_card == 2:
        enter = False
    elif name_card == 3:
        enter = False
    elif name_card == 00:
        exit()
    elif name_card == 99:
        print("\033[;37;m")
        UI("cat README.md")
        enter = True
    else:
        enter = True
    if enter == True and name_card == 99:
        print("")
    elif enter == True:
        print("\033[;31;mInvalid entry!!!\033[;37;m")
    else:
        print("saved")

# The user enters the number of tokens required
print("\033[;32;mEnter the number of codes \033[;31;m[ex:100]")
enter = True
cods = ""
while enter:
    try:
        cods = float(input("\033[;31m|\n---->\033[;35;m"))
        enter = False
    except ValueError:
        print("Invalid entry (Enter a valid number)!!")
        enter = True
    if cods == 0:
        print("\033[;31;mYou cannot enter a zero here")
        enter = True
    else:
        print("")

start = 1
# Random generation phase

if name_card == 1: # Export Zain Iraq codes
    enter = input("\033[;35;mA zain Iraq\033[;33;m  will be generated press Enter to continue ")
    while start <= cods:
        cod = rd.randint(1000000000000000,9999999999999999) # 16 numbers 
        print(f"\033[;31;m[{start}] ---> \033[;33;m *101#{cod}# \033[;32;m Try this !!!")
        start = start + 1 # Add the number "1" each time until the required limit is reached
        sp(1)
elif name_card == 2: # Export Asiacell codes
    enter = input("\033[;31;mA Asiacell \033[;33;mwill be generated press Enter to continue ")
    while start <= cods:
        cod = rd.randint(10000000000000,99999999999999) # number generation code
        print(f"\033[;31;m[{start}] --->  \033[;33;m*133*{cod}# \033[;32;m Try this !!!") # Pre-selected code display message
        start = start + 1 # Add the number "1" each time until the required limit is reached
        sp(1) # Take a little break to get the text out elegantly
elif name_card == 3: # Export Korek Telecom codes
    enter = input("\033[;34;mA Korek Telecom \033[;33;m will be generated press Enter to continue ")
    while start <= cods:
        cod = rd.randint(10000000000000,99999999999999) # number generation code
        print(f"\033[;31;m[{start}] --->\033[;33;m  *221*{cod}# \033[;32;m Try this !!!") # Pre-selected c>
        start = start + 1 # Add the number "1" each time until the required limit i>
        sp(1) # Take a little break to get the text out elegantly
else:
    print("An error occurred in one of your inputs, restart the tool\nmake sure that the correct entries are made")

# Farewell message
print(f"\033[;32;mdone !!!\033[;37;m") # Here the farewell message appears 

