from binascii import unhexlify

class InvalidMessageException(Exception):
    pass

def bxor(a, b):
    "bitwise XOR of bytestrings"
    return bytes([ x^y for (x,y) in zip(a, b)])

def attack_single_byte_xor(ciphertext):
    ascii_text_chars = list(range(97, 122)) + [32]
    best = {"nb_letters": 0}
    for i in range(2**8):
        candidate_key = i.to_bytes(1, byteorder='big')
        candidate_message = bxor(ciphertext, candidate_key*len(ciphertext))
        nb_letters = sum([ x in ascii_text_chars for x in candidate_message])
        if nb_letters>best['nb_letters']:
            best = {"message": candidate_message, 'nb_letters': nb_letters, 'key': candidate_key}
    
    if best['nb_letters'] > 0.7*len(ciphertext):
        return best
    else:
        raise InvalidMessageException('best candidate message is: %s' % best['message'])

if __name__ == '__main__':
    with open('desafio4.txt') as data_file:
        ciphertext_list = [
            unhexlify(line.strip())
            for line in data_file
        ]

    candidates = list()
    for (line_nb, ciphertext) in enumerate(ciphertext_list):
        try:
            message = attack_single_byte_xor(ciphertext)['message']
        except InvalidMessageException:
            pass
        else:
            candidates.append({
                'line_nb': line_nb,
                'ciphertext': ciphertext,
                'message': message
            })
        
    if len(candidates) > 1:
        print("Error: more than one candidate")
    else:
        for (key, value) in candidates[0].items():
            print(f'{key}: {value}')