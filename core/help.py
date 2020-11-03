import json

def red(string):
    return "\033[91m%s\033[0m" % string

def gray(string):
    return "\033[90m%s\033[0m" % string

def help_message():
    list = json.load(open("core/commands.json"))
    for cmd in list:
        print(gray("[") + red("~") + gray("] ") + red(cmd["name"]) + gray(":") + " " + gray(cmd["description"]))