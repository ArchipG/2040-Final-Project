# menu.py

# Import the service classes used in the menu system
from auth_service import AuthService
from reservation_service import ReservationService


class Menu:
    """
    This class controls the menu system of the program.
    - displaying the main menu
    - displaying the user menu after login
    - calling the correct service methods based on user choice
    """

    def __init__(self, file_manager):
        """
        It creates objects for:
        - authentication services
        - reservation services
        """
        self.file_manager = file_manager
        self.auth_service = AuthService(file_manager)
        self.reservation_service = ReservationService(file_manager)


    def display_main_menu(self):
        """
        Displays the main menu and keeps the program running
        until the user selects Exit.
        """
        while True:
            print("\n")
            print(" Welcome to the Reservation Maker ")
            print("")
            print("1. Register / Signup")
            print("2. Login")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                # Start the registration process
                self.auth_service.register()

            elif choice == "2":
                # Start the login process
                logged_in_user = self.auth_service.login()

                # If login is successful, move to the user menu
                if logged_in_user is not None:
                    self.display_user_menu(logged_in_user)

            elif choice == "3":
                # Exit message required by the assignment
                print("Thank you for using our Reservation System")
                break

            else:
                print("Invalid choice. Please select 1, 2, or 3.")


    def display_user_menu(self, user):
        """
        Displays the menu shown after successful login.

        The logged-in user can:
        - view reservation
        - make reservation
        - modify reservation
        - cancel reservation
        - logout
        """
        while True:
            print("\n")
            print(f" Welcome, {user['first_name']} ")
            print("")
            print("1. View Reservation")
            print("2. Make Reservation")
            print("3. Modify Reservation")
            print("4. Cancel Reservation")
            print("5. Logout")

            choice = input("Choose an option: ")

            if choice == "1":
                # View the user's reservation(s)
                self.reservation_service.view_reservation(user)

            elif choice == "2":
                # Make a new reservation
                self.reservation_service.make_reservation(user)

            elif choice == "3":
                # Modify an existing reservation
                self.reservation_service.modify_reservation(user)

            elif choice == "4":
                # Cancel an existing reservation
                self.reservation_service.cancel_reservation(user)

            elif choice == "5":
                # Logout and return to the main menu
                print("You have been logged out.")
                break

            else:
                print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
