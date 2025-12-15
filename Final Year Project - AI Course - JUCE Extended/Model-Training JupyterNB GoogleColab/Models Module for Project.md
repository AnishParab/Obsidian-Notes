## Purpose

Implements full neural network architectures for audio reconstruction and synthesis using differentiable signal processing.
Located in `ddsp/training/models/`. Each model defines the **forward pass**, **losses**, and **audio synthesis** logic.

---
## 1. Base Model (`Model`)

Extends `tf.keras.Model`.
Core features:

* Tracks losses in `_losses_dict`.
* Allows selective checkpoint restoration with `restore()`.
* Supports `return_losses=True` for training.

Usage:

```python
outputs, losses = model(batch, return_losses=True)
```

---
## 2. Autoencoder

Standard DDSP architecture.

**Modules**

* `preprocessor`: Extracts features (f0, loudness).
* `encoder`: Produces latent code.
* `decoder`: Predicts synthesis parameters.
* `processor_group`: Synthesizes waveform.
* `loss_objs`: Computes reconstruction losses.

**Flow**

```
audio → features → encode → decode → synthesize → losses
```

Stable and used in most experiments (`nsynth_ae.gin`, `solo_instrument.gin`).

---
## 3. MidiAutoencoder

Adds a **MIDI-style latent layer**. Two stacked autoencoders:

**Inner branch**:
Audio → CREPE → SynthCoder → DDSP Synth → Reconstruction

**Outer branch**:
SynthCoder output → MidiEncoder → MidiDecoder → DDSP Synth → Reconstruction

Includes:

* MIDI quantization losses
* Optional reverb
* Conversion utilities:
  `pianoroll_to_midi()` and `midi_to_pianoroll()`

---
## 4. ZMidiAutoencoder

Extends `MidiAutoencoder`.
Adds latent encoders for multi-level control:

* `z_synth_encoders`
* `z_global_encoders`
* `z_note_encoder`
  Supports priors on latent variables.

---
## 5. InverseSynthesis (DDSP-INV)

Experimental.
Learns hierarchical sinusoidal and harmonic representations for self-supervised learning.

---
## 6. Configuration and Integration

All models are **Gin-configurable**:

```python
model = models.get_model()  # Loaded via Gin
```

Used by `ddsp_run.py` for train/eval/sample pipelines.

Unit tests (`autoencoder_test.py`) confirm correct audio output shape.

---
## Summary Table

| Model              | Purpose                 | Stable?      | Key Feature                    |
| ------------------ | ----------------------- | ------------ | ------------------------------ |
| `Model`            | Base class              | Yes          | Loss and checkpoint management |
| `Autoencoder`      | Core DDSP model         | Yes          | Audio reconstruction           |
| `MidiAutoencoder`  | Adds MIDI latent layer  | Experimental | MIDI-style quantization        |
| `ZMidiAutoencoder` | Adds latent control     | Experimental | Multi-level latent encoding    |
| `InverseSynthesis` | Hierarchical DDSP model | Experimental | Sinusoidal hierarchy           |

---
## References

Files:

* `ddsp/training/models/model.py`
* `ddsp/training/models/autoencoder.py`
* `ddsp/training/models/midi_autoencoder.py`
* `ddsp/training/models/inverse_synthesis.py`
* `ddsp/training/models/__init__.py`

Docs:

* `ddsp/training/README.md`
* DDSP Wiki: [Models Section](https://github.com/magenta/ddsp/wiki#3.2)

---
