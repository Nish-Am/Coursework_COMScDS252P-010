from person import Person
from student import Student
from faculty import Faculty
from faculty import Department
from faculty import Course
from Staff import Staff

def main():
    person_01 = Person('Uni Memeber', 'P001', 'member01@uni.lk', '+947012245')
    student_01 = Student('Anne', 'P002', 'anne@uni.lk', '+94234123', 'S001', 'DS', '2025/10/01')
    faculty_01 = Faculty(name='Ben', 
                         person_id='P003',  
                         email='ben@uni.lk', 
                         phone='+945632346', 
                         employee_id='E001', 
                         department='Computer Science', 
                         hire_date='2021/02/05')
    
    staf_01 = Staff(name = 'Stela',
                    person_id='P004',  
                    email='stela@uni.lk', 
                    phone='+945633446', 
                    employee_id='E004', 
                    department='Statistics',
                    role= 'Lecturer')

    # method inheritance
    print('\n Registration Infromation \n')

    person_01.get_info()
    student_01.get_info()
    faculty_01.get_info()

    # course enrollment functionality
    print('\n Course Enrollment Infromation \n')

    # Polymorphism - get_responsibilities() across different person types:
    student_01.get_responsibilities()
    faculty_01.get_responsibilities()
    staf_01.get_responsibilities()

    # Create department
    dept_01 = Department('Computer Science', faculty_01)
    dept_01.add_faculty(faculty_01)

    # Create courses
    course_01 = Course('CS101', 'Intro to Programming', 4, faculty_01)
    course_02 = Course('CS102', 'Data Structures', 4, faculty_01)

    dept_01.add_course(course_01)
    dept_01.add_course(course_02)

    # Display department info
    dept_01.get_department_info()

    try: 
        student_01.enroll_course('DS') # enrolling for the first time
        student_01.enroll_course('DS') # check duplcate validation 

        student_01.enroll_course('ST')
        student_01.enroll_course('PY')
        student_01.enroll_course('CS')

        student_01.add_grade(course_code='DS', grade= 10) # validate grade
        student_01.add_grade(course_code='AI', grade= 3.5) # check existing course validation

        student_01.add_grade(course_code='DS', grade= 3.8) 
        student_01.add_grade(course_code='ST', grade= 2.5)
        student_01.add_grade(course_code='PY', grade= 3.7)
        student_01.add_grade(course_code='CS', grade= 3.1)

        student_01.calculate_gpa()

        print(f' {student_01.name} - GPA - {student_01.gpa} - Academic Status - {student_01.get_academic_status()}')

        

    except ValueError as e:
        # Catch any unhandled ValueError from the class
        print('An error occurred in course enrollment :', e)    

if __name__ == '__main__':
    main()