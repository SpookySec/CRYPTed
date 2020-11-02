# LIBS
import os
import platform


# CORE
from core import banner
from core.colors import *
from core.cmd_cmplt import PathComplete, CommandComplete, commands

# MODULES
from modules import hash_id



fbanner = open("core/banner.txt")
banner.banner(fbanner, 0.1)

while True:
    try:
        CommandComplete()
        cmd = input(red("crypted") + gray(" » "))

        if cmd != "":

            # HASH-ID
            if cmd.split()[0] == "hash-id":
                argv = cmd.split()

                if len(argv) < 2:
                    help("hash-id", "hash")
                else:
                    hashid = hash_id.HashID()
                    results = hash_id.parseHashes(hashid.identifyHash(argv[1]))
                    
                    if len(results) > 0:
                        count = 0
                        
                        for hashtype in results:
                            count += 1
                            message(count, hashtype)
                    
                    else:
                        message("*", "No Hashes Matched!")
            
            if cmd.split()[0] == "magic":
                argv = cmd.split()

                if len(argv) < 2:
                    help("magic", "cipher string")

            # CLEAR
            if cmd.split()[0] == "clear":
                os.system("clear")

            # BANNER
            if cmd.split()[0] == "banner":
                banner.banner(fbanner, 0)
            

            # COMMAND NOT FOUND
            if cmd.split()[0] not in commands:
                message("!", gray("Use \"") + red("help") + gray("\" to list available commands"))
                    

    except Exception as e:
        print(e)