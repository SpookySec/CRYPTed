from core import banner
from core.colors import *
from core.cmd_cmplt import PathComplete, CommandComplete

"""
fbanner = open("core/banner.txt").readlines()
for line in fbanner:
    banner.banner(line, 0.001)
"""


while True:
    try:
        CommandComplete()
        cmd = input(red("crypted") + gray(" » "))

        if cmd != "":

            # HASH-ID
            if cmd.split()[0] == "hash-id":
                argv = cmd.split()
                if len(argv) < 2:
                    help("hash-id", "<hash>")

    except Exception as e:
        print(e)