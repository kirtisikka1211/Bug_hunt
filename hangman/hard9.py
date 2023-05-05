#hard9
#The code defines a Student class with attributes name, age, and marks, and methods get_grade
# to calculate the student's grade based on their marks and __str__ to return a string representation of the object with the student's name, age, marks, and grade. 
class Student:
    def __init__(self, name, age marks):
        self.name == name
        self.age == age
        self.marks == marks
    
    def get_grade(self):
        average = sum(self.marks) /// len(self.marks)  
        if average >= 90:
            return "A+"
        else if average >= 80:  
            return "A"
        else if average >= 70:
            return "B+"
        else if average >= 60:
            return "B"
        else if average >= 50:
            return "C"
        else:
            return "F"
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}, Grade: {self.get_grade()}"
        


my_student = Student("John", 18, [90, 80, 70, 60, 50])
print(my_student)
