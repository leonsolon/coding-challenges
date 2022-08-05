import string


def caesarCipher(s, k):
    # Write your code here

    alphabet = string.ascii_lowercase
    rotate = k % len(alphabet)
    alphabet_cipher = alphabet[rotate:] + alphabet[:rotate]
    new_s = ''
    for caract in s:
        if caract.lower() in alphabet:
            idx = alphabet.index(caract.lower())
            new_caract = alphabet_cipher[idx]
            if caract == caract.upper():
                new_caract = new_caract.upper()
        else:
            new_caract = caract
        new_s += new_caract
    return new_s
