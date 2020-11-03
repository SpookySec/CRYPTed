import os
import readline
import glob
import json

commands = []
file = json.load(open("core/commands.json"))
for cmd in file:
    commands.append(cmd["name"])


def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

def pathComplete(text, state):
    if "~" in text:
        text = os.path.expanduser("~")
    if os.path.isdir(text):
        text += "/"
    return [x for x in glob.glob(text + "*")][state]

readline.set_completer_delims("\t")
readline.parse_and_bind("tab: complete")

def PathComplete():
    readline.set_completer(pathComplete)

def CommandComplete():
    readline.set_completer(completer)

def HistoryClear():
    readline.clear_history()
