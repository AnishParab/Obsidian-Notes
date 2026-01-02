## **Design Methodology**

DDSP is built on **TensorFlow 2.x** with a modular design that separates neural control from audio synthesis. Each module has a clear responsibility:

---
### **1. Core DSP Modules**

* **`core`**: Basic DSP functions like oscillators, filters, and envelopes. These are differentiable, so gradients can flow during training.
* **`processors`**: Base classes (`Processor` and `ProcessorGroup`) that manage how DSP modules use neural network outputs, ensuring valid amplitudes and frequencies.
* **`synths`**: Audio generators, e.g., harmonic additive and filtered noise synthesizers, that turn neural control signals into sound.
* **`effects`**: Audio effects like reverb, delay, or distortion, controllable by neural networks.
* **`losses`**: Audio-specific loss functions, e.g., multi-scale spectral loss, to measure how close generated audio is to target audio.
* **`spectral_ops`**: Functions for spectral analysis and Fourier transforms, used in synthesis and loss calculations.

---
### **2. Training Modules**

* **Data Providers**: Load and prepare datasets (NSynth, Maestro) for training. Handles batching and shuffling.
* **Encoders**: Convert input audio into latent features that capture pitch, loudness, and timbre.
* **Decoders**: Convert latent features back into DSP control parameters like harmonic amplitudes or filter settings.
* **Models**: Combine encoders, decoders, and DSP modules for end-to-end training.
* **Training Utilities**: Tools for training like learning rate scheduling, checkpoints, and evaluation.

---
### **3. Processor Framework**

* **Processor**: Converts neural outputs into meaningful DSP parameters and audio. Reusable across modules.
* **ProcessorGroup**: Combines multiple processors in a **DAG**, defining signal flow and allowing flexible module combinations without changing code.

---
### **3. Processor Framework**

- **Processor**: Core abstraction that converts neural outputs into physically meaningful control parameters and then into audio. Supports modular re-use.
- **ProcessorGroup**: Aggregates multiple processors in a **Directed Acyclic Graph (DAG)**, defining the signal flow. Supports configurable combinations of synthesis and effects modules without changing code.

---
### **Design Advantages**
1. **Interpretability**: Each DSP module has explicit, controllable parameters (e.g., harmonic amplitude, filter cutoff).
2. **Modularity**: Core, training, and processor modules can be extended or replaced independently.
3. **Real-Time Performance**: Optimized to run efficiently on a minimum GPU of **NVIDIA GeForce RTX 3050**.
- TensorFlow 2.x GPU Requirements:
Real-time audio generation requires low-latency computation of control parameters at audio buffer rates (typically 128–512 samples per buffer).
NVIDIA RTX 3050 and above support CUDA cores and Tensor Cores, enabling fast parallel computation
RTX 3050 has 8GB VRAM, enough to load neural models (e.g., harmonic + noise + wavetable synthesis) and process audio in real-time without swapping.

---


