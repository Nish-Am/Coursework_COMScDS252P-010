from person import Person

class Faculty(Person):
    
    def __init__(self, name, person_id, email, phone, employee_id, department, hire_date):
        super().__init__(name, person_id, email, phone)
        self.employee_id = employee_id
        self.department  = department
        self.hire_date   = hire_date 

    def get_info(self):
        ''' returns the public infromation about a faculty'''

        print(f'Faculty Level Information \n {self.name} is a Faculty of the University \n Department - {self.department}')