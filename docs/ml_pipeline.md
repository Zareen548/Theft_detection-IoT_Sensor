# Machine Learning Pipeline

## Overview

The theft detection system uses a lightweight **Autoencoder** neural network to identify abnormal sensor behavior directly on the ESP32 microcontroller. Instead of relying on manually tuned rules alone, the model learns the normal operating characteristics of the sensor node and flags deviations as potential anomalies.

The trained model was converted to **TensorFlow Lite for Microcontrollers (TFLite Micro)**, enabling real-time inference on resource-constrained embedded hardware.

---

# Why Machine Learning?

Environmental sensors naturally experience small movements caused by:

- Wind
- Rain
- Tree vibrations
- Installation tolerances
- Sensor noise

Simple threshold-based approaches often generate false alarms because these normal variations may resemble suspicious activity.

Machine learning enables the system to learn normal behavior automatically and distinguish it from genuine theft or tampering attempts.

---

# Why an Autoencoder?

An Autoencoder is an unsupervised neural network designed to reconstruct its input.

During training, the model only learns **normal operating conditions**. Since it has never seen anomalous events, it struggles to reconstruct abnormal inputs, producing a larger reconstruction error.

This makes Autoencoders well suited for embedded anomaly detection, especially when abnormal events are rare or difficult to collect.

---

# Feature Engineering

Raw accelerometer readings were not directly used as model inputs.

Instead, statistical features were extracted to reduce noise and better represent the motion characteristics of the device.

The extracted features included:

- Mean
- Median
- Median Absolute Deviation (MAD)

Among these, **Median Absolute Deviation (MAD)** proved to be the most robust feature for distinguishing normal environmental motion from suspicious handling.

---

# Detection Pipeline

```
Accelerometer Data
        │
        ▼
Feature Extraction
        │
        ▼
Median Absolute Deviation (MAD)
        │
        ▼
Autoencoder Inference
        │
        ▼
Reconstructed Features
        │
        ▼
Mean Squared Error (MSE)
        │
        ▼
Threshold Comparison
        │
        ▼
Normal / Anomaly
```

---

# Reconstruction Error

After inference, the Autoencoder generates a reconstructed version of the input feature vector.

The similarity between the input and reconstructed output is measured using **Mean Squared Error (MSE)**.

- Low MSE → Normal operating condition
- High MSE → Abnormal or suspicious activity

The reconstruction error serves as the anomaly score for the system.

---

# Sensor Fusion

To improve robustness, the system combines machine learning predictions with measurements from an ultrasonic distance sensor.

An alarm is triggered only when both conditions are satisfied:

- The reconstruction error exceeds the learned threshold.
- The measured distance falls below the predefined distance threshold.

This combination helps reduce false positives caused by environmental movement alone.

---

# TinyML Deployment

After training, the Autoencoder model was optimized for embedded deployment by:

1. Training the network using normal sensor data.
2. Converting the trained model to TensorFlow Lite format.
3. Embedding the model into the ESP32 firmware.
4. Running inference locally without cloud connectivity.

This allows the system to perform real-time anomaly detection directly on the microcontroller with low computational overhead.

---

# Advantages of the Approach

- Real-time edge inference
- No cloud dependency
- Low memory footprint
- Low computational cost
- Reduced false alarms
- Suitable for battery-powered IoT devices
- Easily adaptable to other monitoring applications

---

# Potential Improvements

Future enhancements may include:

- More advanced feature extraction techniques
- Sensor fusion with additional sensors (e.g., PIR or camera)
- Adaptive thresholds based on environmental conditions
- Quantized neural network models for lower memory usage
- Wireless notification through LoRaWAN or MQTT
- Cloud-based event logging and visualization

---

# Repository Note

This repository documents the machine learning workflow used in the project.

To protect academic work and implementation details, the following items are intentionally excluded:

- Training scripts
- Model architecture source code
- TensorFlow Lite model
- Experimental datasets
- Firmware implementation
