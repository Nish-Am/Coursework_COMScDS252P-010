from person import Person
from student import Student
from faculty import Faculty
from Staff import Staff

def main():
    person_01 = Person('Uni Memeber 01', 'P001', 'member01@uni.lk', '+947012245')
    student_01 = Student('Anne', 'P002', 'anne@uni.lk', '+94234123', 'S001', 'DS', '2025/10/01')
    faculty_01 = Faculty(name='Ben', 
                         person_id='P003',  
                         email='ben@uni.lk', 
                         phone='+945632346', 
                         employee_id='E001', 
                         department='Computer Science', 
                         hire_date='2021/02/05')

    person_01.get_info()
    student_01.get_info()
    faculty_01.get_info()

if __name__ == "__main__":
    main()