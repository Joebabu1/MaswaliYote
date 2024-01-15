import encryption_module

def student_menu(database):
    while True:
        print("\nMaswaliYote Quiz System - Student Menu:")
        print(".......................................")
        print("1. Login")
        print("2. Take Quiz")
        print("3. View Results")
        print("4. Logout")
        print(".......................................")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            student_username = input("Enter student username: ")
            student_password = encryption_module.encrypt_password(input("Enter student password: "))
            if student_login(student_username, student_password, database):
                break
        elif choice == "2":
            take_quiz(database)
        elif choice == "3":
            view_results(database)
        elif choice == "4":
            print("MaswaliYote Quiz System - Logging out from student account.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def student_login(username, password, database):
    # Implement secure student login logic using encryption_module
    # Check the credentials (you may replace this with a database query)
    for user in database.get_users():
        if user["username"] == username and user["password"] == password and user["role"] == "student":
            print("MaswaliYote Quiz System - Student login successful.")
            return True
    print("Invalid credentials. Please try again.")
    return False

def take_quiz(database):
    # Get available quizzes
    quizzes = database.get_quizzes()

    if not quizzes:
        print("No quizzes available.")
        return

    print("\nMaswaliYote Quiz System - Available Quizzes:")
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"{idx}. {quiz['title']}")

    quiz_choice = int(input("Enter the number of the quiz you want to take: "))

    if 1 <= quiz_choice <= len(quizzes):
        quiz = quizzes[quiz_choice - 1]
        score = conduct_quiz(quiz)
        save_result(database, quiz, score)
    else:
        print("Invalid quiz choice. Please try again.")

def conduct_quiz(quiz):
    score = 0
    print(f"\nTaking Quiz: {quiz['title']}")
    
    for question in quiz['questions']:
        print(f"\nQuestion: {question['text']}")
        
        for idx, option in enumerate(question['options'], start=1):
            print(f"{idx}. {option}")

        answer = int(input("Enter the number of your answer: "))
        correct_answer = question['correct_option']

        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print(f"\nQuiz completed. Your score: {score}/{len(quiz['questions'])}")
    return score

def save_result(database, quiz, score):
    student_username = input("Enter your username: ")
    result = {
        'username': student_username,
        'quiz_title': quiz['title'],
        'score': score
    }
    database.add_student_result(result)
    print("MaswaliYote Quiz System - Result saved successfully.")

def view_results(database):
    student_username = input("Enter your username: ")
    student_results = database.get_student_results()

    print("\nMaswaliYote Quiz System - Your Quiz Results:")
    print("............................................")
    for result in student_results:
        if result['username'] == student_username:
            print(f"Quiz: {result['quiz_title']}, Score: {result['score']}")
    
    if not any(result['username'] == student_username for result in student_results):
        print("No quiz results found for the given username.")
