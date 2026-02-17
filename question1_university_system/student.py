from person import Person

class Student(Person):
    
    def __init__(self, name, person_id, email, phone, student_id, major, enrollment_date):
        super().__init__(name, person_id, email, phone)
        self.student_id = student_id
        self.major = major
        self.enrollment_date = enrollment_date
    
    def get_info(self):
        ''' returns the public infromation about a student'''

        print(f'Student Information \n {self.name} is a student of the University \n Student ID - {self.student_id}')