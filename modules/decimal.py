def decode_decimal(string):
    output = ""
    for number in string:
        output += chr(int(number, 10))
    return output
