"""
Pseudo Python code for sensor anomaly analysis.
Project: ESP32 Sensor Monitoring and Theft Detection

This script shows the main analysis flow:
1. Load accelerometer data
2. Extract MAD features
3. Train autoencoder using normal data
4. Calculate MSE threshold
5. Compare normal vs anomaly signals
6. Compare reaction time
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Load sensor data
# --------------------------------------------------

normal_data = pd.read_csv("data/tree_shaking_normal.csv")
anomaly_data = pd.read_csv("data/picking_up_anomaly.csv")

# Use accelerometer axes
normal_acc = normal_data[["AccelX", "AccelY", "AccelZ"]].values
anomaly_acc = anomaly_data[["AccelX", "AccelY", "AccelZ"]].values


# --------------------------------------------------
# 2. Feature extraction using MAD
# --------------------------------------------------

def calculate_mad(signal):
    median_value = np.median(signal, axis=0)
    mad_value = np.median(np.abs(signal - median_value), axis=0)
    return mad_value


normal_mad = calculate_mad(normal_acc)
anomaly_mad = calculate_mad(anomaly_acc)

print("Normal MAD:", normal_mad)
print("Anomaly MAD:", anomaly_mad)


# --------------------------------------------------
# 3. Train Autoencoder on normal condition only
# --------------------------------------------------

autoencoder = build_autoencoder(input_size=3)

autoencoder.fit(
    normal_acc,
    normal_acc,
    epochs=50,
    batch_size=16,
    validation_split=0.2
)


# --------------------------------------------------
# 4. Calculate reconstruction error and threshold
# --------------------------------------------------

normal_prediction = autoencoder.predict(normal_acc)

normal_mse = np.mean((normal_acc - normal_prediction) ** 2, axis=1)

threshold = np.mean(normal_mse) + 2 * np.std(normal_mse)

print("Recommended threshold:", threshold)


# --------------------------------------------------
# 5. Detect anomaly
# --------------------------------------------------

def detect_anomaly(sample, model, threshold):
    prediction = model.predict(sample)
    mse = np.mean((sample - prediction) ** 2)

    if mse > threshold:
        return "Anomaly Detected"
    else:
        return "Normal Condition"


result = detect_anomaly(anomaly_acc, autoencoder, threshold)
print(result)


# --------------------------------------------------
# 6. Plot normal vs anomaly signal
# --------------------------------------------------

plt.figure(figsize=(10, 7))

axis_names = ["X-force", "Y-force", "Z-force"]

for i in range(3):
    plt.subplot(3, 1, i + 1)
    plt.plot(normal_acc[:, i], label="Normal: Tree Shaking")
    plt.plot(anomaly_acc[:, i], label="Anomaly: Picking up and Movement")
    plt.ylabel(axis_names[i])
    plt.legend()

plt.xlabel("Sample")
plt.suptitle("Tree Shaking vs Picking up Carefully and Movement")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 7. Reaction time comparison
# --------------------------------------------------

models = ["Autoencoder", "CNN"]

normal_time = [128, 720]      # microseconds
anomaly_time = [84, 98]      # microseconds

reaction_table = pd.DataFrame({
    "Model": models,
    "Normal Condition Reaction Time (us)": normal_time,
    "Anomaly Condition Reaction Time (us)": anomaly_time
})

print(reaction_table)
