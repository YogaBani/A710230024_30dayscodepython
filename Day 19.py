# Define a class for Student
class Student:
    def __init__(self, name, nim):
        self.name = name
        self.nim = nim
        self.courses = {}

    def add_course(self, course_code, course_name):
        self.courses[course_code] = {"name": course_name, "grades": []}

    def add_grade(self, course_code, grade):
        if course_code in self.courses:
            self.courses[course_code]["grades"].append(grade)
        else:
            print("Course not found!")

    def get_average_grade(self, course_code):
        if course_code in self.courses:
            grades = self.courses[course_code]["grades"]
            return sum(grades) / len(grades)
        else:
            print("Course not found!")
            return None

# Define a class for Course
class Course:
    def __init__(self, code, name, kkm):
        self.code = code
        self.name = name
        self.kkm = kkm

    def __str__(self):
        return f"{self.code} - {self.name} (KKM: {self.kkm})"

# Create some courses
math = Course("MATH101", "Calculus", 70)
english = Course("ENGL101", "English Literature", 80)

# Create a student
student = Student("John Doe", "1234567890")

# Add courses to the student
student.add_course(math.code, math.name)
student.add_course(english.code, english.name)

# Add grades to the student
student.add_grade(math.code, 85)
student.add_grade(math.code, 90)
student.add_grade(english.code, 75)

# Print the student's grades and average grades
print("Student:", student.name)
print("NIM:", student.nim)
print("Courses:")
for course_code, course_info in student.courses.items():
    print(f"  {course_code} - {course_info['name']}")
    print(f"    Grades: {', '.join(map(str, course_info['grades']))}")
    average_grade = student.get_average_grade(course_code)
    if average_grade is not None:
        print(f"    Average Grade: {average_grade:.2f}")
    print()
