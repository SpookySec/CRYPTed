abc = "abcdefghijklmnopqrstuvwxyz"

def rot13(string):
    secret = "".join([abc[(abc.find(c)+13)%26] for c in string])
    return secret

def rot47(string):
    x = []
    for i in range(len(string)):
        j = ord(string[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(string[i])
    return ''.join(x)