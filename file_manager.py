# Import json so we can store data in JSON files
import json

# Import the custom exception classes
from exceptions import AuthenticationError, ReservationError


class FileManager:
    """
    This class handles all file operations for the project.

    - saving users
    - loading users
    - checking login
    - saving reservations
    - loading reservations
    - updating reservations
    - deleting reservations
    """

    def __init__(self, user_file="users.json", reservation_file="reservations.json"):
        """
        Constructor for the FileManager class.

        user_file stores registered users.
        reservation_file stores all reservations.
        """
        self.user_file = user_file
        self.reservation_file = reservation_file



    def _load_data(self, filename):
        """
        helper method to load data from a JSON file.

        If the file does not exist or is empty,
        it returns an empty list.
        """
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def _save_data(self, filename, data):
        """
        helper method to save data to a JSON file.

        It writes the full list of data into the file.
        """
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)


    def saveUser(self, user_data):
        """
        Saves a new user to the users file.
        """
        users = self._load_data(self.user_file)
        users.append(user_data)
        self._save_data(self.user_file, users)

    def loadUsers(self):
        """
        Loads and returns all users from the users file.
        """
        return self._load_data(self.user_file)

    def checkLogin(self, email, password):
        """
        Checks if the given email and password match
        a registered user.
        Returns True if login is good.
       
        """
        users = self.loadUsers()

        for user in users:
            if user["email"] == email and user["password"] == password:
                return True

        return False

    def getUserByEmail(self, email):
        """
        Finds and returns a user dictionary by email.
        If the user does not exist, return None.
        """
        users = self.loadUsers()

        for user in users:
            if user["email"] == email:
                return user

        return None

    def saveReservation(self, reservation_data):
        """
        Saves a new reservation to the reservation file.
        """
        reservations = self._load_data(self.reservation_file)
        reservations.append(reservation_data)
        self._save_data(self.reservation_file, reservations)

    def loadReservations(self):
        """
        Loads and returns all reservations from the reservation file.
        """
        return self._load_data(self.reservation_file)

    def getUserReservations(self, email):
        """
        Returns all reservations that belong to the given email.
        """
        reservations = self.loadReservations()
        user_reservations = []

        for reservation in reservations:
            if reservation["email"] == email:
                user_reservations.append(reservation)

        return user_reservations

    def updateReservation(self, email, updated_reservation):
        """
        Updates the first reservation found for the given email.
        Raises ReservationError if no reservation is found.
        """
        reservations = self.loadReservations()
        updated = False

        for i in range(len(reservations)):
            if reservations[i]["email"] == email:
                reservations[i] = updated_reservation
                updated = True
                break

        if not updated:
            raise ReservationError("No reservation found to update.")

        self._save_data(self.reservation_file, reservations)

    def deleteReservation(self, email):
        """
        Deletes the first reservation found.
        Raises ReservationError if no reservation is found.
        """
        reservations = self.loadReservations()
        new_reservations = []
        deleted = False

        for reservation in reservations:
            if reservation["email"] == email and not deleted:
                deleted = True
            else:
                new_reservations.append(reservation)

        if not deleted:
            raise ReservationError("No reservation found to delete.")

        self._save_data(self.reservation_file, new_reservations)
