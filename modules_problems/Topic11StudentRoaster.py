class Student:
    def __init__(self, student_id, student_name, student_class=None):
       
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
    
    def display(self):
       
        print("Original attributes and their values of the Student class:")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        if self.student_class:
            print(f"Student Class: {self.student_class}")

student_id = input("Enter Student Id: ")
student_name = input("Enter Student Name: ")
student_class = input("Enter Student Class: ")

student = Student(student_id, student_name, student_class)

student.display()
