# 6. WAP that takes a dictionary where keys are employee names and values are their
# respective salaries. Return the top 3 employees with the highest salaries in
# descending order. If there are ties, sort by name alphabetically.


# Input dictionary
employees = {
    "Naveen": 50000,
    "Sachin": 70000,
    "Sweety": 70000,
    "Mehak": 60000,
}

# Convert dictionary to list of (name, salary)
emp_list = list(employees.items())

# Sort: salary descending, name ascending
emp_list.sort(key=lambda x: (-x[1], x[0]))

# Get top 3 employees
top_3 = emp_list[:3]

# Print result
print("Top 3 employees with highest salaries:")
for name, salary in top_3:
    print(name, ":", salary)
