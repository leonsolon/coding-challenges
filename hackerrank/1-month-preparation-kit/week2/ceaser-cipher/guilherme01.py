def caesarCipher(s, k):
    # Write your code here
    original_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotate = k % len(original_alphabet)
    print(rotate)
    rotate_alphabet = original_alphabet[rotate:] + original_alphabet[:rotate]
    s_cipher = ''
    print(original_alphabet)
    print(rotate_alphabet)
    for i, letter in enumerate(s):

        if letter in original_alphabet:
            s_cipher = s_cipher + rotate_alphabet[original_alphabet.index(letter)]

        elif letter in original_alphabet.upper():
            s_cipher = s_cipher + rotate_alphabet[original_alphabet.index(letter.lower())].upper()
        else:
            s_cipher = s_cipher + letter
    return s_cipher