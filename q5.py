import numpy as np

# Get the value of N from the user
N = int(input("Enter the value of N for the dimensions of the 2D array: "))

# Create a 2D NumPy array using arange
my_2d_array = np.arange(N * N).reshape((N, N))

# Display the created 2D array
print("2D Array:")
print(my_2d_array)
ans=[]
def return_diag(arr):
    for i in range(N):
        ans.append(arr[i][i])
    return ans

print("Diagonal Element:")
print(return_diag(my_2d_array))