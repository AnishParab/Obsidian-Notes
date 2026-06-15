# `curl` Flags

**Request**
```bash
-X GET/POST/PUT/PATCH/DELETE   # method (inferred when possible)
-H "Key: Value"                # header (repeatable)
-d '{"key":"val"}'             # request body
--data-urlencode "key=val"     # URL-encode body automatically
-F "file=@path/to/file"        # multipart form (file upload)
```

**Response**
```bash
-i                             # headers + body
-I                             # headers only (HEAD request)
-o file.json                   # save body to file
-O                             # save with server's filename
-w "%{http_code}"              # extract specific response info
-s                             # silent (no progress bar)
```

**Debugging**
```bash
-v                             # verbose (full request + response)
--trace file.txt               # dump everything to file (more than -v)
--trace-ascii file.txt         # same but readable
```

**Connection**
```bash
-L                             # follow redirects
--max-redirs 5                 # limit redirect hops
--connect-timeout 5            # TCP connection timeout (seconds)
-m 10                          # max total time (seconds)
--retry 3                      # retry on failure
--retry-delay 2                # seconds between retries
```

**Auth**
```bash
-u user:pass                   # basic auth
-H "Authorization: Bearer tk"  # bearer token
--cert cert.pem                # client certificate
--cacert ca.pem                # custom CA cert
-k                             # skip TLS verification (dangerous)
```

**Misc**
```bash
-c cookies.txt                 # save cookies to file
-b cookies.txt                 # send cookies from file
--compressed                   # request compressed response
-K config.txt                  # read flags from file
--http2                        # force HTTP/2
--http3                        # force HTTP/3
```

---
