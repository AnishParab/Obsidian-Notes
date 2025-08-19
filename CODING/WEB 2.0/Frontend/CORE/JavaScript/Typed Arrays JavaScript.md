# Typed-Arrays
- For **binary data** (like from WebGL, audio buffers):
``` js
let buffer = new ArrayBuffer(8);
let view = new Uint8Array(buffer);
view[0] = 255;

```

---
