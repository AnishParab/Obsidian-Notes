# Code

``` python
def caesar_cipher(text, k=3):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + k) % 26 + 65)
        else:
            result += char
    return result

def caesar_decipher(text, k=3):
    return caesar_cipher(text, -k)

def shift_cipher(text, k):
    return caesar_cipher(text, k)

def shift_decipher(text, k):
    return caesar_cipher(text, -k)


# Caesar (k=3)
print(caesar_cipher("obsidian"))      # REVLGLDQ
print(caesar_decipher("REVLGLDQ"))    # OBSIDIAN

# Shift (k=4)
print(shift_cipher("cryptography", 4))        # GVCTXSKVEPTC
print(shift_decipher("GVCTXSKVEPTC", 4))      # CRYPTOGRAPHY
```

---
