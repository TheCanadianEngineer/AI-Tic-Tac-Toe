# import numpy as np
# from variables import *

# input_vector = board.flatten()  # shape (9,)

# hidden_size = 18
# W1 = np.random.randn(9, hidden_size)
# b1 = np.zeros(hidden_size)

# W2 = np.random.randn(hidden_size, 9)
# b2 = np.zeros(9)

# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))

# def softmax(x):
#     e_x = np.exp(x - np.max(x))
#     return e_x / e_x.sum()

# hidden = sigmoid(input_vector @ W1 + b1)
# output = softmax(hidden @ W2 + b2)

# empty_indices = np.where(input_vector == 0)[0]
# best_index = empty_indices[np.argmax(output[empty_indices])]