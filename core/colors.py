def red(string):
    return "\033[91m%s\033[0m" % string

def gray(string):
    return "\033[90m%s\033[0m" % string

def message(symbol, message):
    print(gray("[") + red(symbol) + gray("] ") + gray(message))

def help(command, requirement):
    # print(gray("[") + red("!") + gray("] ") + gray("Command Error!"))
    print(gray("[") + red("!") + gray("] ") + red(command) + " " + gray("<") + red(requirement) + gray(">"))

def yesno():
    return gray("[") + red("Y") + gray("/") + red("N") + gray("]")
