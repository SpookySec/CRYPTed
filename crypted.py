# LIBS
import os
import platform
import base64

# CORE
from core.banner import banner
from core.colors import red, gray, message, help
from core.cmd_cmplt import PathComplete, CommandComplete, HistoryClear, commands
from core.loading import load
from core.update import update
from core.help import help_message

# MODULES
from modules import hash_id
from modules.bases import debase32, debase58, debase64
from modules.rots import rot13, rot47
from modules.hex import decode_hex
from modules.vigenere import decode_vigenere
from modules.url import url_decode
from modules.morse import morse_decode

fbanner = open("core/banner.txt")
banner(fbanner, 0.05)
fbanner.close()

while True:
    try:
        CommandComplete()
        cmd = input(red("crypted") + gray(" » "))

        if cmd != "":

            # URL DECODE
            if cmd.split()[0] == "url-decode":
                argv = cmd.split()

                if len(argv) < 2:
                    help("url-decode", "URL")
                
                else:
                    message("+", url_decode(argv[1]))

            # VIGENERE
            if cmd.split()[0] == "vigenere":
                argv = cmd.split()

                if len(argv) < 3:
                    print(gray("[") + red("!") + gray("] ") + red("vigenere") + " " + gray("<") + red("key") + gray(">")+ " " + gray("<") + red("ciphered text") + gray(">"))

                else:
                    try:
                        message("+", decode_vigenere(argv[2], argv[1]))
                    except:
                        message("!", "An Unknown Error Has Occurred!")
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
            
            # ROT47
            if cmd.split()[0] == "rot47":
                argv = cmd.split()

                if len(argv) < 2:
                    help("rot47", "shifted string")

                else:
                    try:
                        message("+", rot47(argv[1]))
                    except:
                        message("!", "An Unknown Error Has Occurred!")

            # MORSE
            if cmd.split()[0] == "morse-decode":
                argv = cmd.split()

                if len(argv) < 2:
                    help("morse-decode", "morse code")
                
                else:
                    try:
                        message("+", morse_decode(argv[1:]))
                    except Exception as e:
                        print(e.with_traceback())
                        message("!", "An Unknown Error Has Occurred!")
                        message("*", red("Format") + gray(": .... . .-.. .-.. ---"))


            # HELP
            if cmd.split()[0] == "help":
                help_message()

            # AUTHOR
            if cmd.split()[0] == "whoami":
                message("~", "Made By " + red("@") + gray("spooky_sec"))

            # CLEAR
            if cmd.split()[0] == "clear":
                os.system("clear")
            
            # RESET
            if cmd.split()[0] == "reset":
                HistoryClear()

            # BANNER
            if cmd.split()[0] == "banner":
                fbanner = open("core/banner.txt")
                banner(fbanner, 0)
                fbanner.close()

            # UPDATE
            if cmd.split()[0] == "update":
                try:
                    update()
                    message("+", "Updated Successfully")
                except:
                    message("!", "An Error Has Occurred!")
            
            # EXIT
            if cmd.split()[0] == "exit":
                message("~", "Bye :3")
                exit(0)

            # COMMAND NOT FOUND
            if cmd.split()[0] not in commands:
                message("!", gray("Use \"") + red("help") + gray("\" To List Available Commands"))
                    

    except KeyboardInterrupt:
        print()
        message("!", "Please Use \"" + red("exit") + gray("\" To Exit"))
        continue

    except Exception as e:    
        print(e.with_traceback())