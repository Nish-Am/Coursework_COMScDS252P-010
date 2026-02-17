class Person:
    def __init__(self, name, person_id, email, phone):
        self.name = name
        self.person_id = person_id
        self.email = email
        self.phone = phone

    def get_info(self):
        ''' returns the public infromation about the person'''
        print(f'This is a generic person level information. \n {self.name} is a memeber of University')

    def update_info(self, email, phone):
        '''update person info'''
        self.email = email
        self.phone = phone