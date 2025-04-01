import json
import os

class Student:
    """
    Represents a student with a name, age, and grade.
    """
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        """
        Converts the student object to a dictionary.
        """
        return {
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        """
        Creates a Student object from a dictionary.
        """
        return Student(data["name"], data["age"], data["grade"])
