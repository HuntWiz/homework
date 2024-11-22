import numpy as np

a = np.array([[5, 4, 3, 1], [6, 12, 7, 9], [1, 10, 13, 12]])
print(a)

a.sort()
print(a)

b = a[0][1] + a[2][2]
print(a[0][1], a[2][2], b)


prediction = np.array([[1, 1, 1]])
labels = np.array([[1, 11, 1]])
mean_square_error = (1/3)*np.sum(np.square(prediction - labels))
print(mean_square_error)
