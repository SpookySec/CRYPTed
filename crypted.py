# LIBS
import os
import platform
import base64

# CORE
from core.banner import banner
from core.colors import *
from core.cmd_cmplt import PathComplete, CommandComplete, HistoryClear, commands
from core.loading import load
from core.update import update


# MODULES
from modules import hash_id
from modules.bases import debase32, debase58, debase64
from modules.rots import *
from modules.hex import decode_hex
from modules.vigenere import decode_vigenere

fbanner = open("core/banner.txt")
banner(fbanner, 0.05)
fbanner.close()

while True:
    try:
        CommandComplete()
        cmd = input(red("crypted") + gray(" » "))

        if cmd != "":

            # DECODE HEX
            if cmd.split()[0] == "hex":
                argv = cmd.split()

                if len(argv) < 2:
                    help("hex", "hex string")
                
                else:
                    try:
                        message("+", decode_hex(argv[1]))
                    except ValueError:
                        message("!", "Doesn't Look Like Hex")
                        message("!", red("Format: ") + gray("41414141"))
                    except Exception as e:
                        print(e.with_traceback())

            # HASH-ID
            if cmd.split()[0] == "hash-identifier":
                argv = cmd.split()

                if len(argv) < 2:
                    help("hash-identifier", "hash")
                else:
                    hashid = hash_id.HashID()
                    results = hash_id.parseHashes(hashid.identifyHash(argv[1]))
                    
                    if len(results) > 0:
                        count = 0
                        
                        load(gray("Parsing Hashes"), 3)
                        for hashtype in results:
                            count += 1
                            message(count, hashtype)
                    
                    else:
                        message("!", "No Hashes Matched!")
            
            # BASE 32
            if cmd.split()[0] == "base32":
                argv = cmd.split()

                if len(argv) < 2:
                    help("base32", "encoded string")

                else:
                    try:
                        message("+", debase32(argv[1]))
                    except base64.binascii.Error:
                        message("!", "Doesn't Look Like base32")
                    except:
                        message("!", "An Unknown Error Has Occurred!")
            
            # BASE 58
            if cmd.split()[0] == "base58":
                argv = cmd.split()

                if len(argv) < 2:
                    help("base58", "encoded string")

                else:
                    try:
                        message("+", debase58(argv[1]))
                    except (UnicodeDecodeError, ValueError):
                        message("!", "Doesn't Look Like base58")
                    except:
                        message("!", "An Unknown Error Has Occurred!")
            
            # BASE 64
            if cmd.split()[0] == "base64":
                argv = cmd.split()

                if len(argv) < 2:
                    help("base64", "encoded string")

                else:
                    try:
                        message("+", debase64(argv[1]))
                    except base64.binascii.Error:
                        message("!", "Doesn't Look Like base64")
                    except:
                        message("!", "An Unknown Error Has Occurred!")

            # ROT13
            if cmd.split()[0] == "rot13":
                argv = cmd.split()

                if len(argv) < 2:
                    help("rot13", "shifted string")
                
                else:
                    try:
                        message("+", rot13(argv[1]))
                    except:
                        message("!", "An Unknown Error Has Occurred!")

            
            # AUTHOR
            if cmd.split()[0] == "whoami":
                message("~", "Made By " + red("@") + gray("spooky_sec"))

            # CLEAR
            if cmd.split()[0] == "clear":
                os.system("clear")
                HistoryClear()

            # BANNER
            if cmd.split()[0] == "banner":
                fbanner = open("core/banner.txt")
                banner(fbanner, 0)
                fbanner.close()

            # UPDATE
            if cmd.split()[0] == "update":
                message("+", red("Response: ") + gray(update()))
            
            # EXIT
            if cmd.split()[0] == "exit":
                message("~", "Bye :3")
                exit(0)

            # COMMAND NOT FOUND
            if cmd.split()[0] not in commands:
                message("!", gray("Use \"") + red("help") + gray("\" To List Available Commands"))
                    

    except Exception as e:
        print(e.with_traceback())