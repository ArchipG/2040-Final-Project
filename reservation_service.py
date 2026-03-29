# reservation_service.py
from datetime import datetime

# Import the Reservation model
from models import Reservation

# Import the Validation class for checking user input
from validation import Validation

# Import custom exceptions
from exceptions import ReservationError


class ReservationService:
    """
    This class handles all reservation-related operations.
    - viewing reservations
    - making reservations
    - modifying reservations
    - cancelling reservations
    """

    def __init__(self, file_manager):
        """
        file_manager is used to save, load, update,
        and delete reservation data from files.
        """
        self.file_manager = file_manager

    # -------------------------------------------------
    # VIEW RESERVATION
    # -------------------------------------------------

    def view_reservation(self, user):
        """
        Displays all reservations for the logged-in user.
        """
        reservations = self.file_manager.getUserReservations(user["email"])

        if not reservations:
            print("No reservation found")
            return

        print("\n--- Your Reservation(s) ---")

        for index, reservation in enumerate(reservations, start=1):
            print(f"\nReservation {index}")
            print(f"Number of days: {reservation['num_days']}")
            print(f"From Date: {reservation['from_date']}")
            print(f"To Date: {reservation['to_date']}")
            print(f"Number of Persons: {reservation['num_persons']}")
            print(f"Number of Rooms: {reservation['num_rooms']}")


    # MAKE RESERVATIO
    def make_reservation(self, user):
        """
        Creates a new reservation for the logged-in user.
        """
        print("\n--- Make Reservation ---")

        # Get and validate from date
        while True:
            try:
                from_date = input("From Date (YYYY-MM-DD): ")
                from_date = Validation.validate_date(from_date)
                break
            except ValueError as e:
                print(e)

        # Get and validate to date
        while True:
            try:
                to_date = input("To Date (YYYY-MM-DD): ")
                to_date = Validation.validate_date(to_date)
                break
            except ValueError as e:
                print(e)

        # convert to datetime objects
        from_date_obj = datetime.strptime(from_date, "%Y-%m-%d").date()
        to_date_obj = datetime.strptime(to_date, "%Y-%m-%d").date()

        num_days = (to_date_obj - from_date_obj).days

        if num_days <= 0:
            print("To date must be after from date")
            return

        # Get and validate number of persons
        while True:
            try:
                num_persons = input("Number of Persons: ")
                num_persons = Validation.validate_int(num_persons)
                break
            except ValueError as e:
                print(e)

        # Get and validate number of rooms
        while True:
            try:
                num_rooms = input("Number of Rooms: ")
                num_rooms = Validation.validate_int(num_rooms)
                break
            except ValueError as e:
                print(e)

        # Create a Reservation object using the logged-in user's email
        new_reservation = Reservation(
            user["email"],
            num_days,
            from_date,
            to_date,
            num_persons,
            num_rooms
        )

        # Save the reservation as a dictionary in the file
        self.file_manager.saveReservation(new_reservation.to_dict())

        print("Reservation saved successfully.")



    # MODIFY RESERVATION
    def modify_reservation(self, user):
        """
        Modifies the logged-in user's existing reservation.
        If no reservation exists, an error message is shown.
        """
        reservations = self.file_manager.getUserReservations(user["email"])

        if not reservations:
            print("No reservation found")
            return

        # For simplicity, modify the first reservation found
        current_reservation = reservations[0]

        print("\n--- Current Reservation ---")
        print(f"Number of days: {current_reservation['num_days']}")
        print(f"From Date: {current_reservation['from_date']}")
        print(f"To Date: {current_reservation['to_date']}")
        print(f"Number of Persons: {current_reservation['num_persons']}")
        print(f"Number of Rooms: {current_reservation['num_rooms']}")

        print("\n--- Enter Updated Reservation Details ---")

        # Get and validate updated from date
        while True:
            try:
                from_date = input("From Date (YYYY-MM-DD): ")
                from_date = Validation.validate_date(from_date)
                break
            except ValueError as e:
                print(e)

        # Get and validate updated to date
        while True:
            try:
                to_date = input("To Date (YYYY-MM-DD): ")
                to_date = Validation.validate_date(to_date)
                break
            except ValueError as e:
                print(e)

        # convert to datetime objects
        from_date_obj = datetime.strptime(from_date, "%Y-%m-%d").date()
        to_date_obj = datetime.strptime(to_date, "%Y-%m-%d").date()

        num_days = (to_date_obj - from_date_obj).days

        if num_days <= 0:
            print("To date must be after from date")
            return

        # Get and validate updated number of persons
        while True:
            try:
                num_persons = input("Number of Persons: ")
                num_persons = Validation.validate_int(num_persons)
                break
            except ValueError as e:
                print(e)

        # Get and validate updated number of rooms
        while True:
            try:
                num_rooms = input("Number of Rooms: ")
                num_rooms = Validation.validate_int(num_rooms)
                break
            except ValueError as e:
                print(e)

        # Create the updated reservation object
        updated_reservation = Reservation(
            user["email"],
            num_days,
            from_date,
            to_date,
            num_persons,
            num_rooms
        )

        try:
            # Update the user's reservation in the file
            self.file_manager.updateReservation(user["email"], updated_reservation.to_dict())
            print("Reservation updated successfully.")
        except ReservationError as e:
            print(e)


    # CANCEL RESERVATION
   
    def cancel_reservation(self, user):
        """
        Cancels the logged-in user's reservation.
        If no reservation is found, an error message is shown.
        """
        try:
            self.file_manager.deleteReservation(user["email"])
            print("Reservation cancelled successfully.")
        except ReservationError as e:
            print(e)
