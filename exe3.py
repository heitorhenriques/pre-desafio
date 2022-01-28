from ast import BitXor
from binascii import unhexlify

def bxor(a, b):
    "bitwise XOR of bytestrings"
    return bytes([ x^y for (x,y) in zip(a, b)])

if __name__ == '__main__':
    msg = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    key = 2

    decryp_text = ""

    for a in range(65,91):
        candidate_key = a.to_bytes(1, byteorder='big')
        keystream = candidate_key*len(msg)
        decryp_text = bxor(msg,keystream)
        
        print("Decrypted text ",chr(a),": {}".format(decryp_text))
    
    #O melhor candidato é o caracter 88
    print("\n")
    print("O melhor candidato é o caracter ",chr(88))