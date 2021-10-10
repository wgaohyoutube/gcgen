import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("")
import colorama, time, random
colorama.init(autoreset=True)
from colorama import Fore
print(Fore.CYAN+"""

     ╔══════════╦══════════╦═════════════════╗
     ║ Consoles ║    PC    ║  Subscriptions  ║
     ╠══════════╬══════════╬═════════════════╣
     ║ xbox     ║ steam    ║ spotify premium ║
     ║ ps4      ║ ms store ║                 ║
     ║          ║ amazon   ║                 ║
     ╚══════════╩══════════╩═════════════════╝

     * type it exact *

""")
key = input("     card     \     ")
keys = int(input("     amount     \     "))
numb = 0
invalid = 0
for i in range(0,keys):
    time.sleep(0.001)
    ran = random.randrange(0,100)
    print(Fore.RED+"     invalid card")
    invalid = invalid + 1
    if ran == 20:
        print(Fore.GREEN+"     valid card  ",Fore.CYAN+"[valid]")
        numb = numb + 1
print(Fore.LIGHTGREEN_EX+"     all cards checked successfully")
print("    ",numb,Fore.CYAN+"valid card(s)")
invalid = invalid - numb
print("    ",invalid,Fore.RED+"invalid card(s)")




while True:
    recheck = input("     type 'r' to recheck your cards     \     ")
    if recheck == "r":
        for i in range(0,keys):
            time.sleep(0.001)
            ran = random.randrange(0,100)
            print(Fore.RED+"     invalid card")
            invalid = invalid + 1
            if ran == 20:
                print(Fore.GREEN+"     valid card  ",Fore.CYAN+"[valid]")
                numb = numb + 1
    print(Fore.LIGHTGREEN_EX+"     all cards rechecked successfully")
    print("    ",numb,Fore.CYAN+"valid card(s)")
    invalid = invalid - numb
    print("    ",invalid,Fore.RED+"invalid card(s)")