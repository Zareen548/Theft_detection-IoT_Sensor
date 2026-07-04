# System Overview

## Introduction

This project presents an IoT-based sensor monitoring and theft detection framework designed for remote environmental monitoring applications.

The system continuously measures environmental conditions while simultaneously protecting the deployed sensor node from theft, vandalism, or unauthorized movement.

The complete prototype was developed around an ESP32-S2 microcontroller with onboard TinyML inference for real-time anomaly detection.

---

## Objectives

The framework was designed to:

- Monitor environmental temperature and humidity
- Detect abnormal movement of the sensor node
- Detect unauthorized removal attempts
- Minimize false alarms caused by environmental disturbances
- Perform anomaly detection directly on the embedded device
- Trigger real-time alerts without cloud processing

---

# Hardware Architecture

The prototype consists of the following hardware components:

| Hardware | Function |
|----------|----------|
| ESP32-S2 | Main controller |
| DHT11 | Temperature & humidity sensing |
| ADXL345 | Motion sensing |
| HC-SR04 | Distance measurement |
| Passive Buzzer | Audible alarm |
| LiPo Battery | Portable power |

---

# System Workflow

```
Environmental Sensors
        │
        ▼
ESP32 Sensor Acquisition
        │
        ▼
Feature Extraction
        │
        ▼
TinyML Autoencoder
        │
        ▼
Anomaly Score (MSE)
        │
        ▼
Threshold Evaluation
        │
        ▼
Buzzer Alert
```

---

# Machine Learning Pipeline

The anomaly detection system follows these steps:

1. Collect accelerometer readings
2. Collect ultrasonic distance
3. Extract statistical features
4. Compute Median Absolute Deviation (MAD)
5. Execute Autoencoder inference
6. Compute reconstruction error
7. Compare against learned threshold
8. Trigger alarm if anomaly is detected

---

# Experimental Validation

The system was evaluated under multiple real-world scenarios including:

- Tree shaking
- Device pickup
- Device removal
- Free fall
- Manual shaking
- Aggressive removal
- Casual handling

The framework successfully distinguished normal environmental motion from suspicious handling.

---

# Technologies Used

- ESP32-S2
- Arduino Framework
- TensorFlow Lite
- TinyML
- Python
- NumPy
- Pandas
- Autoencoder Neural Network
