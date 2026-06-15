# Code

``` python
def build_cipher_alphabet(key):
    seen = []
    for char in key.upper():
        if char.isalpha() and char not in seen:
            seen.append(char)
    remaining = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if c not in seen]
    return seen + remaining

def monoalphabetic_encrypt(plaintext, key):
    cipher_alpha = build_cipher_alphabet(key)
    result = ""
    for char in plaintext.upper():
        if char.isalpha():
            result += cipher_alpha[ord(char) - 65]
        else:
            result += char
    return result

def monoalphabetic_decrypt(ciphertext, key):
    cipher_alpha = build_cipher_alphabet(key)
    plain_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in ciphertext.upper():
        if char.isalpha():
            result += plain_alpha[cipher_alpha.index(char)]
        else:
            result += char
    return result


key = "the quick brown fox jumps over the lazy dog"
plaintext = "attack postponed to tomorrow"

ct = monoalphabetic_encrypt(plaintext, key)
pt = monoalphabetic_decrypt(ct, key)

print(ct)  # THHTEQ UICHUIKBR HI HIOIWWIN
print(pt)  # ATTACK POSTPONED TO TOMORROW
```

---
