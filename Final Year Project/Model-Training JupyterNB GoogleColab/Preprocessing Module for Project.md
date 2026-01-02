## Purpose

Formats and normalizes raw audio features before neural network training. Handles f0, loudness, and power computation and scaling. Located in `ddsp/training/preprocessing.py`.

---
## Core Design

All preprocessors inherit from `nn.DictLayer`.
Input: dictionary with keys like `audio`, `f0_hz`, `loudness_db`.
Output: same dictionary plus normalized features.
Used at the start of the DDSP model pipeline (`Autoencoder.encode()`).

---
## 1. `F0LoudnessPreprocessor`

Standard preprocessor for f0 and loudness.

**Params**

* `time_steps`: default 1000
* `frame_rate`: default 250
* `sample_rate`: default 16000
* `compute_loudness`: bool

**Process**

1. Optionally computes loudness via `ddsp.spectral_ops.compute_loudness()`.
2. Resamples f0 and loudness to uniform `time_steps`.
3. Normalizes both to [0, 1]:

   * f0 scaled via MIDI mapping (`scale_f0_hz`)
   * loudness scaled from [-DB_RANGE, 0] (`scale_db`)

**Outputs**

* `f0_hz`, `loudness_db`, `f0_scaled`, `ld_scaled`

---
## 2. `F0PowerPreprocessor`

Extends previous class; replaces loudness with power.

**Extra Param**

* `frame_size`: default 64

**Process**

* Computes or loads `power_db` using `compute_power()`.
* Scales to [0, 1] using `scale_db`.

**Outputs**

* `f0_hz`, `pw_db`, `f0_scaled`, `pw_scaled`

---
## 3. `OnlineF0PowerPreprocessor`

Performs full online feature extraction, compatible with real-time systems and VST plugins.

**Params**

* `frame_rate` (default 250)
* `frame_size` (default 1024)
* `padding`: `'center'` or `'same'`
* `compute_power`, `compute_f0`: booleans
* `crepe_saved_model_path`: CREPE checkpoint or preset size
* `viterbi`: smoothing toggle

**Process**

1. Runs at 16 kHz (CREPE requirement).
2. Computes power with `compute_power()` if enabled.
3. Computes f0 + confidence using frozen CREPE.
4. Stops gradients.
5. Scales outputs.
6. Checks shape consistency.

**Outputs**

* `f0_hz`, `pw_db`, `f0_scaled`, `pw_scaled`, `f0_confidence`

---
## 4. Scaling Utilities

Used across models and inference scripts.

| Function            | Operation               |
| ------------------- | ----------------------- |
| `scale_db()`        | [-DB_RANGE, 0] → [0, 1] |
| `inv_scale_db()`    | Inverse                 |
| `scale_f0_hz()`     | Hz → MIDI [0, 1]        |
| `inv_scale_f0_hz()` | Inverse                 |

---
## Integration with Models

Example configuration:

```python
models.Autoencoder.preprocessor = @preprocessing.F0LoudnessPreprocessor()
preprocessing.F0LoudnessPreprocessor.time_steps = 1000
```

Used automatically during `encode()`:

```python
features.update(self.preprocessor(features))
```

---
## Summary Table

| Preprocessor                | Features     | On-the-fly Computation | Output Keys                                       | Typical Use    |
| --------------------------- | ------------ | ---------------------- | ------------------------------------------------- | -------------- |
| `F0LoudnessPreprocessor`    | f0, loudness | Loudness optional      | f0_hz, loudness_db, f0_scaled, ld_scaled          | Training       |
| `F0PowerPreprocessor`       | f0, power    | Power optional         | f0_hz, pw_db, f0_scaled, pw_scaled                | Training       |
| `OnlineF0PowerPreprocessor` | f0, power    | Yes                    | f0_hz, pw_db, f0_scaled, pw_scaled, f0_confidence | Realtime / VST |

---
## Notes

* Proper scaling stabilizes training and convergence.
* CREPE-based extraction runs at fixed 16 kHz.
* Each preprocessor includes `invert_scaling()` for reconstructing Hz and dB values.

**References**
Files: `ddsp/training/preprocessing.py`, `ddsp/training/gin/models/vst/`, `ddsp/colab/tutorials/3_training.ipynb`
Docs: `ddsp/training/README.md`, DDSP Wiki §3.1

---
