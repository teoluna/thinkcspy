def rot13(mess):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ''
    for char in mess:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            if (alphabet.index(char) + (25-alphabet.index(char))) % 25: 
                pos = alphabet.index(char) + 13
                encrypted = encrypted + alphabet[pos]
            else:
                pos = (alphabet.index(char) + 13) - 26
                encrypted = encrypted + alphabet[pos]
    return encrypted

print(rot13('abcde'))
print(rot13('nopqr'))
print(rot13(rot13('since rot thirteen is symmetric you should see this message')))
