import sys, time

def red(string):
    return "\033[91m%s\033[0m" % string

def gray(string):
    return "\033[90m%s\033[0m" % string

banner_text = f"""
{red(" ██████╗") + gray(r"                       __           __")}
{red("██╔════╝") + gray(r"     _______  ______  / /____  ____/ /")}
{red("██║     ") + gray(r"    / ___/ / / / __ |/ __/ _ |/ __  / ")}
{red("██║     ") + gray(r"   / /  / /_/ / /_/ / /_/  __/ /_/ /  ")}
{red("╚██████╗") + gray(r"  /_/   |__, / .___/|__/|___/|__,_/   ")}
{red(" ╚═════╝") + gray(r"     /____/_/                         ")}
\n"""

def banner(amount):
    for letter in banner_text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(amount)
