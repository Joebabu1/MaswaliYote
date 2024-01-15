import encryption_module

def admin_menu(database):
    while True:
        print("\nMaswaliYote Quiz System - Admin Menu:")
        print(".....................................")
        print("1. Login")
        print("2. Create Quiz")
        print("3. View Quiz")
        print("4. Update Quiz")
        print("5. Delete Quiz")
        print("6. Manage Users")
        print("7. Logout")
        print(".....................................\n")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            admin_username = input("Enter admin username: ")
            admin_password = encryption_module.encrypt_password(input("Enter admin password: "))
            if admin_login(admin_username, admin_password, database):
                break
        elif choice == "2":
            create_quiz(database)
        elif choice == "3":
            view_quiz(database)
        elif choice == "4":
            update_quiz(database)
        elif choice == "5":
            delete_quiz(database)
        elif choice == "6":
            manage_users(database)
        elif choice == "7":
            print("Logging out from MaswaliYote Quiz System - Admin account.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

#def admin_login(username, password, database):
    # Implement secure admin login logic using encryption_module
    # Check the credentials (you may replace this with a database query)
    #for user in database.get_users():
        #if user["username"] == username and user["password"] == password and user["role"] == "admin":
           # print("Admin login successful.")
            #return True
    #print("Invalid credentials. Please try again.")
    #return False


def admin_login(username, password, database):
    # Hardcoded temporary admin credentials for demonstration purposes
    temp_admin_username = "admin"
    temp_admin_password = encryption_module.encrypt_password("admin_password")

    if username == temp_admin_username and password == temp_admin_password:
        print("MaswaliYote Quiz System - Admin login successful.")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False



def create_quiz(database):
    quiz_title = input("Enter the title of the quiz: ")
    questions = []

    while True:
        question_text = input("Enter the question text (or 'done' to finish adding questions): ")
        if question_text.lower() == 'done':
            break

        options = []
        correct_option = None

        for i in range(1, 5):
            option = input(f"Enter option {i}: ")
            options.append(option)

        while True:
            try:
                correct_option = int(input("Enter the number of the correct option (1-4): "))
                if 1 <= correct_option <= 4:
                    break
                else:
                    print("Invalid option. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        questions.append({
            'text': question_text,
            'options': options,
            'correct_option': correct_option
        })

    quiz = {
        'title': quiz_title,
        'questions': questions
    }

    database.add_quiz(quiz)
    print("Quiz created successfully.")

def view_quiz(database):
    quizzes = database.get_quizzes()

    if not quizzes:
        print("No quizzes available.")
        return

    print("\nMaswaliYote Quiz System - Available Quizzes:")
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"{idx}. {quiz['title']}")

    quiz_choice = int(input("Enter the number of the quiz you want to view: "))

    if 1 <= quiz_choice <= len(quizzes):
        quiz = quizzes[quiz_choice - 1]
        print(f"\nQuiz Title: {quiz['title']}")
        print("Questions:")
        for question in quiz['questions']:
            print(f"\n{question['text']}")
            for idx, option in enumerate(question['options'], start=1):
                print(f"{idx}. {option}")
            print(f"Correct Option: {question['correct_option']}")
    else:
        print("Invalid quiz choice. Please try again.")

def update_quiz(database):
    quizzes = database.get_quizzes()

    if not quizzes:
        print("No quizzes available.")
        return

    print("\nMaswaliYote Quiz System - Available Quizzes:")
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"{idx}. {quiz['title']}")

    quiz_choice = int(input("Enter the number of the quiz you want to update: "))

    if 1 <= quiz_choice <= len(quizzes):
        quiz = quizzes[quiz_choice - 1]
        print(f"\nUpdating Quiz: {quiz['title']}")
        
        new_title = input("Enter the new title of the quiz (or press Enter to keep the current title): ")
        if new_title:
            quiz['title'] = new_title

        for question in quiz['questions']:
            print(f"\nUpdating Question: {question['text']}")
            new_text = input("Enter the new text of the question (or press Enter to keep the current text): ")
            if new_text:
                question['text'] = new_text

            print("Updating Options:")
            for i in range(4):
                new_option = input(f"Enter the new option {i + 1} (or press Enter to keep the current option): ")
                if new_option:
                    question['options'][i] = new_option

            while True:
                try:
                    new_correct_option = int(input("Enter the new correct option (1-4, or press Enter to keep the current correct option): "))
                    if new_correct_option and 1 <= new_correct_option <= 4:
                        question['correct_option'] = new_correct_option
                        break
                    elif not new_correct_option:
                        break
                    else:
                        print("Invalid option. Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        database.save_data()
        print("MaswaliYote Quiz System - Quiz updated successfully.")
    else:
        print("Invalid quiz choice. Please try again.")

def delete_quiz(database):
    quizzes = database.get_quizzes()

    if not quizzes:
        print("MaswaliYote Quiz System - No quizzes available.")
        return

    print("\nMaswaliYote Quiz System - Available Quizzes:")
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"{idx}. {quiz['title']}")

    quiz_choice = int(input("Enter the number of the quiz you want to delete: "))

    if 1 <= quiz_choice <= len(quizzes):
        deleted_quiz = quizzes.pop(quiz_choice - 1)
        database.save_data()
        print(f"Quiz '{deleted_quiz['title']}' deleted successfully.")
    else:
        print("Invalid quiz choice. Please try again.")

def manage_users(database):
    while True:
        print("\nMaswaliYote Quiz System - User Management:")
        print("1. Create User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Back to Admin Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_user(database)
        elif choice == "2":
            view_users(database)
        elif choice == "3":
            update_user(database)
        elif choice == "4":
            delete_user(database)
        elif choice == "5":
            print("MaswaliYote Quiz System - Returning to Admin Menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def create_user(database):
    username = input("Enter the username: ")
    password = encryption_module.encrypt_password(input("Enter the password: "))
    role = input("Enter the role (admin/student): ").lower()

    user = {
        'username': username,
        'password': password,
        'role': role
    }

    database.add_user(user)
    print(f"User '{username}' created successfully.")

def view_users(database):
    users = database.get_users()

    if not users:
        print("No users available.")
        return

    print("\nMaswaliYote Quiz System - User List:")
    for user in users:
        print(f"Username: {user['username']}, Role: {user['role']}")

def update_user(database):
    username = input("Enter the username of the user you want to update: ")
    user_index = database.find_user_index(username)

    if user_index is not None:
        print(f"\nUpdating User: {username}")
        new_password = encryption_module.encrypt_password(input("Enter the new password (or press Enter to keep the current password): "))
        new_role = input("Enter the new role (admin/student, or press Enter to keep the current role): ").lower()

        new_data = {}
        if new_password:
            new_data['password'] = new_password
        if new_role:
            new_data['role'] = new_role

        database.update_user(user_index, new_data)
        print(f"User '{username}' updated successfully.")
    else:
        print("User not found. Please try again.")

def delete_user(database):
    username = input("Enter the username of the user you want to delete: ")
    user_index = database.find_user_index(username)

    if user_index is not None:
        deleted_user = database.get_users().pop(user_index)
        database.save_data()
        print(f"User '{deleted_user['username']}' deleted successfully.")
    else:
        print("User not found. Please try again.")
