brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
            '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
            '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']

asciicodes = [' ','!','"','#','$','%','&','','(',')','*','+',',','-','.','/',
              '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
              'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']

def convert(string, toNotation, fromNotation):
    return [toNotation[fromNotation.index(d)] for c in string for d in fromNotation if c == d]

def braille(string):
    return ''.join(convert(string, brailles, asciicodes))

def ascii(string):
    return ''.join(convert(string, asciicodes, brailles))
