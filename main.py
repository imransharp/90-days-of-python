from services.student_service import StudentService

def main():
    service = StudentService()

    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            try:
                service.add_student(name, int(age), grade)
            except ValueError:
                print("❌ Invalid age. Please enter a number.")

        elif choice == "2":
            service.display_students()

        elif choice == "3":
            name = input("Enter student name to search: ")
            service.search_student(name)

        elif choice == "4":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
