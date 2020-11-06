lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab', 
        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba', 
        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb', 
        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'} 

def decode_bacon(message): 
    decipher = '' 
    i = 0
    while True : 
        if(i < len(message)-4):
            substr = message[i:i + 5] 
            if(substr[0] != ' '): 
                decipher += list(lookup.keys())[list(lookup.values()).index(substr)] 
                i += 5
            else: 
                decipher += ' '
                i += 1
        else: 
            break
    return decipher