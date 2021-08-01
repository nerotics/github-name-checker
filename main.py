import requests
import colorama
import ctypes
import os
from pathlib import Path
from colorama import Fore

current_path = os.path.dirname(os.path.realpath(__file__)) # Credits to MattyTM on Github
mypath = Path('users.txt')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    open(current_path +"/"+str("users")+str("")+".txt","a")
    clear()
    check()

def check():
    clear()
    if mypath.stat().st_size == 0:
        print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}!{Fore.WHITE}] {Fore.LIGHTBLUE_EX}Please put your usernames in users.txt")
    else:
        file = open("users.txt", 'r')
        data = file.read()
        names = data.split()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[!] Checking {len(names)} names ")
        with open("users.txt", 'r') as list:
            names = [ line.strip() for line in list.read().split('\n') if line ]
            for name in names:
                r = requests.get(f"https://github.com/" + name)
                if(r.status_code == 404):
                    print(f'{Fore.WHITE}[{Fore.GREEN}Valid{Fore.WHITE}]{Fore.GREEN} {name}')
                else: 
                    print(f'{Fore.WHITE}[{Fore.RED}Invalid{Fore.WHITE}]{Fore.RED} {name}')


main()
