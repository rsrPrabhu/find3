'''
NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy stands for Numerical Python.

Why Use NumPy?
In Python we have lists that serve the purpose of arrays, but they are slow to process.

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.
'''


import numpy as np, random

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr)

print(arr[1:5])

print(np.__version__)
print(arr[0])

print(arr[1:5:2])   #[2 4]
print(arr[::2]) #[1 3 5 7]

arr2D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2D[1, 1:4])  # comma splits the array
print(arr2D[0:2, 2])
print(arr2D.dtype)

copyArray = arr2D.copy()  # copy Array
print(copyArray)


viewArray = arr2D.view()  # view is help to copy Array , but changes happens to view and original that reflects on original Array
print(viewArray)


print(arr2D.shape)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)


newarr = np.array_split(arr, 3)
print(newarr)  # [array([[1, 2, 5, 6]]), array([[3, 4, 7, 8]]), array([], shape=(0, 4), dtype=int64)]

print(np.where(arr == 4))


# ------------  Random
print('Numpy Random Starts Here')
randomValue = random.randint(0,10)  # BW this
print(randomValue)

randomValue2=random.randint(100 , 150)
print(randomValue2)

randomValue3 = random.choice([3, 5, 7, 9])
#randomValue4 = random.choice([3, 5, 7, 9], size=(3, 5))

print(randomValue3)
#print(randomValue4)

# ------------  Random Data Distribution
# Data Distribution is a list of all possible values, and how often each value occurs.

'''
Key Concepts:
Random numbers (uniform, normal, etc.)
Random sampling (choices, permutations, shuffling)
Randomly splitting data (train/test split)
'''
print('Numpy Random Data Distribution Starts Here')
choice = np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])
print(choice)


randomSelect = np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])
print(randomSelect)

'''
5:   This represents the range [0, 1, 2, 3, 4].
     The function will sample from this range of integers.
     
3:   This specifies the number of samples to draw (size=3).
You will get three unique integers in the result because replace=False.

replace=False:
replace=False means that sampling is done without replacement, 
so once an element is selected, it cannot be selected again in the same sampling process. This ensures all selected elements are unique.
Sampling without replacement, meaning no integer will be selected more than once.

p=[0.1, 0, 0.3, 0.6, 0]:
These are the probabilities associated with each element in the range [0, 1, 2, 3, 4].
The probabilities must sum to 1, which is true in this case (0.1 + 0 + 0.3 + 0.6 + 0 = 1).
Probabilities specify how likely each element is to be selected:
0 has a probability of 0.1.
1 has a probability of 0 (will never be selected).
2 has a probability of 0.3.
3 has a probability of 0.6.
4 has a probability of 0 (will never be selected).
'''

# Mean = 0, Standard deviation = 1
normal_dist = np.random.normal(0, 1, (2, 3))
print("\nRandom Numbers from Normal Distribution:\n", normal_dist)

# Mean = 5, Standard deviation = 2
normal_custom = np.random.normal(5, 2, (3, 3))
print("\nCustom Normal Distribution:\n", normal_custom)


# Generate random integers in range [low, high)
rand_int = np.random.randint(1, 10)  # Single integer
print("\nRandom Integer:", rand_int)

# Random integers from 0 to 100, 5 elements
rand_int_array = np.random.randint(0, 100, 5)
print("\nRandom Integer Array:", rand_int_array)

import numpy as np

# Random float between 0 and 1
rand_float = np.random.random()
print("Random Float:", rand_float)

# Random 3x3 matrix from uniform distribution [0, 1)
rand_array = np.random.random((3, 3))
print("\nRandom Array:\n", rand_array)


# Randomly choose from a list (with replacement)
choices = np.random.choice([10, 20, 30, 40], size=5, replace=True)
print("\nRandom Choices:", choices)

# Without replacement
choices_no_replacement = np.random.choice([10, 20, 30, 40], size=3, replace=False)
print("\nRandom Choices (without replacement):", choices_no_replacement)

# Shuffling Data
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)  # In-place shuffling
print("\nShuffled Array:", arr)

# Permuting Elements
arr = np.array([1, 2, 3, 4, 5])
permuted = np.random.permutation(arr)
print("\nPermuted Array:", permuted)

 #
# Generate a random dataset (100 samples, 10 features)
data = np.random.random((100, 10))

# Split the data into training (80%) and testing (20%)
train_data = data[:80]  # First 80 samples
test_data = data[80:]   # Last 20 samples
print("\nTraining Data Shape:", train_data.shape)
print("Testing Data Shape:", test_data.shape)

# Adding Random Noise (for Regularization or Augmentation)
# Original data
data = np.array([10, 20, 30, 40, 50])

# Add random noise (Gaussian noise)
noise = np.random.normal(0, 2, data.shape)  # mean=0, std=2
augmented_data = data + noise

print("\nOriginal Data:", data)
print("Augmented Data with Noise:", augmented_data)

random_array = np.random.normal(50, 20, size=10)
print(random_array)

#These numbers are centered around 50 (the mean).
#Most numbers fall within ±20 (standard deviation) of 50.

random_2d = np.random.normal(0, 2, size=(2, 3))
print("2D Array of Random Numbers:\n", random_2d)

#Each number is independently sampled from a normal distribution with mean = 0 and std = 2.
#Numbers are spread around 0, with most values within ±2.

original_data = np.array([1, 2, 3])
noise = np.random.normal(0, 0.1, original_data.shape)
augmented_data = original_data + noise
print("Augmented Data:", augmented_data , noise)

#Useful for generating synthetic datasets for training/testing.
