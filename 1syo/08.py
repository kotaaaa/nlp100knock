


def cipher(word):
    return "".join(chr(219 - ord(i)) if 'a'<=i<='z' else i for i in word)




if __name__ == "__main__":
    sentence = "Hello 23world"
    ciphertext = cipher(sentence)

    print (sentence)
    print (ciphertext)
    print (cipher(ciphertext))
