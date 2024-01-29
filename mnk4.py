import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96])
y = np.array([3.35, 3.62, 4.21, 4.5, 4.9, 5.3, 5.8, 6.11, 6.3, 6.1])

mean_x = np.mean(x)
mean_y = np.mean(y)
slope = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x) ** 2)
intercept = mean_y - slope * mean_x

print(f"Linear Regression Equation: y = {slope:.2f}x + {intercept:.2f}")# Quadratic 
coefficients = np.polyfit(x, y, 2)
quadratic_fit = np.poly1d(coefficients)
print(f"Quadratic Regression Equation: {quadratic_fit}")


radius_to_predict = 0.86# Use the quadratic regression equation to predict the cost
predicted_cost = quadratic_fit(radius_to_predict)

print(f"Predicted patent for a competition of {radius_to_predict} : {predicted_cost:.2f}")

plt.scatter(x, y, label='Original data')

plt.plot(x, quadratic_fit(x), color='green', label='Quadratic regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
