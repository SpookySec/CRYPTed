import sys, time

def banner(str, amount):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(amount)

