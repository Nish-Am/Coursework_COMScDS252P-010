import re

class Person:
    def __init__(self, name, person_id, email, phone):
        self.name = name
        self.person_id = person_id
        self.email = email
        self.phone = phone

        self.validate()

    def get_info(self):
        ''' returns the public infromation about the person'''
        print(f'\n This is a generic person level information. \n {self.name} is a memeber of University')

    def update_info(self, email, phone):
        '''update person info'''
        self.email = email
        self.phone = phone

    def validate(self):
        ''' validate basic info '''

        # validate if name has numbers 
        if any(char.isdigit() for char in self.name):
            raise ValueError(f'Invalid Name ! {self.name} name cannot contain numbers.')
        
        # validate email 
        if '@' not in self.email:
            raise ValueError(f'Invalid Email ! {self.email} emial should contain @ sign')
        
        # validate date format 
        if not re.match(r'^[\d\+]+$', self.phone):
            raise ValueError(f"Invalid phone Number ! : '{self.phone}' should contain only digits or '+'")
