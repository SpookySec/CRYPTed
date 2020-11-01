def blink(string):
    return "\033[5m%s\033[0m" % string

def red(string):
    return "\033[91m%s\033[0m" % string

def green(string):
    return "\033[32m%s\033[0m" % string

def yellow(string):
    return "\033[33m%s\033[0m" % string

def blue(string):
    return "\033[34m%s\033[0m" % string

def magenta(string):
    return "\033[35m%s\033[0m" % string

def cyan(string):
    return "\033[36m%s\033[0m" % string

def gray(string):
    return "\033[90m%s\033[0m" % string

def white(string):
    return "\033[97m%s\033[0m" % string

def message(symbol, message):
    print(gray("[") + red(symbol) + gray("] ") + gray(message))

def help(command, requirement):
    # print(gray("[") + red("!") + gray("] ") + gray("Command Error!"))
    print(gray("[") + red("!") + gray("] ") + red(command) + " " + gray("<") + red(requirement) + gray(">"))