import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Create a Linear Regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make predictions on new data
X_new = np.array([[0], [2]])
y_pred = model.predict(X_new)

# Visualize the data and the regression line
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X_new, y_pred, color='red', linewidth=2, label='Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression (Utsukta)')
plt.show()
