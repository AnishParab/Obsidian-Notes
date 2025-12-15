# Dataset
### NSynth Dataset
[Nsynth Dataset](https://www.tensorflow.org/datasets/catalog/nsynth)
[NSynth Google Dataset](https://magenta.withgoogle.com/datasets/nsynth)

### Maestro Dataset
[Maestro Dataset](https://www.kaggle.com/datasets/jackvial/themaestrodatasetv2)
[Maestro Google Dataset](https://magenta.withgoogle.com/datasets/maestro)

- NSynth and MAESTRO datasets, which are instrumental in training and evaluating models for music generation and transcription tasks.

---
# JUCE Framework

JUCE is an open-source, cross-platform C++ application framework designed for developing audio applications and plugins. It supports creating standalone software and plugins in formats like VST, AU, AAX, and LV2, and is widely used in the audio development community. 

---
# Digital Signal Processing (DSP)

Digital Signal Processing (DSP) involves converting real-world analog signals into digital form, analyzing and manipulating them using algorithms, and then converting them back to analog if necessary. This process enables various applications such as audio and speech processing, image and video compression, and telecommunications. 

---
# CREPE (Convolutional Representation for Pitch Estimation)

Description: CREPE is a deep learning-based pitch detection algorithm developed by researchers at Cornell University. It uses a convolutional neural network (CNN) to estimate the fundamental frequency (f₀) directly from audio waveforms.

Key Features:
Works on monophonic audio.
Robust to noise and various timbres.
Produces continuous pitch estimates in Hz.
Requires minimal pre-processing of the input audio.
Reference: CREPE on arXiv

---
# pYIN (Probabilistic YIN)

Description: pYIN is a probabilistic extension of the YIN algorithm for fundamental frequency estimation. It analyzes the autocorrelation function of audio signals and applies probabilistic modeling to improve robustness.

Key Features:
Provides confidence estimates for detected pitches.
Handles noisy and expressive musical signals better than the original YIN.
Can output multiple candidate pitches with probabilities.
Reference: pYIN IEEE Paper

---

