
def calculate_result(student_number, name, marks_c, marks_cpp, marks_java):
    total_marks = marks_c + marks_cpp + marks_java
    average = total_marks / 3
    
   
    if average < 70:
        result = "Fail"
        grade = "-"
    else:
        result = "Pass"
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
    
    print(f"\nStudent Number: {student_number}")
    print(f"Student Name: {name}")
    print(f"Marks in C: {marks_c}")
    print(f"Marks in C++: {marks_cpp}")
    print(f"Marks in Java: {marks_java}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average}")
    print(f"Result: {result}")
    print(f"Grade: {grade}")


student_number = input("Enter student number: ")
name = input("Enter student name: ")
marks_c = float(input("Enter marks in C: "))
marks_cpp = float(input("Enter marks in C++: "))
marks_java = float(input("Enter marks in Java: "))

calculate_result(student_number, name, marks_c, marks_cpp, marks_java)
