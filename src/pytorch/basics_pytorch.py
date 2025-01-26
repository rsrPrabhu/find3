import torch
import torch.nn as nn
import torch.optim as optim

# 1. Prepare the Data (Simple Example: y = 2x + 3)
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])  # Input data
y_train = torch.tensor([[5.0], [7.0], [9.0], [11.0]])  # Target data


# 2. Define the Model
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # One input, one output

    def forward(self, x):
        return self.linear(x)


model = LinearRegressionModel()

# 3. Define Loss Function and Optimizer
criterion = nn.MSELoss()  # Mean Squared Error Loss
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent

# 4. Train the Model
num_epochs = 1000
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(x_train)
    loss = criterion(outputs, y_train)

    # Backward pass and optimization
    optimizer.zero_grad()  # Reset gradients
    loss.backward()  # Compute gradients
    optimizer.step()  # Update weights

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# 5. Test the Model
x_test = torch.tensor([[6.0]])  # Test input
predicted = model(x_test).item()  # Forward pass
print(f"Prediction for input 6.0: {predicted:.2f}")

# 6. Save and Load the Model (Optional)
torch.save(model.state_dict(), "linear_regression_model.pth")
print("Model saved.")
