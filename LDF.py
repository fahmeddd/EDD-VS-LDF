# Define the function to sort the input based on latest deadline first algorithm
def latest_deadline_first(input_list):
    # Sort the list based on deadline in descending order
    sorted_list = sorted(input_list, key=lambda x: x[1], reverse=True)
    return sorted_list

# Initialize an empty list to store the input data
input_data = []

# Take 20 inputs for computation time and deadline and append to input_data list
for i in range(20):
    ci = int(input(f"Enter computation time for task {i+1}: "))
    di = int(input(f"Enter deadline for task {i+1}: "))
    input_data.append((ci, di))

# Sort the input data based on latest deadline first algorithm using the function defined above
sorted_data = latest_deadline_first(input_data)

# Print the sorted data
print("Sorted data based on latest deadline first algorithm: ")
for i, task in enumerate(sorted_data):
    print(f"Task {i+1}: Computation time = {task[0]}, Deadline = {task[1]}")