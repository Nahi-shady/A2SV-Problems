
def gradingStudents(grades):
    # Write your code here
    graded = []
    for i in grades:
        if i < 38:
            graded.append(i)
        elif i%5 < 3:
            graded.append(i)
        else:
            graded.append(5 * round(i/5))
    return graded