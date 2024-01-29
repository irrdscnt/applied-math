import matplotlib.pyplot as plt

# Данные для графика
euler_method = ([0, 0.8, 1.6, 2.4, 3.2], [2, 2.8, 7.4399999999999995, 18.991999999999997, 42.9856])
modified_euler_method = ([0, 0.8, 1.6, 2.4, 3.2], [2, 4.72, 14.9664, 41.168768, 101.19778816000002])
runge_kutta_method = ([0, 0.8, 1.6, 2.4, 3.2], [2, 5.3344000000000005, 17.63437056, 49.859425132544004, 126.3659864145658])
analiticheskii_method=([0, 0.8, 1.6, 2.4, 3.2], [2, 5.35325, 17.71819, 50.13906, 127.19518])

# Построение графика
plt.plot(euler_method[0], euler_method[1], label='Euler Method')
plt.plot(modified_euler_method[0], modified_euler_method[1], label='Modified Euler Method')
plt.plot(runge_kutta_method[0], runge_kutta_method[1], label='Runge-Kutta Method')
plt.plot(analiticheskii_method[0], analiticheskii_method[1], label='Analitycal Method')

# Добавление подписей и легенды
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Comparison of Numerical Integration Methods')
plt.legend()

# Отображение графика
plt.show()
