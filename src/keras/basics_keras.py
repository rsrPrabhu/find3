import joblib
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
def train_and_save_model():
   # Step 1: Load the dataset
 df = pd.read_csv("bank-additional-full.csv", delimiter=";")  # Ensure the correct delimiter is used

   # Step 2: Preprocess the data
   # 2a: Handle missing values (if any), here we fill with 0 for simplicity
 df = df.fillna(0)

   # 2b: Convert categorical columns to numeric values using LabelEncoder
 label_encoder = LabelEncoder()

   # Encode the target column 'y' (binary: 'yes' -> 1, 'no' -> 0)
 df['y'] = label_encoder.fit_transform(df['y'])

   # Encode other categorical columns (e.g., 'job', 'marital', 'education', etc.)
 categorical_columns = df.select_dtypes(include=['object']).columns
 for column in categorical_columns:
    if column != 'y':  # Skip encoding the target column 'y'
        df[column] = label_encoder.fit_transform(df[column])

   # 2c: Separate features (X) and target (y)
 X = df.drop(columns=['y'])  # Features (everything except target)
 y = df['y']  # Target column

   # Step 3: Scale the features (important for neural networks)
 scaler = StandardScaler()
 X_scaled = scaler.fit_transform(X)  # Normalize the features

   # Step 4: Split the data into training and testing sets (80% train, 20% test)
 X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

   # Save column names of X_train
 joblib.dump(X.columns, 'columns.pkl')  # Save the column names

   # Step 5: Build the Neural Network model
 model = Sequential()

   # Input layer and first hidden layer (ReLU activation)
 model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))

   # Second hidden layer (ReLU activation)
 model.add(Dense(32, activation='relu'))

   # Output layer (Sigmoid activation for binary classification)
 model.add(Dense(1, activation='sigmoid'))

   # Step 6: Compile the model (using Adam optimizer and binary crossentropy loss function)
 model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

   # Step 7: Train the model (use training and validation data)
 history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

   # Step 8: Evaluate the model
 test_loss, test_accuracy = model.evaluate(X_test, y_test)

 model.save('model.keras')
 joblib.dump(scaler, 'scaler.pkl')  # Save the scaler

 print(f"Test Loss: {test_loss}")
 print(f"Test Accuracy: {test_accuracy}")
'''
# Step 9: Visualize the training process (accuracy and loss over epochs)
# Plot training & validation accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Plot training & validation loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
'''

if __name__ == '__main__':
    # Train and save the model and scaler when starting the file
    train_and_save_model()


