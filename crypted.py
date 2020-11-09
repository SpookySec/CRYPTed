#!/usr/bin/python3
# LIBS
import os
import platform
if platform.system() != "Linux":
    print("[!] Sorry This Tool Is Meant To Be Run On Linux :/")
    exit(0)

try:
    # CORE
    from core.banner import banner
    from core.colors import red, gray, message, help
    from core.cmd_cmplt import PathComplete, CommandComplete, HistoryClear, commands
    from core.help import help_message

    import base64
    
    # MODULES
    from modules import hash_id
    from modules.bases import debase32, debase58, debase64
    from modules.rots import rot13, rot47
    from modules.hex import decode_hex
    from modules.vigenere import decode_vigenere
    from modules.url import url_decode
    from modules.morse import morse_decode
    from modules.utf import utf_decode
    from modules.nato import convert_nato
    from modules.octal import decode_octal
    from modules.netbios import decode_netbios
    from modules.binary import decode_binary
    from modules.reverse import reverse_string
    from modules.decimal import decode_decimal
    from modules.bacon import decode_bacon
    from modules import cracker

except ModuleNotFoundError:
    message("!", "Please Run 'install.sh'!")
    exit(1)

banner(0.001)

while True:
    try:
        CommandComplete()
        cmd = input(red("crypted") + gray(" » "))

        if cmd != "":

            # CRACK HASH
            if cmd.split()[0] == "crack":
                argv = cmd.split()
                
                if len(argv) < 2:
                    help("crack", "hash")

                else:
                    try:
                        c = cracker.OnlineHashCrack(argv[1])
                        success = c.Crack()

                        if not success:
                            message("!", "Couldn't Crack The Hash!")

                        else:
                            message("+", "Successfully Cracked!")
                            message("+", "Hash: {}".format(c.hash))
                            message("+", "Plain: {}".format(c.plaintext))
                    except:
                        message("!", "An Unknown Error Has Occurred!")

            # DECIMAL
            if cmd.split()[0] == "bacon-decode":
                argv = cmd.split()

                if len(argv) < 2:
                    help("bacon-decode", "bacon string")
                else:
                    try:
                        message("+", decode_bacon(argv[1].lower()))
                    except ValueError:
                        message("!", "Please Provide Real Bacon Ciphers")
                    except:
                        message("!", "An Unknown Error Has Occurred!")

            # DECIMAL
            if cmd.split()[0] == "decimal-convert":
                argv = cmd.split()

                if len(argv) < 2:
                    help("decimal-convert", "decimal string")
                else:
                    try:
                        message("+", decode_decimal(argv[1:]))
                    except ValueError:
                        message("!", "Only Takes Decimal Values")
                    except:
                        message("!", "An Unknown Error Has Occurred!")

            # REVERSE STRING
            if cmd.split()[0] == "reverse-string":
                argv = cmd.split()

                if len(argv) < 2:
                    help("reverse-string", "string")
                else:
                    try:
                        message("+", reverse_string(argv[1]))
                    except:
                        message("!", "An Unknown Error Has Occurred!")
                        
            # NET BIOS
            if cmd.split()[0] == "binary-convert":
                argv = cmd.split()

                if len(argv) < 2:
                    help("binary-convert", "binary number")
                else:
                    try:
                        message("+", decode_binary(argv[1:]))
                    except ValueError:
                        message("!", "Binary Is Only 1s And 0s")
                        message("*", red("Format") + gray(": 01101000 01101001"))
                    except OverflowError:
                        message("!", "That Number Was Greater Than Maximum")
                        message("*", red("Format") + gray(": 01101000 01101001"))
                    except Exception as e:
                        print(e.with_traceback())
                        message("!", "An Unknown Error Has Occurred!")

            # NET BIOS
            if cmd.split()[0] == "netbios-decode":
                argv = cmd.split()

                if len(argv) < 2:
                    help("netbios-decode", "name")
                else:
                    try:
                        message("+", decode_netbios(argv[1].strip()))
                    except:
                        message("!", "An Unknown Error Has Occurred!")

            # OCTAL
            if cmd.split()[0] == "octal":
                argv = cmd.split()

                if len(argv) < 2:
                    help("octal", "octal strings")
                else:
                    try:
                        octal_strings = argv[1:]
                        message("+", decode_octal(octal_strings))
                    except ValueError:
                        message("!", "Make Sure You're Using Octal Numbers!")
                        message("*", red("Format") + gray(": 150 145 154 154 157"))
                    except:
                        message("!", "An Unknown Error Has Occrred!")
                        message("*", red("Format") + gray(": 150 145 154 154 157"))

            # NATO
            if cmd.split()[0] == "nato":
                argv = cmd.split()

                if len(argv) < 2:
                    help("nato", "ascii string")
                else:
                    try:
                        word = convert_nato(argv[1])
                        if not word:
                            message("!", "Can't Convert These Characters")
                        for letter in word:
                            message("+", letter)
                    except:
                        message("!", "An Unknown Error Has Occrred!")
            

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
                    print(gray("[") + red("!") + gray("] ") + red("vigenere") + " " + gray("<") + red("ciphered text") + gray(">")+ " " + gray("<") + red("key") + gray(">"))

                else:
                    try:
                        message("+", decode_vigenere(argv[1], argv[2]))
                    except:
                        message("!", "An Unknown Error Has Occurred!")
            # DECODE HEX
            if cmd.split()[0] == "hex-decode":
                argv = cmd.split()

                if len(argv) < 2:
                    help("hex-decode", "hex string")
                
                else:
                    try:
                        message("+", decode_hex("".join(argv[1:])))
                    except ValueError:
                        message("!", "Doesn't Look Like Hex")
                        message("!", red("Format: ") + gray("41 41 41 41"))
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
            if cmd.split()[0] == "base32-decode":
                argv = cmd.split()

                if len(argv) < 2:
                    help("base32-decode", "encoded string")

                else:
                    try:
                        message("+", debase32(argv[1]))
                    except base64.binascii.Error:
                        message("!", "Doesn't Look Like base32")
                    except:
                        message("!", "An Unknown Error Has Occurred!")
            
            # BASE 58
            if cmd.split()[0] == "base58-decode":
                argv = cmd.split()

                if len(argv) < 2:
                    help("base58-decode", "encoded string")

                else:
                    try:
                        message("+", debase58(argv[1]))
                    except (UnicodeDecodeError, ValueError):
                        message("!", "Doesn't Look Like base58")
                    except:
                        message("!", "An Unknown Error Has Occurred!")
            
            # BASE 64
            if cmd.split()[0] == "base64-decode":
                argv = cmd.split()

                if len(argv) < 2:
                    help("base64-decode", "encoded string")

                else:
                    try:
                        message("+", debase64(argv[1]))
                    except base64.binascii.Error:
                        message("!", "Doesn't Look Like base64")
                    except:
                        message("!", "An Unknown Error Has Occurred!")

            # ROT13
            if cmd.split()[0] == "rot13-decode":
                argv = cmd.split()

                if len(argv) < 2:
                    help("rot13-decode", "shifted string")
                
                else:
                    try:
                        message("+", rot13(argv[1]))
                    except:
                        message("!", "An Unknown Error Has Occurred!")
            
            # ROT47
            if cmd.split()[0] == "rot47-decode":
                argv = cmd.split()

                if len(argv) < 2:
                    help("rot47-decode", "shifted string")

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
                        cipher = ""
                        for char in argv[1:]:
                            cipher += " "
                            cipher += char
                        cipher = cipher.strip()
                        message("+", morse_decode(cipher))
                    except ValueError:
                        message("!", "Ay, That Ain't No Valid Letter")
                        message("*", red("Format") + gray(": .... . .-.. .-.. ---"))
                    except Exception as e:
                        print(e.with_traceback())
                        message("!", "An Unknown Error Has Occurred!")
                        message("*", red("Format") + gray(": .... . .-.. .-.. ---"))
            
            # UTF-8
            if cmd.split()[0] == "utf-8-decode":
                argv = cmd.split()

                if len(argv) < 2:
                    help("utf-8-decode", "text")

                else:
                    try:
                        message("+", utf_decode(argv[1]))
                    except Exception as e:
                        message("!", "An Unknown Error Has Occurred!")
                        print(e.with_traceback())


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
                banner(0)
            
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
