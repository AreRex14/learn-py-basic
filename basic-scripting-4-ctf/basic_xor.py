# simple xor python text encryption/decryption

def xor(data, key):
    return bytearray(a^b for a, b in 
zip(*map(bytearray, [data, key])))

# >>> one_time_pad = 'shared secret' 
# >>> plaintext = 'unencrypted' 
# >>> ciphertext = xor(plaintext, one_time_pad) 
# >>> ciphertext 
# bytearray(b'\x06\x06\x04\x1c\x06\x16Y\x03\x11\x06\x16') 
# >>> decrypted = xor(ciphertext, one_time_pad) 
# >>> decrypted
# bytearray(b'unencrypted')
# >>> plaintext == str(decrypted)
# True