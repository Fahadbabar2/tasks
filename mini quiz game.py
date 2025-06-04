class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.rollnumber = roll_number
        self.marks = marks

    def print_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Roll Number:", self.rollnumber)
        print("Marks:", self.marks)

# Creating a student using variables
student_name = "fahad"
studentroll = 168
student_marks = 88

student1 = Student(student_name, studentroll, student_marks)
student1.print_details()
