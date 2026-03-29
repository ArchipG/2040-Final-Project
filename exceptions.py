class InvalidInputError(Exception):
    """Raised when user input is blank or of the wrong type."""
    pass


class AuthenticationError(Exception):
    """Raised when login credentials are incorrect."""
    pass


class ReservationError(Exception):
    """Raised when reservation-related actions fail."""
    pass
