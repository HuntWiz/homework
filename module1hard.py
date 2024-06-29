grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
new_grades = [(sum(grades[x])/len(grades[x])) for x in range(len(grades))]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
students_grades = dict(zip(students, new_grades))
print(students_grades)
