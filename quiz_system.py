import admin_module
import student_module
from database import Database
import encryption_module

def main():
    database = Database()
    database.load_data()

    while True:
        print("\nWelcome to MaswaliYote Quiz Management System:")
        print("..............................................")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Exit")
        print("..............................................\n")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            admin_username = input("Enter admin username: ")
            admin_password = encryption_module.encrypt_password(input("Enter admin password: "))
            if admin_module.admin_login(admin_username, admin_password, database):
                admin_module.admin_menu(database)
        elif choice == "2":
            student_username = input("Enter student username: ")
            student_password = encryption_module.encrypt_password(input("Enter student password: "))
            if student_module.student_login(student_username, student_password, database):
                student_module.student_menu(database)
        elif choice == "3":
            database.save_data()
            print("Exiting MaswaliYote Quiz System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
