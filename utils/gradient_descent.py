import numpy as np

# Defining the sigmoid function for activations
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

learnrate = 0.5
x = np.array([1, 2])
y = np.array(0.5)

# Initial weights
w = np.array([0.5, -0.5])

# Calculate one gradient descent step for each weight
# Calculate output of neural network
nn_output = sigmoid(x[0]*w[0] + x[1]*w[1])
# or nn_output = sigmoid(np.dot(x, weights))

# Calculate error of neural network
# output error (y - y-hat)
error = y - nn_output

# error term (lowercase delta)
error_term = error * sigmoid_prime(np.dot(x,w))

# Calculate change in weights
del_w = [ learnrate * error_term * x[0],
                 learnrate * error_term * x[1]]

print('Neural Network output:')
print(nn_output)
print('Amount of Error:')
print(error)
print('Change in Weights:')
print(del_w)
