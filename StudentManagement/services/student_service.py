from models.student import Student
import json
import os

DATA_FILE = "data/students.json"

class StudentService:
    """
    Handles student operations like add, display, and search.
    """
    def __init__(self):
        # Ensure the data file exists
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as file:
                json.dump([], file)

    def add_student(self, name, age, grade):
        """
        Adds a new student to the JSON file.
        """
        student = Student(name, age, grade)
        students = self.load_students()
        students.append(student.to_dict())
        self.save_students(students)
        print(f"✅ Student '{name}' added successfully!")

    def load_students(self):
        """
        Loads students from the JSON file.
        """
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self, students):
        """
        Saves students to the JSON file.
        """
        with open(DATA_FILE, "w") as file:
            json.dump(students, file, indent=4)

    def display_students(self):
        """
        Displays all students.
        """
        students = self.load_students()
        if not students:
            print("❌ No students found.")
            return
        print("\n📋 All Students:")
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

    def search_student(self, name):
        """
        Searches for a student by name.
        """
        students = self.load_students()
        for student in students:
            if student['name'].lower() == name.lower():
                print(f"🔍 Found: Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
                return
        print(f"❌ Student '{name}' not found.")
