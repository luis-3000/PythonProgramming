lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

#Print students data
for student in students:
    print student["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]

# Add your function below!
def average(numbers):  #Calculate the average
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

# Compute a student's average using weighted averages
def get_average(student):
    """ 
    Takes a student dictionary as input and returns his/her 
    weighted average
    """
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])        
    sum = (homework * 0.10) + (quizzes * 0.30) + (tests * 0.60)
    return sum

    
def get_letter_grade(score):
    """ Takes score as a number argument
        Returns the letter grade for the student"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
print get_letter_grade(lloyd)

# Now calculate the class average
""" 
01. Define a function called get_class_average that has one argument
    students. You can expect students to be a list containing your three
    students.
02. First, make an empty list called results.
03. For each student item in the class list, calculate 
    get_average(student) and then call results.append() with that 
    result.
04. Finally, return the result of calling average() with results.
""""
# Now calculate the class average
def get_class_average(students):
    """ Takes the 3 studens list"""    
    results = []    
    for student in students:
        result = get_average(student)
        results.append(result)        
    return average(results)

"""
Instructions
01. Finally, print out the result of calling get_class_average with 
    your students list. Your students should be [lloyd, alice, tyler].
02. Then, print the result of get_letter_grade for the class's average.
"""
for student in students:
    print get_class_average(students)
    print get_letter_grade(get_class_average(students))