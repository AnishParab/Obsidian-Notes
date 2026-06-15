# Brute Force on Caesar Cipher

- Try all 25 possible shifts until intelligible plaintext is found
- Demonstrates why Caesar Cipher is insecure

---
#### Example — Ciphertext: SQDYMZK

| Shift | Back | Result  |
|-------|------|---------|
| 0     | 26   | SQDYMZK |
| 1     | 25   | TREZNAL |
| 2     | 24   | USFAOBM |
| 3     | 23   | VTGBPCN |
| 4     | 22   | WUHCQDO |
| 5     | 21   | XVIDREP |
| 6     | 20   | YWJESFQ |
| 7     | 19   | ZXKFTGR |
| 8     | 18   | AYLGUHS |
| 9     | 17   | BZMHVIT |
| 10    | 16   | CANIWJU |
| 11    | 15   | DBOJXKV |
| 12    | 14   | ECPKYLW |
| 13    | 13   | FDQLZMX |
| 14    | 12   | GERMANY |
| 15    | 11   | HFSNBOZ |
| 16    | 10   | IGTOCP A|
| 17    | 9    | JHUPD QB|
| 18    | 8    | KIVQERC |
| 19    | 7    | LJWRFSD |
| 20    | 6    | MKXSGTE |
| 21    | 5    | NLYTHUF |
| 22    | 4    | OMZUIVC |
| 23    | 3    | PNAVJWD |
| 24    | 2    | QOBWKXE |
| 25    | 1    | RPCXLYJ |

- Shift 14 → **GERMANY** — intelligible plaintext found
- Only 25 attempts needed → brute force trivial

---
