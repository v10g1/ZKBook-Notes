import numpy as np

# define the matrices
O = np.matrix([[0,1,0,0]])
L = np.matrix([[0,0,1,0]])
R = np.matrix([[0,0,0,1]])

# witness vector
a = np.array([1, 4223, 41, 103])

# Multiplication `*` is element-wise, not matrix multiplication.
# Result contains a bool indicating an element-wise indicator that the equality is true for that element.
result = np.matmul(O, a) == np.matmul(L, a) * np.matmul(R, a) 

# check that every element-wise equality is true
assert result.all(), "result contains an inequality"
