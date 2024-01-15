import json

class Database:
    def __init__(self):
        # Sample data structures for quizzes, student results, and users
        self.quizzes = []
        self.student_results = []
        self.users = []

    def save_data(self):
        # Save quizzes, student results, and users to JSON files
        with open("quizzes.json", "w") as quizzes_file:
            json.dump(self.quizzes, quizzes_file, indent=2)

        with open("student_results.json", "w") as results_file:
            json.dump(self.student_results, results_file, indent=2)

        with open("users.json", "w") as users_file:
            json.dump(self.users, users_file, indent=2)

    def load_data(self):
        # Load quizzes, student results, and users from JSON files
        try:
            with open("quizzes.json", "r") as quizzes_file:
                self.quizzes = json.load(quizzes_file)
        except FileNotFoundError:
            self.quizzes = []

        try:
            with open("student_results.json", "r") as results_file:
                self.student_results = json.load(results_file)
        except FileNotFoundError:
            self.student_results = []

        try:
            with open("users.json", "r") as users_file:
                self.users = json.load(users_file)
        except FileNotFoundError:
            self.users = []

    def get_quizzes(self):
        return self.quizzes

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)
        self.save_data()

    def get_student_results(self):
        return self.student_results

    def add_student_result(self, result):
        self.student_results.append(result)
        self.save_data()

    def get_users(self):
        return self.users

    def add_user(self, user):
        self.users.append(user)
        self.save_data()

    def find_user_index(self, username):
        # Find the index of a user by username
        for idx, user in enumerate(self.users):
            if user["username"] == username:
                return idx
        return None

    def update_user(self, index, new_data):
        # Update user details by index
        self.users[index].update(new_data)
        self.save_data()
