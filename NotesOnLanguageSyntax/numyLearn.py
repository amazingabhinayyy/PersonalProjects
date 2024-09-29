import numpy as np 

a = np.array([1,2,3]) 

zeros = np.zeros((2,2)) #creates a 2 by 2 array of zeros
ones = np.ones((1,2)) #creates a 1 by 2 array of ones
constant = np.full((2,2),7) #creates w by w array of 7
identity = np.eye(2)
random = np.random.random((2,2))
indices = np.arange(4) # creates indexes 0-3
emptySameShape = np.empty_like(zeros)
print(emptySameShape.shape)

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3]
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"
# MUTABLE

#Indexing
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"
#using integers preserves matrix operations

#Boolean array indexing
a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx = (a > 2)   #creates array of booleans

#Mathematics

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11, 12])
#print(np.dot(v, w))
np.sum(x)
print(np.sum(x,axis=0)) #sum of col
print(np.sum(x,axis=1)) #sum or row


#Updating np arrays and complex logic
#a[np.arange(4), b] += 10
#a[a > 2]
#x.T to get transpose