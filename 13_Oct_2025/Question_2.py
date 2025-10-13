import matplotlib.pyplot as plt

X = range(-15, 16)
Y = [x**2 for x in X]

plt.plot(X, Y, 'r')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Plotting y = x^2")
plt.show()