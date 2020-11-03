def decode_octal(num_list):
    values = []
    for octal_string in num_list:
        number = int(octal_string, base=8)
        values.append(number)
    return "".join(chr(value) for value in values)