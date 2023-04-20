# Define the function to sort the input based on earliest due date algorithm
def earliest_due_date(input_list):
    # Sort the list based on deadline
    sorted_list = sorted(input_list, key=lambda x: x[1])
    return sorted_list

# Initialize an empty list to store the input data
input_data = []

# Take 20 inputs for computation time and deadline and append to input_data list
for i in range(20):
    ci = int(input(f"Enter computation time for task {i+1}: "))
    di = int(input(f"Enter deadline for task {i+1}: "))
    input_data.append((ci, di))

# Sort the input data based on earliest due date algorithm using the function defined above
sorted_data = earliest_due_date(input_data)

# Print the sorted data
print("Sorted data based on earliest due date algorithm: ")
for i, task in enumerate(sorted_data):
    print(f"Task {i+1}: Computation time = {task[0]}, Deadline = {task[1]}")

# Check if the schedule is feasible
current_time = 0
feasible = True
for task in sorted_data:
    current_time += task[0]
    if current_time > task[1]:
        feasible = False
        break

if feasible:
    print("This schedule is feasible.")
else:
    print("This schedule is not feasible.")
