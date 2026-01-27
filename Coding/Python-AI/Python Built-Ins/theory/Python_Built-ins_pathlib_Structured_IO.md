# Structural inspection (no I/O)
- These operations are **pure**:
``` python
p = Path("/home/asp/audio.wav")

p.name      # "audio.wav"
p.stem      # "audio"
p.suffix    # ".wav"
p.parent    # Path("/home/asp")
p.parts     # ('/', 'home', 'asp', 'audio.wav')
```

No disk access occurs.

This enables:
- safe reasoning
- deterministic behavior
- testability

---
