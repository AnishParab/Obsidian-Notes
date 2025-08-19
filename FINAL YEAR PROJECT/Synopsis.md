# Introduction

---
## Introduction of Project

This project explores a novel approach to **neural audio synthesis**, where any **monophonic input audio**—such as a vocal recording or a solo instrument—can be transformed into the **timbre of a target instrument**. The system is designed to offer both **interpretability** and **control** by combining traditional digital signal processing (DSP) techniques with modern deep learning methods. At its core, the project implements a modular synthesis pipeline that reconstructs audio using **differentiable DSP components**.

Initially, a basic monophonic-to-instrument conversion system will be built using **harmonic additive synthesis** and **filtered noise synthesis**. On top of this foundation, the system will be extended to support **richer synthesis models** by integrating:
- **Wavetable synthesis** with learnable or modulated wavetable positions.

These DSP modules will be implemented using the **JUCE framework in C++**, ensuring real-time audio performance and low-latency processing. Crucially, the entire signal chain is kept **differentiable**, allowing neural networks to optimize not just the synthesis parameters, but the entire audio generation pipeline end-to-end.

This enhanced architecture enables more **expressive**, **controllable**, and **interpretable** audio synthesis, supporting applications such as:
- **Timbre transfer**
- **Real-time music production tools**
- **Creative sound design**
- **Data-efficient music generation models**

By expanding the traditional synthesis palette with advanced DSP methods and neural control, this project aims to bridge the gap between classic audio engineering and modern machine learning in an efficient and musically meaningful way.

---
## Advantages of Project

- **Expanded Synthesis Capabilities**  
    The integration of **wavetable synthesis** dramatically broadens the timbral range beyond the original harmonic-plus-noise paradigm. This allows generation of **evolving textures**, **realistic instrument emulations**, and **nonlinear articulations**, suited for both sound design and expressive music production.
    
- **Fine-Grained, Interpretable Parameter Control**  
    Unlike end-to-end black-box models, the enhanced DSP modules expose **explicit, meaningful parameters**—such as _wavetable index_, _grain overlap_. These make the system **interpretable**, **tunable**, and **controllable by external models or users**, encouraging experimentation and targeted audio sculpting.
    
- **Real-Time, Low-Latency Audio Processing**  
    Built in **JUCE using C++**, the system is optimized for **sample-accurate, real-time performance**. This makes it ideal for **live use**, **plugin integration (VST3/AU)**, and **interactive musical systems**, enabling neural synthesis without compromising responsiveness.
    
- **Cross-Platform & DAW-Compatible Architecture**  
    JUCE provides native support for **Windows**, **macOS**, **Linux**, **iOS**, and **Android**, along with seamless deployment as audio plugins. This ensures that the enhanced DDSP engine is **portable and integrable** across **DAWs** (e.g., Ableton, Logic, FL Studio), mobile music apps, and custom DSP tools.
    
- **Hybrid Neural-DSP Design with Differentiability**  
    All added DSP modules are designed to be **differentiable**, retaining compatibility with spectrogram-based training losses and neural parameter inference. This allows **deep learning models to control synthesis parameters** end-to-end, merging neural flexibility with DSP transparency.
    
- **System Efficiency & Hardware Readiness**  
    By delegating synthesis to **optimized DSP blocks** instead of deep decoder networks, the system achieves **lower CPU/GPU overhead**, making it viable on **resource-constrained environments** like embedded systems or mobile processors.
    
- **Scalable and Modular Architecture**  
    The modular design facilitates **future extension**, whether adding new synthesis engines, loss functions, or real-time modulation systems. It also supports **community collaboration** and **integration into larger system architectures**, such as generative music pipelines or AI-assisted composition tools.

---
# Literature Study

## Analysis of Papers
- This literature study analyzes key papers related to Google Magenta’s Differentiable Digital Signal Processing (DDSP) and its proposed enhancement with new DSP modules (wavetable) implemented in the JUCE framework. The focus is on understanding the foundational DDSP framework, its strengths, limitations, and how recent advancements in audio synthesis and JUCE-based processing can inform the proposed improvements.

