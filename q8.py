import numpy as np

cost=np.array([[30, 46], [35, 51]])
total=np.array([2488, 2852])

inv_cost=np.linalg.inv(cost)


ans=np.dot(inv_cost,total)
children=ans[0]
adult=ans[1]

print("Children: ",round(children))

print("Adults: ",round(adult))














# import numpy as np

# # Coefficients matrix
# coefficients = np.array([[30, 46], [35, 51]])

# # Constants matrix
# totals = np.array([2488, 2852])

# # Solve the system of equations
# solution = np.linalg.solve(coefficients, totals)

# # Extract the values for children and adults
# num_children = round(solution[0])
# num_adults = round(solution[1])
# print("Number of children: ", num_children)

# print("Number of adults: ", num_adults)