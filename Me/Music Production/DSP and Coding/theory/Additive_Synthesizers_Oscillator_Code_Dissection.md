# `make_time_array`

```python
np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
```

##### **What it's doing:**
- `sample_rate * duration` = total number of samples. At 44100Hz for 1 second = 44100 samples.
- `linspace` spaces them evenly from `0` to `duration`.
- `endpoint=False` excludes the final value.

##### **Why `endpoint=False` matters:**
- Say duration = 1.0s. With `endpoint=True` you'd get samples at:
```
[0/44100, 1/44100, 2/44100, ..., 44100/44100]
```
- That last sample is exactly at `t = 1.0`. If you render another 1-second block and concatenate, the boundary looks like:
```
... t=0.9999, t=1.0000, t=0.0000, t=0.0001 ...
```
- `t=1.0` and the next block's `t=0.0` are both present — you've doubled a sample at the seam. For a sine wave that introduces a tiny discontinuity. Clicks in audio. `endpoint=False` avoids this.

---
# `sine_oscillator`

```python
amplitude * np.sin(2 * np.pi * freq * t + phase)
```
- This is vectorized — `t` is an array, so numpy computes all 44100 values in one C-level loop. No Python `for` loop. This is the right way to do DSP in numpy.

##### **Why `2π`?** 
- `sin` operates in radians. One full cycle = `2π` radians. So `2π · f · t` gives you `f` full cycles per second — which is exactly what frequency means.

##### **The phase argument `φ`:**
- Right now it's useless for a single oscillator — shifting the phase of one sine doesn't change how it sounds. But consider two partials:
```python
p1 = sine_oscillator(440, 0.5, 1.0, phase=0)
p2 = sine_oscillator(440, 0.5, 1.0, phase=np.pi)  # 180° shifted
sum = p1 + p2  # → silence. Complete cancellation.
```
- Phase alignment between partials determines whether they reinforce or cancel. In additive synthesis with many partials, phase relationships shape the transient character of a sound — even if steady-state timbre is identical.

---
# The normalization contract

- The function returns values in `[-1, 1]`. This is a convention you must enforce everywhere in your signal chain.

When you start stacking partials:
```python
wave = partial1 + partial2 + partial3 + ...
```

- Each one contributes amplitude. If you have 10 partials each at amplitude 0.5, your output peaks at ±5.0. That's catastrophic clipping when written to a WAV file.

- You'll need to normalize before writing:
```python
wave = wave / np.max(np.abs(wave))
```

- Or manage amplitudes upfront so the sum stays within bounds. We'll handle this properly in Step 2.

---
# `sf.write`

```python
sf.write("sine_440.wav", wave, SAMPLE_RATE)
```

- `soundfile` infers bit depth from the numpy dtype. `np.float64` (numpy default) → 64-bit float WAV. That's fine for offline work. For compatibility with DAWs (like Bitwig), 32-bit float or 16-bit int is more standard:

```python
sf.write("sine_440.wav", wave.astype(np.float32), SAMPLE_RATE, subtype='FLOAT')
```

- Keep this in mind — we'll standardize to `float32` going forward.

---
# The plot window — why only 5ms?

```python
samples_5ms = int(SAMPLE_RATE * 0.005)
```

- At 440Hz, one cycle = `1/440 ≈ 2.27ms`. Plotting 1 full second = 44100 points of a repeating wave — visually useless, looks like a solid block. 5ms gives you ~2 full cycles — enough to see the waveform shape clearly.

---