### Foundational Paper: DDSP: Differentiable Digital Signal Processing

- **Citation**: Engel, J., Hantrakul, L., Gu, C., & Roberts, A. (2020). _DDSP: Differentiable Digital Signal Processing_. International Conference on Learning Representations (ICLR). [https://openreview.net/forum?id=B1x1ma4tDr](https://openreview.net/forum?id=B1x1ma4tDr)
- **Key Contributions**:
    - Introduces DDSP, combining interpretable DSP components (harmonic additive synthesizer, filtered noise synthesizer, reverb) with neural networks for audio synthesis.
    - Demonstrates high-fidelity audio generation using a small dataset (13 minutes of audio), leveraging differentiable DSP modules trained end-to-end with multi-scale spectrogram loss.
    - Shows applications like timbre transfer (e.g., violin to flute, voice to violin) and blind dereverberation, with interpretable control over synthesis parameters.
    - Achieves efficiency by reducing model parameters compared to neural-only models like WaveNet, enabling high-quality synthesis on modest hardware.
- **Strengths**:
    - Interpretability: DSP components allow users to inspect and modify parameters (e.g., harmonic amplitudes), unlike black-box neural models.
    - Efficiency: Requires fewer parameters and less training data, suitable for real-time applications.
    - Modularity: Flexible architecture supports custom DSP components and external pitch inputs.
- **Limitations**:
    - Limited to monophonic audio, struggling with polyphonic or complex multi-instrument sounds.
    - Challenges in modeling transients (e.g., percussive attacks), as the harmonic-plus-noise model oversimplifies non-harmonic components.
    - Relies on CREPE for pitch detection, which is computationally intensive and less effective for polyphonic or noisy audio.
    - Implementation in Python/TensorFlow limits real-time performance on resource-constrained devices.

### Related Work: Neural Audio Synthesis and DSP Enhancements

- **Paper**: Hantrakul, L., Engel, J., Roberts, A., & Gu, C. (2020). _Self-Supervised Pitch Detection by Inverse Audio Synthesis_. ICML Workshop on Self-supervision in Audio and Speech. [https://arxiv.org/abs/2007.08775](https://arxiv.org/abs/2007.08775)
    
    - **Contributions**: Introduces a self-supervised pitch detection method for DDSP, improving robustness to data scarcity and reducing reliance on labeled datasets like CREPE’s.
    - **Strengths**: Enhances DDSP’s flexibility by enabling pitch estimation without extensive annotations, supporting diverse audio inputs.
    - **Limitations**: Limited evaluation on complex audio; performance in polyphonic settings unclear.
	
- **Paper**: Kim, J. W., et al. (2019). _CREPE: A Convolutional Representation for Pitch Estimation_. [https://arxiv.org/abs/1802.06182](https://arxiv.org/abs/1802.06182)
    
    - **Contributions**: Introduces CREPE, a convolutional neural network for monophonic pitch estimation, used in DDSP for f0 extraction.
    - **Strengths**: High accuracy for monophonic audio, robust to noise compared to traditional methods like pYIN.
    - **Limitations**: Computationally intensive, less effective for polyphonic audio, and requires 16kHz input, limiting versatility.

### JUCE and Real-Time Audio Processing

- **Reference**: JUCE Framework Documentation. [https://docs.juce.com/master/](https://docs.juce.com/master/)
    
    - **Contributions**: JUCE provides a C++ framework for high-performance audio processing, with classes like `dsp::Oscillator`, `dsp::ProcessorChain`, and `AudioBuffer` for building DSP modules.
    - **Strengths**: Optimized for real-time audio, supports VST/AU plugins, and is cross-platform, aligning with DDSP’s real-time goals.

    - **Limitations**: Not inherently differentiable, requiring custom gradient implementations for DDSP compatibility.
	
- **Paper**: Reiss, J. D., & McPherson, A. (2014). _Audio Effects: Theory, Implementation and Application_. CRC Press.
    
    - **Contributions**: Provides a comprehensive overview of DSP techniques (e.g., wavetable, granular, physical modeling) implementable in C++, relevant for JUCE-based enhancements.
    - **Strengths**: Offers practical algorithms for new DSP modules, with focus on real-time processing.
    - **Limitations**: Lacks differentiability discussion, requiring adaptation for DDSP’s training pipeline.
    - **Relevance**: Guides the implementation of new DSP modules in JUCE, ensuring they are efficient and align with DDSP’s interpretable design.

### Enhanced DDSP Models and Deployment

- **DDSP-VST: Neural Audio Synthesis with Differentiable DSP in Real-Time Plugins** (Hantrakul et al., 2022)
    
    - _Overview_: Adapted the original DDSP framework for integration as a VST plugin using JUCE, facilitating real-time neural audio synthesis within digital audio workstations (DAWs).
        
    - _Strengths_: Enables realtime, low-latency synthesis and practical deployment for musical applications.
        
    - _Limitations_: The model primarily remains monophonic and faces practical constraints as a plugin.
        
- **DDSP-J: Differentiable DSP with JAX for Ultrafast Neural Audio Synthesis** (Hantrakul et al., 2022)
    
    - _Overview_: Ported DDSP to JAX, resulting in significant speed improvements (>10×) for both training and inference.
        
    - _Strengths_: Makes rapid experimentation possible and supports modern hardware acceleration.
        
    - _Limitations_: Core model architecture remains limited in polyphonic and transient synthesis.
        

### Polyphonic and Transient-Enhanced Models

- **Polyphonic DDSP: Neural Synthesizer for Multiple Notes** (Yang et al., 2022)
    - _Overview_: Expands DDSP to handle polyphonic music by modeling separate parameter tracks for multiple notes or voices.
    - _Strengths_: Overcomes the monophonic limitation of classic DDSP.
    - _Limitations_: Accurate note separation increases computational demands and complexity.
        
- **TransienDDSP: Improved Neural Audio Synthesis with Transient Modeling** (Cao et al., 2023)
    - _Overview_: Integrates a dedicated transient module alongside the harmonic-plus-noise model, enhancing synthesis of percussive attacks.
    - _Strengths_: Produces more realistic percussive and transient sounds.
    - _Limitations_: Introduces additional model complexity.

---
## Algorithms/Technology Used
### Core Algorithms
The foundational algorithms in DDSP are centered around differentiable DSP components, which allow for end-to-end training with neural networks. These components are detailed as follows:
1. **Harmonic Additive Synthesizer**:
    - **Description**: This algorithm generates audio by summing sinusoidal harmonics, each with controllable amplitudes and frequencies. It is based on the principle of additive synthesis, where the audio signal is reconstructed by adding together multiple sine waves at harmonic frequencies relative to a fundamental frequency (f0).
    - **Implementation**: Utilizes oscillator banks to generate harmonics, ensuring that frequencies are constrained below the Nyquist frequency to avoid aliasing. For example, at a sample rate of 16 kHz, with a Nyquist frequency of 8 kHz, only 18 harmonics are typically nonzero for a 440 Hz fundamental (18*440=7920 Hz), and amplitudes are logarithmically scaled and normalized to sum to 1.0.
    - **Role**: Provides the tonal, harmonic structure of the synthesized audio, essential for mimicking pitched instruments.
2. **Filtered Noise Synthesizer**:
    - **Description**: Generates non-harmonic, stochastic components by filtering white noise with time-varying bandpass filters. This is crucial for capturing elements like breathiness or noise in instruments, which are not adequately represented by harmonics alone.
    - **Implementation**: Employs time-varying filter envelopes to control the frequency and Q-factor of the bandpass filters, with amplitudes scaled to ensure realistic noise characteristics.
    - **Role**: Enhances the realism of synthesized audio by adding stochastic, non-pitch-related components.
3. **Reverb**:
    - **Description**: Simulates room acoustics by adding reverberation effects, which model how sound reflects in a physical space. DDSP offers two parameterizations for reverb, allowing flexibility in modeling different acoustic environments.
	- **Implementation**: Likely uses variable-length delay modulation and time-varying filters to create the reverb effect, ensuring differentiability for integration with neural training.
    - **Role**: Adds spatial depth and realism, enabling applications like blind dereverberation and transfer of room acoustics to new environments.

### Neural Network Integration
DDSP leverages neural networks to predict control parameters for the DSP components, enhancing adaptability and expressivity. The typical architecture includes:
- **Network Types**: Recurrent neural networks (RNNs) like LSTMs or feedforward networks, which process input features such as fundamental frequency (f0) and loudness to generate control signals.
- **Functionality**: These networks convert user inputs (e.g., control signals, audio features) into complex DSP controls, such as harmonic amplitudes, filter coefficients, and reverb parameters. This allows for dynamic adjustment during synthesis, enabling applications like independent control of pitch and loudness.

### Pitch Detection
- **CREPE (Convolutional Representation for Pitch Estimation)**: DDSP uses CREPE for extracting the fundamental frequency (f0) from input audio. CREPE is a convolutional neural network-based pitch detection algorithm, known for its robustness with monophonic audio and resistance to noise compared to traditional methods like pYIN. It requires a 16 kHz input, which aligns with DDSP's audio processing requirements.

### Training Methodology
The training process is designed for efficiency and accuracy, utilizing:
- **Multi-Scale Spectrogram Loss**: This loss function compares the magnitude spectrograms of generated and target audio across multiple frame sizes (e.g., 64, 128, 256, 512, 1024, 2048 samples). This multi-scale approach ensures that the synthesized audio matches the target at various time-frequency resolutions, enhancing fidelity. The loss is computed using Fourier transforms, likely implemented via TensorFlow's spectral operations.
- **Training Efficiency**: DDSP models can be trained on as little as 13 minutes of audio, demonstrating significant data efficiency compared to neural-only models like WaveNet, which often require extensive datasets.

### Supporting Technologies
DDSP's implementation relies on several key technologies to ensure functionality and performance:
- **TensorFlow**: The primary framework for building and training the deep learning models, providing the necessary tools for backpropagation and gradient computation. DDSP's differentiable DSP modules are integrated as TensorFlow layers, enabling seamless end-to-end training.
- **Gin Configuration**: Utilizes the Gin library for managing hyperparameters and configuring the signal processing chain. This allows for flexible setup, with configurations specified in .gin files, such as defining the ProcessorGroup as a Directed Acyclic Graph (DAG). For example, the oscillator_bank.use_angular_cumsum parameter can be globally configured for slower but more accurate algorithms.

### Why Not Use GanSynth
**GanSynth** is a GAN-based model for generating raw audio waveforms directly from latent codes. While it's powerful for synthesis, it does not align with the goals of this project for the following reasons:
1. **Lack of Interpretability and Control**  
    GanSynth generates audio from high-dimensional latent vectors that do not correspond to musically meaningful parameters like f₀, timbre, or loudness. This black-box nature makes it unsuitable for tasks requiring fine-grained, user-controllable synthesis.
2. **Not Modular or Differentiable at Component Level**  
    The system generates end-to-end waveforms using deep generative networks. It cannot integrate traditional DSP modules (like harmonic additive synthesis, filtered noise, or reverb) in a differentiable, modular manner.
3. **Resource-Intensive and Non-Real-Time**  
    GAN models require high computational resources for both training and inference. Real-time audio applications, as targeted in this project via the JUCE framework, are incompatible with the latency and performance characteristics of GanSynth.

### Why Not Use WaeNet
**WaeNet** is a waveform autoencoding network that reconstructs audio using learned features like f₀, loudness, and a latent timbre vector. It aligns better with this project's goals but still has limitations when used directly:
1. **Decoder is Fully Neural, Not DSP-Inspired**  
    WaeNet's decoder directly generates waveforms using neural networks. This bypasses the opportunity to use structured, interpretable synthesis models like harmonic + filtered noise + wavetable synthesis, which are central to this project.
2. **Limited Physical Interpretability in Generation**  
    Although WaeNet extracts controllable parameters during encoding, the synthesis step still lacks physical modeling or perceptual transparency, which are critical for timbre transfer and expressive sound design.
3. **Harder to Extend with Richer Synthesis Models**  
    Incorporating physical modeling (e.g., Karplus-Strong), granular synthesis, or other real-time DSP modules would require significant restructuring of WaeNet’s neural decoder. A custom architecture provides more flexibility and modularity.

---
# Proposed Idea
This project proposes a **hybrid neural-DSP audio synthesis system** that integrates **harmonic additive synthesis**, **filtered noise synthesis**, and **wavetable synthesis**, driven by neural network control implemented using **TensorFlow (Bazel) Python** for neural components and **JUCE/C++** for DSP modules. The system ensures end-to-end differentiability, delivering high-fidelity, real-time audio synthesis for music production, sound design, and research applications.

## Approaches to Project
The project adopts a modular, hybrid approach combining interpretable DSP techniques with neural network control to achieve expressive, high-quality audio synthesis. The architecture is designed for real-time performance, extensibility, and end-to-end differentiability to enable seamless training and optimization.
- **Input Analysis & Feature Extraction**: Processes monophonic audio input (e.g., solo instruments or vocals) using a neural encoder implemented in TensorFlow (Bazel) Python to extract fundamental frequency (f₀), loudness, and a timbral latent vector (z) capturing instrument-specific characteristics.
- **Neural Control Parameter Prediction**: A TensorFlow-based neural decoder maps extracted features to time-varying control parameters for DSP modules, including harmonic amplitudes, noise filter coefficients, and wavetable indices.
- **DSP Synthesis Modules**:
    - **Harmonic Additive Synthesizer**: Generates tonal components by summing sinusoidal harmonics, with frequencies as integer multiples of f₀, constrained below the Nyquist frequency to prevent aliasing.
    - **Filtered Noise Synthesizer**: Produces stochastic, non-harmonic components (e.g., breathiness, percussive attacks) by applying time-varying bandpass filters to white noise, with neural control over filter parameters.
    - **Wavetable Synthesizer**: Uses a bank of predefined or neurally learned wavetables to generate evolving timbres, with neural control over wavetable selection and interpolation.
- **Signal Mixing & Post-Processing**: Combines outputs from the synthesis modules with neural-controlled mixing proportions, followed by a differentiable reverb module for spatial effects.
- **Output Audio**: Produces high-fidelity synthesized audio for real-time playback or further processing.


- **JUCE/C++ Framework**: DSP modules (harmonic additive, filtered noise, wavetable, and reverb) are implemented in JUCE/C++ with differentiable signal processing routines, ensuring low-latency, real-time performance.
- **TensorFlow (Bazel) Python**: Neural components (encoder and decoder) are built using TensorFlow with Bazel for efficient model development, training, and deployment, maintaining end-to-end differentiability for optimization.
- **Modularity**: The system is designed for extensibility, supporting additional DSP modules or future polyphonic capabilities.
- **Interoperability**: TensorFlow models are integrated with JUCE/C++ via serialized model weights or real-time inference pipelines, ensuring seamless neural-DSP interaction.

## Proposed Solutions
The system addresses key challenges in audio synthesis by combining traditional DSP with neural control, offering solutions for timbre modeling, real-time performance, and extensibility.
- **High-Fidelity Timbre Modeling**:
    - Harmonic additive synthesis ensures accurate reproduction of pitched, tonal components by summing sinusoids, constrained to avoid aliasing.
    - Filtered noise synthesis captures stochastic elements like breathiness or percussive attacks, with neural control over bandpass filter parameters.
    - Wavetable synthesis expands the timbre palette by using flexible, neurally controlled wavetables, enabling complex and evolving sounds.
- **Real-Time Performance**:
    - JUCE/C++ optimizes DSP modules for low-latency processing, suitable for live music production or interactive applications.
    - TensorFlow (Bazel) Python enables efficient neural network inference, with optimized model architectures for real-time performance on standard hardware.
- **Interpretable Control**:
    - Neural decoder provides explicit control over synthesis parameters, allowing users to manipulate pitch, loudness, and timbre intuitively.
    - End-to-end differentiability enables fine-tuning of synthesis parameters via gradient-based optimization, improving target timbre matching.
- **Extensibility**:
    - Modular design supports integration of additional synthesis techniques (e.g., granular synthesis) or effects (e.g., distortion, chorus).
    - Future-proofed for polyphonic synthesis by allowing multi-note inputs and layered synthesis processes.

## Proposed Algorithms
The following algorithms form the core of the synthesis system, implemented with end-to-end differentiability using TensorFlow (Bazel) Python for neural components and JUCE/C++ for DSP modules.
- **Feature Extraction Algorithm**:
    - **Input**: Monophonic audio (16-bit PCM, 16 kHz sample rate).
    - **Process**: A TensorFlow-based convolutional neural network (CNN) or transformer encoder extracts:
        - Fundamental frequency (f₀) using a differentiable pitch detection algorithm (e.g., CREPE adapted for TensorFlow).
        - Loudness via root-mean-square (RMS) energy analysis.
        - Timbral latent vector (z) using a learned embedding space to capture instrument-specific features.
    - **Output**: Time-varying feature vectors [f₀, loudness, z].
- **Neural Parameter Prediction Algorithm**:
    - **Input**: Feature vectors `[f₀, loudness, z]`
	- **Process**: A TensorFlow-based recurrent or transformer decoder predicts:
    - **Harmonic amplitudes**
        - Vector of normalized (log) harmonic magnitudes, summing to 1.0.
    - **Noise filter parameters**
        - Time-varying **center frequency**, **Q-factor**, and **amplitude** for each bandpass filter.
    - **Optional: Spectral morphing parameters**
        - Scalar controls (e.g., brightness, sharpness) used to **modulate timbre** over time — could affect **wavetable morph position**, but **not indices**.
	- **Output**:
	    - `[harmonic_amplitudes, filter_params, timbre_mod_params]`
### **1. Harmonic Additive Synthesis**

- **Input**:
    
    - Predicted **fundamental frequency** (f₀)
        
    - **Harmonic amplitudes** from the neural decoder
        
- **Process**:
    
    - Produces the tonal component of the sound using the predicted harmonic structure
        
- **Output**:
    
    - `harm_signal(t)`: the tonal signal based on f₀ and its harmonics
        

---

### **2. Filtered Noise Synthesis**

- **Input**:
    
    - **Noise shaping parameters** (center frequency, Q-factor, amplitude) predicted by the neural decoder
        
- **Process**:
    
    - Shapes noise to represent the non-tonal or stochastic component of the sound
        
- **Output**:
    
    - `noise_signal(t)`: colored/stochastic audio component
### **3. Wavetable Synthesis**

- **Input**:
    
    - **Fixed or learned wavetables**
        
    - **Timbral modulation parameters** (derived from the decoder or latent space)
        
- **Process**:
    
    - Uses scalar controls to morph and modulate predefined wavetables over time
        
    - Responds dynamically to expressive inputs such as brightness or articulation
        
- **Output**:
    
    - `wavetable_signal(t)`: expressive timbral layer
### **4. Mixing and Reverb**

- **Input**:
    
    - Synthesized signals:
        
        - `harm_signal(t)`
            
        - `noise_signal(t)`
            
        - `wavetable_signal(t)`
            
    - Decoder-predicted:
        
        - **Mixing weights**
            
        - **Reverb parameters**
            
- **Process**:
    
    - Balances all components through a weighted mix
        
    - Applies differentiable reverb for spatialization and realism
        
- **Output**:
    
    - `final_audio(t)`: unified and post-processed synthesized sound
---
# Requirement Specification
