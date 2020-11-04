def decode_netbios(nbname):
    if len(nbname) != 32:
        return nbname
    l = []
    for i in range(0, 32, 2):
        l.append(chr(((ord(nbname[i]) - 0x41) << 4) |
                     ((ord(nbname[i+1]) - 0x41) & 0xf)))
    return ''.join(l).split('\x00', 1)[0]