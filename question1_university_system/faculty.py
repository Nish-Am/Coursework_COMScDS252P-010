from person import Person

class Faculty(Person):
    
    def __init__(self, name, person_id, email, phone, employee_id, department, hire_date):
        super().__init__(name, person_id, email, phone)
        self.employee_id = employee_id
        self.department  = department
        self.hire_date   = hire_date 

    def get_info(self):
        ''' returns the public infromation about a faculty'''

        print(f'\n Faculty Level Information \n {self.name} is a Faculty of the University \n Department - {self.department}')

    def get_responsibilities(self):
        ''' returns responsinilities of Faculty '''
        
        print(f'\n Faculty {self.name} responsibilities are : \n')
        print('Teach courses and mentor students.')
        print('Conduct research and publish papers.')

class Department:
    def __init__(self, dept_name, dept_head):
        self.dept_name = dept_name
        self.dept_head = dept_head   
        self.faculty_list = []
        self.course_list = []

    def add_faculty(self, faculty):
        self.faculty_list.append(faculty)

    def add_course(self, course):
        self.course_list.append(course)

    def get_department_info(self):
        print(f'\nDepartment: {self.dept_name}')
        print(f'Head: {self.dept_head.name}')
        print('Faculty Members:')
        for f in self.faculty_list:
            print(f' - {f.name}')
        print('Courses Offered:')
        for c in self.course_list:
            print(f' - {c.course_name} ({c.course_code})')

class Course:
    def __init__(self, course_code, course_name, credits, instructor=None, max_capacity=30):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.instructor = instructor   
        self.enrolled_students = []
        self.max_capacity = max_capacity

    def add_student(self, student):
        if not self.is_full():
            self.enrolled_students.append(student)
            print(f'{student.name} enrolled in {self.course_name}')
        else:
            print(f'{self.course_name} is full!')

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print(f'{student.name} removed from {self.course_name}')

    def is_full(self):
        return len(self.enrolled_students) >= self.max_capacity
        