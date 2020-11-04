def decode_binary(number_list):
    output = ""
    for num in number_list:
        output += chr(int(num, 2))
    
    return output