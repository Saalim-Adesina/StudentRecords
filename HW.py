def main():
    while True:
        response = display_menu()
        if response == 1:
            add_student()
        elif response == 2:
            add_course()
        elif response == 3:
            enroll_student()
        elif response == 4:
            display_students()
        elif response == 5:
            display_courses()
        elif response == 6:
            student_average()
        elif response == 7:
            highest_grade()
        elif response == 8:
            print("\t\tExiting....")
            break

# Helper functions

# Checks if a student exists on student.txt
def student_exists(ID):
        '''
        Checks whether the student exits\n
        Returns True if the student exists\n
        Retuns False if student doesn't exist\n
        '''

        exists = False
        with open('students.txt', 'r') as file:
            ids = []
            for line in file:
                ids.append(int(line.split(',')[0].strip()))
        try:
            if int(ID) in ids:
                exists = True
            else:
                exists = False
        except ValueError:
            return 'Error: Input not a number'
        return exists    

# Checks if the course exists on courses.txt
def course_exists(name):
    '''
    Returns True if the course exists.\n
    Returns False if course doesn't exist.
    '''
    exists = False
    with open('courses.txt', 'r') as file:
        courses = []
        for eachLine in file:
            courses.append(eachLine.strip())    
    
    if name in courses:
        exists = True

    return exists

# Ensures grade is between 1 and 100
def validate_grade():
    while True:
        try:
            grade = int(input('Enter your grade: '))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade should be an integer between 0 and 100")
        except ValueError:
            print("\t\tEnter an integer value")

# Converts the ID to a name 
def student_record(ID:int):
    '''
    Converts an ID to the grades record\n
    Returns a list [ID,Name,Grade]
    '''
    with open('students.txt', 'r') as file:
        student = 0
        for line in file:
            line_list = line.split(',')
            if int(ID) == int(line_list[0]):
                return line_list

# Main Functions

# Display menu
def display_menu():
    while True:
        try: 
            response = int(input("""
            Enter an option number: 
                1. Add a new student 
                2. Add a new course 
                3. Enroll a student in a course and assign a grade 
                4. Display all students 
                5. Display all courses 
                6. Calculate average grade for a student 
                7. Find the highest-scoring student in a course 
                8. Exit
>"""))
            if 1 <= response <= 8:
                break
            else:
                print("\nSelect a number between 1 and 8")
        except ValueError:
            print('\nEnter a valid number')
    
    return response

# Register a student
def add_student():    
    with open('students.txt', 'a') as file:
        
        # Validating for text and spaces
        while True:
            valid_name = True
            name = input("Enter the name of the student: ")

            # validating input
            for letter in name:
                if not letter.isalpha() and not letter.isspace():
                    valid_name = False
            if valid_name:    
                break
            else:
                print('\t\tPlease input a valid name with letters and spaces only')
        
        while True:
            try:
                # Ensuring the ID contains only numbers
                ID = int(input("Enter the id of the student: "))
            except ValueError:
                print("Only enter a number")

            # Ensuring the ID doesn't already exist
            if not student_exists(ID):
                file.write(f'{ID},{name}\n')
                print('\n\t---Student Added Succesfully---')
                break
            else:
                print('\t\tStudent ID is already taken')

# Add a course
def add_course():
    with open('courses.txt', 'a') as file:
        while True:
            course = input("Enter the name of the course: ")
            if course.isalpha():
                break
            else:
                print("Course name can only contain alphabets")

        # Validate the course doesn't already exists
        while not course_exists(course):
            file.write(course + '\n')
            print(f'\t---Course: {course} Added Successfully---')
            break
        else:
            print('Course already exists')

# Enroll a student to a registered course
def enroll_student():
    while True:
        
        # Validating ID to only digits
        while True:
            student = input("Enter the ID of the student: ")
            if student.isdigit():
                break
            else:
                print("\tID can only contain integers")

        # Validating ID exists in students.txt
        if not student_exists(student):
            print(f'\t\tStudent with ID {student} doesn\'t exist' )
        else:
            # Validating course exists in courses.txt
            while True: 
                course = input("Enter the course to enroll the student in: ")
                if not course_exists(course):
                    print(f'\t\tCourse: {course} doesn\'t exist')
                else: 
                    # Saving record into grades.txt
                    with open('grades.txt', 'a') as file:
                        grade = validate_grade()
                        file.write(f'{student},{course},{grade}\n')
                        print('Student Sucessfuly enrolled')
                        break
            break

# Display all students
def display_students():
    '''
    Returns students and student ID in a tuple\n
    ([students], [ids])
    '''
    with open('students.txt', 'r') as file:
        students =[]
        ids = []
        for line in file:
            students.append(line.split(',')[1].strip())
            ids.append(int(line.split(',')[0].strip())) 
    
    #Check if files aren't empty
    if students == [] and ids == []:
        print('No student records')
    else:
        print('-------Students-------')
        counter = 1
        for student in students:
            print(f'{counter}) {student}')
            counter += 1

# Display all courses
def display_courses():
    with open('courses.txt', 'r') as file:
        courses =[]
        for line in file:
            courses.append(line.strip())
    
    if courses == []:
        print("No courses registered")
    else:
        counter = 1
        print('--------Your Courses---------')
        for course in courses:
            print(f'{counter}) {course}')
            counter += 1
        
# Calculate the average of a student in all courses
def student_average():
    student = 0
    average = 0
    while True:
        while True:
            student = input("Enter the ID of the student: ")
            if student.isdigit():
                break
            else:
                print('Enter a valid number ID')

        if student_exists(student):
            with open('grades.txt', 'r') as file:
                student_grades = []
                all_records = []
                sum = 0
                counter = 0
                average = 0
                for eachLine in file:
                    line = eachLine.split(',')
                    # Accumulate all grades of the student
                    if line[0] == student:
                        sum += int(line[2])
                        counter += 1
                try:        
                    average = format(sum / counter, '.2f')
                except ZeroDivisionError:
                    pass
                break
        else:
            print("\t\tThe student doesn't exist")
    
    print('\t\tThe average of the student is: ' + str(average))

# Finding the student with the highest grade in a course
def highest_grade():
    while True:
        course = input("Enter your course: ")

        # Validating input
        if course_exists(course):
            max_grade = -1
            max_student = None
            with open('grades.txt', 'r') as file:
                for eachLine in file:
                    #eachLine = 'ID,Course,Grade'
                    line = eachLine.split(',')
                    if line[1] == course: 
                        grade = int(line[2].strip())
                        student = line[0]
                        if grade > max_grade:
                            max_grade = grade
                            max_student = student

            if max_student == None and max_grade == -1:
                print('No grades exist for the student')
                break
            else:
                print(f'\nThe student with the highest grade in {course} is:\n\tName: {student_record(max_student)[1]}\tID: {max_student} \n\tGrade: {max_grade}' )
                break
        else:
            print(f'Your course {course} doesn\'t exist')

main()