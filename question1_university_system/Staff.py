from person import Person

class Staff(Person):
    
    def __init__(self, name, person_id, email, phone, employee_id, role, department):
        super().__init__(name, person_id, email, phone)
        self.employee_id = employee_id
        self.department  = department
        self.role        = role

    def get_info(self):
        ''' returns the public infromation about a Staff Memeber'''

        print(f'\n Staff Information \n {self.name} is a Staff member of the University \n Department - {self.department}')

    def get_responsibilities(self):
        ''' returns responsinilities of Staff '''
        
        print(f'\nStaff {self.name} responsibilities are : \n')
        print('Manage administrative tasks and support operations.')
        print('Handle role-specific organizational responsibilities.')