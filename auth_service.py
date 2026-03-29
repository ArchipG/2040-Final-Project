from models import User
from validation import Validation


class AuthService:
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def register(self):
        print("\n--- Registration In-Process ---")

        while True:
            try:
                email = input("Email: ")
                Validation.validate_email(email)

                first_name = input("First Name: ")
                Validation.validate_name(first_name)

                last_name = input("Last Name: ")
                Validation.validate_name(last_name)

                password = input("Password: ")
                Validation.validate_password(password)

                dob = input("Date of Birth (YYYY-MM-DD): ")
                Validation.validate_date(dob)

                # check duplicate email
                users = self.file_manager.loadUsers()
                for user in users:
                    if user["email"] == email:
                        raise ValueError("Email already exists")

                new_user = User(email, first_name, last_name, password, dob)
                self.file_manager.saveUser(new_user.to_dict())

                print("Registration Successful\n")
                break

            except Exception as e:
                print(f"Error: {e}")
                print("Please try again.\n")

    def login(self):
        print("\n--- Login ---")

        while True:
            try:
                email = input("Enter your Email: ")
                password = input("Enter your Password: ")

                if self.file_manager.checkLogin(email, password):
                    print("Login Successful\n")
                    return email  # return logged-in user email
                else:
                    print("Incorrect email or password")

                choice = input("Try again (1), Register (2), Exit (3): ")

                if choice == "1":
                    continue
                elif choice == "2":
                    self.register()
                elif choice == "3":
                    return None
                else:
                    print("Invalid option")

            except Exception as e:
                print(f"Error: {e}")
