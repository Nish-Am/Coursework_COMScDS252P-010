from person import Person

class Staff(Person):
    
    def __init__(self, name, person_id, email, phone, employee_id, role, department):
        super.__init__(name, person_id, email, phone)
        self.employee_id = employee_id
        self.department  = department
        self.role        = role