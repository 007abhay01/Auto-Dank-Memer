#==========ImportingModules==========#
import sys
from colorama import Fore
from colorama import Back
import random
import pyautogui as p
import time
import pyperclip 
#==========main.py==========#
print("     _         _          ____              _      __  __                          ")
print("    / \  _   _| |_ ___   |  _ \  __ _ _ __ | | __ |  \/  | ___ _ __ ___   ___ _ __ ")
print("   / _ \| | | | __/ _ \  | | | |/ _` | '_ \| |/ / | |\/| |/ _ \ '_ ` _ \ / _ \ '__|")
print("  / ___ \ |_| | || (_) | | |_| | (_| | | | |   <  | |  | |  __/ | | | | |  __/ |   ")
print(" /_/   \_\__,_|\__\___/  |____/ \__,_|_| |_|_|\_\ |_|  |_|\___|_| |_| |_|\___|_|   ")
print("                                                                                   ")
print("Script was made by Monochromish | https://github.com/Monochromish/Auto-Dank-Memer | Please Star my Repository")
print("[ ALERT ] Run This Script At Your Own Risk. I am not responsible if your dank memer account gets banned / blacklisted ( yes it happens )")
def select_text() -> str:
    p.tripleClick(x=901, y=879)
    p.hotkey('ctrl', 'c')
    return pyperclip.paste()
def beg():
    p.typewrite('pls beg', interval=0.1)
    p.press('enter')
def fish():
    p.typewrite('pls fish', interval=0.04)
    p.press('enter')
def deposit():
    p.typewrite('pls deposit all', interval=0.07)
    p.press('enter')
def balance():
    p.typewrite('pls balance', interval=0.5)
    p.press('enter')
def inventory():
    p.typewrite('pls inv', interval=0.6)
    p.press('enter')
def search():
    p.typewrite('pls search', interval=0.1)
    p.press('enter')
    time.sleep(6)
    options = select_text().split(',')
    p.typewrite(random.choice(options), interval=0.2)
    p.press('enter')
def random_afk():
    rand = random.randint(0, 20) == 1
    if rand:
        afk = random.randint(1800, 2700)
        print('Going AFK For ', afk / 60, 'minutes')
        time.sleep(afk)
while True:
    try:
        random_afk()
        rand = random.randint(40, 60)
        print(
            Back.LIGHTRED_EX,
            'Sleeping',
            Back.RESET,
            f'{rand} {Fore.RED}s{Fore.RESET}',
        )
        time.sleep(rand)
        times = [0.3, 0.2, 0.5, 0.7, 1]
        options = ['beg', 'fish', 'search', 'deposit']
        na = []
        while True:
            choice = random.choice(options)
            if choice not in na:
                na.append(choice)
            if len(na) == 4:
                break
        for val in na:
            if val == 'beg':
                time.sleep(random.choice(times))
                print(
                    Back.LIGHTGREEN_EX,
                    'Begging',
                    Back.RESET,
                )
                beg()
                time.sleep(0.5)
            elif val == 'fish':
                time.sleep(random.choice(times))
                print(
                    Back.GREEN,
                    'Fishing',
                    Back.RESET,
                )
                fish()
                time.sleep(0.4)
            elif val == 'search':
                time.sleep(random.choice(times))
                print(
                    Back.LIGHTGREEN_EX,
                    'Searching',
                    Back.RESET,
                )
                search()
                time.sleep(0.6)
            elif val == 'deposit':
                time.sleep(random.choice(times))
                print(
                    Back.GREEN,
                    'Depositing',
                    Back.RESET
                )
                deposit()
            show_inventory = random.randint(0, 7) == 1
            if show_inventory:
                inventory()
            show_balance = random.randint(0, 7) == 1
            if show_balance:
                balance()
    except KeyboardInterrupt:
        print(f'{Fore.LIGHTRED_EX}Terminated.{Fore.RESET}')
        sys.exit()
#==========END==========#