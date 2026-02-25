from person import Person

class Student(Person):
    
    def __init__(self, name, person_id, email, phone, student_id, major, enrollment_date):
        super().__init__(name, person_id, email, phone)
        self.__student_id = student_id
        self.major = major
        self.enrollment_date = enrollment_date

        self.enrolled_courses = list()
        self.grades = dict()
        self.__gpa = 0
    
    def get_info(self):
        ''' returns the public infromation about a student'''

        print(f'\n Student Information \n {self.name} is a student of the University.')


    def enroll_course(self, course_code): 
        ''' Add a course to the student's enrolled list if not already enrolled'''

        if len(self.enrolled_courses) >= 6:
            raise ValueError('Cannot enroll in more than 6 courses')

        if course_code not in self.enrolled_courses:
            self.enrolled_courses.append(course_code)
            print(f'{self.name} has been enrolled in {course_code}.')
        else:
            print(f'{self.name} is already enrolled in {course_code}.')


    def add_grade(self, course_code, grade):
        # validate grade 
        if not (0.0 <= grade <= 4.0):
            raise ValueError(f'Invalid grade {grade}. Must be between 0.0 and 4.0.')

        # update grade
        if course_code in self.enrolled_courses:
            self.grades[course_code] = grade
            print(f'Grade {grade} added for {course_code}.')
        else:
            print(f'{self.name} is not enrolled in {course_code}.')

    @property
    def calculate_gpa(self):
        course_count = 0
        total_marks = 0

        for course, grade in self.grades.items():
            if grade is not None:
                course_count += 1
                total_marks += grade

        if course_count > 0 :
            self.__gpa = round(total_marks / course_count, 2)
        else :
            self.__gpa = 0

    def get_academic_status(self):
        ''' Return academic status based on GPA. '''

        if self.__gpa >= 3.5:
            return 'Dean\'s List'
        elif self.__gpa >= 2.0:
            return 'Good Standing'
        else:
            return 'Probation'
        
    def get_responsibilities(self):
        ''' returns responsinilities of a student '''

        print(f'\nStudent {self.name} responsibilities are : \n')
        print('Attend lectures and complete assignments.')
        print('Prepare for exams and submit projects.')






    
       
    

    

 
