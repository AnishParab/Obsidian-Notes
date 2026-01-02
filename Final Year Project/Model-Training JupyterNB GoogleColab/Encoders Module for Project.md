## Purpose

Transforms preprocessed audio features into latent vectors (`z`) for conditioning synthesis or representing timbre and style.
Located in `ddsp/training/encoders.py`.

---

## Core Class

### `ZEncoder`

Base class for latent encoders.

**Functions**

* Derives `input_keys` from `compute_z()` signature.
* Defines consistent output `{'z': tensor}`.
* Expands 2D z to match feature time resolution.

**Key method**

```python
def compute_z(self, *inputs):
    # Subclasses implement encoding logic
```

---

## Audio-Based Encoders

### 1. `MfccTimeDistributedRnnEncoder`

Encodes audio → MFCCs → RNN → Dense → z.

**Specs**

* Predefined FFT sizes for 63–1000 time steps.
* Instance normalization (`nn.Normalize('instance')`).
* RNN type selectable (`gru` or `lstm`).
* Output: time-varying latent z.

Used for **temporal feature encoding**.

---

### 2. `MfccEncoder`

Simpler variant.
Computes MFCCs for one or more FFT sizes, resamples to target frame rate, normalizes, outputs MFCCs as z.
Used when temporal correlation is sufficient without RNN compression.

---

### 3. `MfccRnnEncoder`

Computes MFCCs then compresses over time using RNN.

**Modes**

* `mean_aggregate=True`: average hidden states → global z.
* `False`: concatenate final RNN states.

Used for **global timbre/style latents**.

---

### 4. `ExpressionEncoder`

Fuses multiple features (e.g., f0, loudness, MFCCs).
Optionally computes MFCCs from audio.
Processes concatenated features through neural net.
Pools in time if `pool_time=True` for a global latent.

Used for expressive, multi-feature conditioning.

---

## Feature-Based Encoders

### 5. `AggregateFeaturesEncoder`

Concatenates `f0_scaled` and `ld_scaled`, applies dense layer, averages over time.
Outputs global z representing pitch–loudness dynamics.

---

### 6. `OneHotEncoder`

Learns embeddings for categorical one-hot inputs (e.g., instrument ID).

**Params**

* `vocab_size`, `n_dims`, `skip_expand`.

If `skip_expand=True`, latent z is broadcast during synthesis.

---

## Specialized Encoders (Experimental)

### 7. `ResnetSinusoidalEncoder`

Maps raw audio directly to synthesizer parameters.
Workflow: log-mel spectrogram → ResNet → dense heads for outputs
(e.g., frequencies, amplitudes, noise magnitudes).

Used in `InverseSynthesis` models for **direct param prediction**.

---

### 8. `SinusoidalToHarmonicEncoder`

Converts sinusoidal parameters to harmonic synthesizer controls.

**Steps**

1. Scale sinusoids by Nyquist range.
2. Concatenate freqs and amps.
3. Pass through neural net.
4. Output harmonic amp, distribution, and f0.
5. Remove above-Nyquist harmonics and renormalize.

Used for **hierarchical harmonic modeling**.

---

## MIDI-Based Encoders

### 9. `MidiEncoder`

Encodes f0 and loudness into pitch (`z_pitch`) and velocity (`z_vel`).

**Process**

* Concatenate f0_midi + loudness.
* Neural net + normalization + Dense(2).
* Add f0 residual if `f0_residual=True`.

---

### 10. `HarmonicToMidiEncoder`

Same as `MidiEncoder` but operates on harmonic parameters
(f0_midi, amps, harmonic distribution, noise magnitudes).

Used in **MIDI Autoencoder** and **Z-MIDI Autoencoder**.

---

## Integration

Encoders are used between preprocessing and decoding in `Autoencoder` models:

```python
features = preprocessor(features)
features.update(encoder(features))
outputs = decoder(features)
```

Configured via Gin:

```python
models.Autoencoder.encoder = @encoders.MfccTimeDistributedRnnEncoder()
MfccTimeDistributedRnnEncoder.z_dims = 32
```

---

## Summary Table

| Encoder                         | Input                | Output          | Temporal         | Use                |
| ------------------------------- | -------------------- | --------------- | ---------------- | ------------------ |
| `ZEncoder`                      | any                  | z               | variable         | base               |
| `MfccTimeDistributedRnnEncoder` | audio                | z               | time-varying     | main audio encoder |
| `MfccEncoder`                   | audio                | z               | time-varying     | simple MFCC latent |
| `MfccRnnEncoder`                | audio                | z               | global           | timbre embedding   |
| `ExpressionEncoder`             | f0, loudness, audio  | z               | optional pooling | expressive         |
| `AggregateFeaturesEncoder`      | f0_scaled, ld_scaled | z               | global           | feature summary    |
| `OneHotEncoder`                 | categorical          | z               | broadcast/global | instrument ID      |
| `ResnetSinusoidalEncoder`       | audio                | synth params    | time-varying     | inverse synthesis  |
| `SinusoidalToHarmonicEncoder`   | sinusoid params      | harmonic params | time-varying     | hierarchical       |
| `MidiEncoder`                   | f0_midi, loudness    | z_pitch, z_vel  | time-varying     | MIDI Autoencoder   |
| `HarmonicToMidiEncoder`         | synth params         | z_pitch, z_vel  | time-varying     | Z-MIDI model       |

---

**References**

* File: `ddsp/training/encoders.py`
* Docs: `ddsp/training/README.md`
* DDSP Wiki §3.2
* Colab: `ddsp_colab/3_training.ipynb`

---
