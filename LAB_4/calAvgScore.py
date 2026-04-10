# 3. Given a dictionary where the keys are student names and the values are lists of
# scores, WAP to calculate the average score for each student and return it as a
# dictionary.

def calculate_average(scores_dict):
    avg_dict = {}

    for student, scores in scores_dict.items():
        total = sum(scores)
        average = total / len(scores)
        avg_dict[student] = average

    return avg_dict


# Example input
students = {
    "Sachin": [85, 90, 78],
    "NAveen": [88, 92, 80, 84],
}

result = calculate_average(students)
print(result)
