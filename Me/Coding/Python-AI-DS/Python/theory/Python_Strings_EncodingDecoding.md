# Encoding and Decoding

Used for handling text data in different formats (e.g., UTF-8).

```python
label_text = "Any language string"
encoded_label = label_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")
```

| Variable            | Type    | Example Output           |
| ------------------- | ------- | ------------------------ |
| `encoded_label`     | `bytes` | `b'Any language string'` |
| `decoded_label`<br> | `str`   | `Any language string`    |
|                     |         |                          |

### Example Code
``` python
# Encoding and Decoding Example

text = "नमस्ते Python 👋"

# Encode string (str → bytes)
encoded_text = text.encode("utf-8")
print(encoded_text)
print(type(encoded_text))   # <class 'bytes'>

# Decode bytes (bytes → str)
decoded_text = encoded_text.decode("utf-8")
print(decoded_text)
print(type(decoded_text))   # <class 'str'>

# Equality check
print(text == decoded_text)  # True
```

**Output**
``` text
b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 Python \xf0\x9f\x91\x8b'
<class 'bytes'>
नमस्ते Python 👋
<class 'str'>
True
```

---