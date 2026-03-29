# auth_service.py

# Import the User model
from models import User

# Import the Validation class
from validation import Validation


class AuthService:

    def __init__(self, file_manager):
        """
        Constructor for the AuthService class.

        file_manager is used to save users,
        load users, and check login information.
        """
        self.file_manager = file_manager

    def register(self):
        print("\n--- Registration In-Process ---")

        # Keep asking for a valid email until one is entered
        while True:
            try:
                email = input("Email: ")
                email = Validation.validate_email(email)

                # Check if the email already exists
                users = self.file_manager.loadUsers()
                for user in users:
                    if user["email"] == email:
                        raise ValueError("Email already exists")

                break
            except ValueError as e:
                print(f"Error: {e}")

        # Keep asking for a valid first name
        while True:
            try:
                first_name = input("First Name: ")
                first_name = Validation.validate_name(first_name)
                break
            except ValueError as e:
                print(f"Error: {e}")

        # Keep asking for a valid last name
        while True:
            try:
                last_name = input("Last Name: ")
                last_name = Validation.validate_name(last_name)
                break
            except ValueError as e:
                print(f"Error: {e}")

        # Keep asking for a valid password
        while True:
            try:
                password = input("Password: ")
                password = Validation.validate_password(password)
                break
            except ValueError as e:
                print(f"Error: {e}")

        # Keep asking for a valid date of birth
        while True:
            try:
                dob = input("Date of Birth (YYYY-MM-DD): ")
                dob = Validation.validate_date(dob)
                break
            except ValueError as e:
                print(f"Error: {e}")

        # Create a new User object
        new_user = User(email, first_name, last_name, password, dob)

        # Save the user as a dictionary
        self.file_manager.saveUser(new_user.to_dict())

        print("Registration Successful\n")

    def login(self):
        print("\n--- Login ---")

        while True:
            try:
                # Ask for login credentials
                email = input("Enter your Email: ")
                email = Validation.validate_email(email)

                password = input("Enter your Password: ")
                password = Validation.validate_password(password)

                # Check whether login is valid
                if self.file_manager.checkLogin(email, password):
                    print("Login Successful\n")

                    # Return the full user dictionary
                    return self.file_manager.getUserByEmail(email)
                else:
                    print("The password or username you've entered is incorrect.")

                # Ask what to do next after failed login
                print("\n1. Try Again")
                print("2. Register")
                print("3. Exit to Main Menu")
                choice = input("Choose an option: ")

                if choice == "1":
                    continue
                elif choice == "2":
                    self.register()
                elif choice == "3":
                    return None
                else:
                    print("Invalid option. Returning to login screen.")

            except ValueError as e:
                print(f"Error: {e}")
