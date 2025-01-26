import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Define a Sequential model
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

print(model , "")
# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Dummy data
import numpy as np
X = np.random.random((100, 10))
y = np.random.randint(2, size=(100, 1))

# Train the model
model.fit(X, y, epochs=10, batch_size=16)
