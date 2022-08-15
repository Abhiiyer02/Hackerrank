import os
def gradingStudents(grades):
    # Write your code here
    for i in range(grades_count):
        if grades[i] < 40:
            if grades[i] >= 38:
                grades[i] += (40-i)
            else:
                continue
            print(grades[i])
        elif grades[i]>=40:
            if grades[i]%5 > 2:
                grades[i] += (5 - (grades[i] % 5))
            print(grades[i])
    return grades
    #print(grades)

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    print(grades)
    grades.