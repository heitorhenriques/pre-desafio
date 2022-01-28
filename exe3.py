from ast import BitXor
from binascii import unhexlify

def bxor(a, b):
    "bitwise XOR of bytestrings"
    return bytes([ x^y for (x,y) in zip(a, b)])

def letter_ratio(input_bytes):
    ascii_text_chars = list(range(97, 122)) + [32]
    nb_letters = sum([ x in ascii_text_chars for x in input_bytes])
    return nb_letters / len(input_bytes)

def is_probably_text(input_bytes):
    r = letter_ratio(input_bytes)
    return True if r>0.7 else False

if __name__ == '__main__':
    msg = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

    for i in range(2**8):
        candidate_key = i.to_bytes(1, byteorder='big')
        keystream = candidate_key*len(msg)
        decryp_text = bxor(msg,keystream)
        
        if is_probably_text(decryp_text):
            key = chr(i)
            ascii_text_chars = list(range(97, 122)) + [32]
            nb_letters = sum([ x in ascii_text_chars for x in decryp_text])
            break
    
    print("chave:",key)
    print("menssagem:",decryp_text)
    print("numero de letras:",nb_letters)