#------------- IMPORT -------------#
from os import system as c
import time
import random
import os

#------------- COLOUR -------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{G}
██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║  ██║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝ 
███████║███████║██║     ███████║██║██╔██╗ ██║██║  ███╗
██╔══██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██║   ██║
██║  ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
{Y}         HACKING WORLD - VIP DIAMOND HACK TOOL
{A}---------------------------------------------------
""")

#------------- ROOT CHECK -------------#
def root_check():
    try:
        uid = os.geteuid()
        if uid != 0:
            print(f"{R}[X] SORRY! ROOT DEVICE REQUIRED FOR THIS TOOL.")
            input(f"{A}\nPress Enter To Exit...")
            exit()
    except:
        print(f"{R}[X] ROOT DEVICE REQUIRED. NON-ROOT DEVICE DETECTED!")
        input(f"{A}\nPress Enter To Exit...")
        exit()

#------------- ANIMATION -------------#
def loading(txt):
    logo()
    print(f"{C}{txt}")
    for i in range(12):
        dots = "." * (i % 4)
        print(f"{Y}[{G}{'='*i}{A}>{' '*(12-i)}] {i*8}%{dots}", end="\r")
        time.sleep(0.25)
    print(f"{G}\n[✓] DONE!\n")
    time.sleep(1)

#------------- MAIN MENU -------------#
def menu():
    root_check()
    logo()
    print(f"{A}[1] START DIAMOND HACK")
    print(f"{A}[2] SHOW VIP PASSWORD LIST")
    print(f"{A}[0] EXIT TOOL")
    print(f"{A}--------------------------------------------------")
    choice = input(f"{Y}[?] SELECT OPTION: ")
    if choice == '1':
        diamond_hack()
    elif choice == '2':
        password_list()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION, TRY AGAIN")
        time.sleep(1)
        menu()

#------------- DIAMOND HACK -------------#
def diamond_hack():
    logo()
    c('espeak "Free Fire Diamond Hack Starting"')
    uid = input(f"{C}ENTER FREE FIRE UID: ")
    print(f"\n{Y}[+] Connecting to Garena Free Fire Server...")
    loading("Connecting...")
    print(f"{G}[✓] UID Verified: {uid}")

    print(f"\n{B}[+] Selecting Diamond Packages...")
    time.sleep(2)
    amounts = [500, 1000, 2000, 5000, 10000]
    for amount in amounts:
        print(f"{C}[*] Injecting {amount} Diamonds...")
        time.sleep(1.2)
    time.sleep(1)

    print(f"\n{R}[!] SECURITY CHECK COMPLETED ")
    time.sleep(1.5)
    print(f"{Y}Visit this link to finish verification: {G}https://garena-vip-confirm.com")

    input(f"\n{A}Press Enter To Return To Menu...")
    menu()

#------------- PASSWORD LIST -------------#
def password_list():
    logo()
    print(f"{P} VIP Diamond Hack Passwords:")
    passwords = [
        'diamondpro2025', 'garenaVIP@999', 'ffhackzone123',
        'ultrakingff', 'ffgodmodeX', 'vipprohack'
    ]
    for pw in passwords:
        print(f"{C}[*] {pw}")
        time.sleep(0.5)
    input(f"\n{A}Press Enter To Return To Menu...")
    menu()

#------------- START TOOL -------------#
menu()