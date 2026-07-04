# System Pseudocode

The original firmware is not publicly available.

The following pseudocode summarizes the overall operation of the system.

---

## Initialization

```text
Initialize ESP32

Initialize DHT11

Initialize ADXL345

Initialize HC-SR04

Initialize buzzer

Load TinyML model

Load anomaly threshold

Load distance threshold
```

---

## Main Monitoring Loop

```text
Loop Forever

    Read temperature

    Read humidity

    Read accelerometer values

    Read ultrasonic distance

    Extract motion features

    Calculate Median Absolute Deviation (MAD)

    Run Autoencoder inference

    Compute reconstruction error (MSE)

    If

        MSE > anomaly threshold

        AND

        Distance < distance threshold

            Trigger buzzer

            Report anomaly

    Else

            Continue monitoring

End Loop
```

---

# Feature Extraction

```text
Input:

Accelerometer X

Accelerometer Y

Accelerometer Z

↓

Compute statistical features

↓

Median

Mean

Median Absolute Deviation (MAD)

↓

Feature Vector
```

---

# TinyML Inference

```text
Feature Vector

↓

TensorFlow Lite Autoencoder

↓

Reconstructed Feature Vector

↓

Mean Squared Error (MSE)

↓

Compare with Threshold

↓

Normal / Anomaly
```

---

# Decision Logic

```text
IF

Reconstruction Error > Learned Threshold

AND

Measured Distance < Distance Threshold

THEN

Alarm ON

ELSE

Continue Monitoring
```

---

# Repository Note

The original firmware, TinyML model, training scripts, and datasets are intentionally omitted from this repository due to security and academic restrictions.

This document is intended to demonstrate the overall system logic without exposing implementation-specific details.
