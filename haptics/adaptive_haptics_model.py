# Haptics/adaptive_haptics_model.py
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
from sklearn.model_selection import train_test_split

# Sample data for training - replace with actual data
# Features: [comprehension_level, response_time, accuracy]
# Labels: [haptic_intensity] - a value between 0 and 1 indicating feedback intensity
features = np.array([
    [0.1, 1.2, 0.85],
    [0.4, 0.8, 0.95],
    [0.3, 1.5, 0.60],
    [0.6, 0.6, 0.90],
    [0.7, 1.0, 0.70],
    [0.2, 1.3, 0.65]
])
labels = np.array([0.3, 0.7, 0.4, 0.8, 0.5, 0.6])

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Build a simple neural network for haptic intensity prediction
def create_haptic_model(input_shape):
    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=(input_shape,)),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='linear')  # Output is the haptic intensity level (0 to 1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# Initialize and train the model
model = create_haptic_model(X_train.shape[1])
history = model.fit(X_train, y_train, epochs=50, batch_size=2, validation_split=0.1)

# Evaluate model performance
loss, mae = model.evaluate(X_test, y_test, verbose=2)
print(f"Test Loss: {loss}, Mean Absolute Error: {mae}")

# Save the model as TensorFlow Lite for Unity integration
model.save('Haptics/adaptive_haptics_model.h5')
print("Model saved as adaptive_haptics_model.h5")

# Convert model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the converted TFLite model
with open('Haptics/adaptive_haptics_model.tflite', 'wb') as f:
    f.write(tflite_model)
print("Model converted and saved as adaptive_haptics_model.tflite")

