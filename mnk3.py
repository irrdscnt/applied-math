import numpy as np
import matplotlib.pyplot as plt

x = np.array([10, 15, 25, 35, 45, 55, 65, 75, 85, 95])
y = np.array([2600, 2100, 1300, 1000, 820, 670, 580, 510, 490, 470])

mean_x = np.mean(x)
mean_y = np.mean(y)
slope = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x) ** 2)
intercept = mean_y - slope * mean_x

print(f"Linear Regression Equation: y = {slope:.2f}x + {intercept:.2f}")# Quadratic 
coefficients = np.polyfit(x, y, 2)
quadratic_fit = np.poly1d(coefficients)
print(f"Quadratic Regression Equation: {quadratic_fit}")


radius_to_predict = 1# Use the quadratic regression equation to predict the cost
predicted_cost = quadratic_fit(radius_to_predict)

print(f"Predicted cost for a radius of {radius_to_predict} km: {predicted_cost:.2f}")

plt.scatter(x, y, label='Original data')

plt.plot(x, quadratic_fit(x), color='green', label='Quadratic regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


