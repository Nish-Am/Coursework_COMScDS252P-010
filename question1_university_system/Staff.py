from person import Person

class Staff(Person):
    
    def __init__(self, name, person_id, email, phone, employee_id, role, department):
        super().__init__(name, person_id, email, phone)
        self.employee_id = employee_id
        self.department  = department
        self.role        = role

    def get_info(self):
        ''' returns the public infromation about a Staff Memeber'''

        print(f'Staff Information \n {self.name} is a Staff member of the University \n Department - {self.department}')