# Overview

The **Data module** provides a unified framework for **loading, batching, and managing audio datasets** used in training **DDSP (Differentiable Digital Signal Processing)** models.
Core functionality revolves around the **`DataProvider`** base class and its concrete implementations for different data sources.

---
## Core Architecture

### `DataProvider` Base Class

The foundation for all DDSP data loaders.

**Properties**

* `sample_rate`: Audio sample rate (e.g., 16000 Hz)
* `frame_rate`: Feature frame rate (e.g., 250 Hz)

**Methods**

1. `get_dataset(shuffle)`
   → Returns a `tf.data.Dataset` of examples.
   
2. `get_batch(batch_size, shuffle, repeats, drop_remainder)`
   → Returns a batched and prefetched dataset for training.

**Batching Process**

* Calls `get_dataset()`
* Repeats dataset `repeats` times (`-1` for infinite)
* Batches and prefetches examples

---
## Main Provider Implementations

### 1. `TFRecordProvider`

Loads data from TFRecord files prepared with `ddsp_prepare_tfrecord`.

**Expected Features**

* `audio`: Raw waveform
* `audio_16k`: Resampled audio (for CREPE pitch detection)
* `f0_hz`: Fundamental frequency (Hz)
* `f0_confidence`: Pitch confidence
* `loudness_db`: Loudness in dB

**Example**

```python
data_provider = ddsp.training.data.TFRecordProvider(TRAIN_TFRECORD_FILEPATTERN)
dataset = data_provider.get_dataset(shuffle=False)
```

---
### 2. `NSynthTfds`

Loads **NSynth dataset** via TensorFlow Datasets and restructures it into DDSP’s feature format.

**Example**

```python
data_provider = data.NSynthTfds(split='test')
dataset = data_provider.get_batch(batch_size=1, shuffle=False)
```

**Feature Mapping**

* `audio` → raw waveform
* `f0_hz`, `f0_confidence`, `loudness_db` → extracted features
* Optionally includes note and instrument labels

---
### 3. Multi-Dataset Providers

Used to **combine multiple datasets** into one.

#### `ZippedProvider`

* Uses `tf.data.Dataset.zip()`
* Produces tuples of synchronized examples from each dataset.

#### `MixedProvider`

* Uses `tf.data.experimental.sample_from_datasets()`
* Randomly samples from datasets using specified weights.

**Batch Ratio Control**

* `batch_size_ratios`: defines the relative contribution of each dataset to the final batch.

---
## Specialized Providers

### `SyntheticNotes`

* Loads synthetic data created by `ddsp_generate_synthetic_data.py`.
* Contains harmonic and noise synthesis parameters.
* Used for **self-supervised or synthetic data experiments**.

### `Urmp`

* Loads URMP dataset TFRecords (musical instrument recordings with MIDI).
* Supports instrument-specific splits and file suffixes (`batched`, `unbatched`, etc.).
* Useful for **instrument-conditioned training**.

---
## Usage in Training

1. The training loop initializes a `data_provider`.
2. `data_provider.get_batch()` creates a batched `tf.data.Dataset`.
3. The trainer distributes the dataset across devices (multi-GPU setup).
4. An iterator feeds batches into the model.

**Code Example**

```python
dataset = data_provider.get_batch(batch_size, shuffle=True, repeats=-1)
dataset = trainer.distribute_dataset(dataset)
dataset_iter = iter(dataset)
```

---
## Dataset Statistics

The same provider is used for computing normalization stats via:

```python
compute_dataset_statistics(data_provider)
```

This function iterates through the dataset to compute loudness, power, and pitch distributions.

---
## Extensibility

You can define **custom data providers** by subclassing `DataProvider` and implementing:

```python
def get_dataset(self, shuffle):
    # Return a tf.data.Dataset
```

This enables integration of new datasets or input pipelines.

---
## Summary Table

| Provider Type      | Source                | Combines Multiple?      | Key Features                   |
| ------------------ | --------------------- | ----------------------- | ------------------------------ |
| `TFRecordProvider` | TFRecord files        | No                      | Standard audio + f0 + loudness |
| `NSynthTfds`       | TFDS NSynth           | No                      | Restructured NSynth data       |
| `ZippedProvider`   | Multiple providers    | Yes (zip)               | Parallel tuples of datasets    |
| `MixedProvider`    | Multiple providers    | Yes (weighted sampling) | Weighted mixing                |
| `SyntheticNotes`   | TFRecords (synthetic) | No                      | Harmonics, noise magnitudes    |
| `Urmp`             | TFRecords (URMP)      | No                      | MIDI + audio pairs             |

---
## References

* **File:** `ddsp/training/data.py`
* **Docs:** `ddsp/training/README.md`
* **Colab Demos:**

  * `train_autoencoder.ipynb`
  * `3_training.ipynb`

---
**Related Wiki Pages**

* [DDSP: Differentiable Digital Signal Processing](https://github.com/magenta/ddsp)
* [Data Preparation and Loading](https://github.com/magenta/ddsp/wiki#3.3)
* [Timbre Transfer Demo](https://github.com/magenta/ddsp/wiki#4.4)

---
