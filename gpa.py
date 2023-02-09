def calculate_gpa():
    courses = []
    total_units = 0
    total_grade_points = 0

    numberOfCourses = int(input("Enter the Number of Courses you Offered: "))
    for i in range(numberOfCourses):
        code = input("Enter the course code: ")
        title = input("Enter the course title: ")
        score = int(input("Enter your score: "))
        units = int(input("Enter the number of units: "))

        if score >= 70 and score <= 100:
            grade = 'A'
        elif score >= 60 and score <= 69:
            grade = 'B'
        elif score >= 50 and score <= 59:
            grade = 'C'
        elif score >= 45 and score <= 49:
            grade = 'D'
        elif score >= 40 and score <= 44:
            grade = 'E'
        else:
            grade = 'F'

        if grade == 'A':
            grade_points = 5.0
        elif grade == 'B':
            grade_points = 4.0
        elif grade == 'C':
            grade_points = 3.0
        elif grade == 'D':
            grade_points = 2.0
        elif grade == 'E':
            grade_points = 1.0
        else:
            grade_points = 0

        courses.append((code, title, score, units, grade, grade_points))

        total_units += units
        total_grade_points += grade_points * units
        
    if total_units == 0:
        print("GPA: N/A")
    else:
        gpa = total_grade_points / total_units
       
       
        print("\nDISPLAYING: \n")
        for course in courses:
            print("{} \t {} \t\t {} \t\t {}".format(course[0], course[1], course[3], course[2]))


        print("\nSemester Total Points: {:.2f}".format(total_grade_points))
        print("Semester Total units: {:.2f}".format(total_units))
        print("\nSemester GPA: {:.2f}".format(gpa))
        
calculate_gpa()