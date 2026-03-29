import re
from datetime import datetime, date

class Validation:

    @staticmethod
    def validate_email(email):
        if not email:
            raise ValueError("Email cannot be empty")

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise ValueError("Invalid email format")

        return email

    @staticmethod
    def validate_name(name):
        if not name:
            raise ValueError("Name cannot be empty")
        if not name.isalpha():
            raise ValueError("Name must contain only letters")

        return name

    @staticmethod
    def validate_password(password):
        if not password:
            raise ValueError("Password cannot be empty")
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters")

        return password

    @staticmethod
    def validate_future_date(date_str):
        if not date_str:
            raise ValueError("Date cannot be empty")

        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date_str):
            raise ValueError("Date must be in YYYY-MM-DD format")

        try:
            parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid calendar date")

        today = date.today()

        if parsed_date < today:
            raise ValueError("Date cannot be in the past")

        return date_str

    @staticmethod
    def validate_dob(date_str):
        if not date_str:
            raise ValueError("Date cannot be empty")

        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date_str):
            raise ValueError("Date must be in YYYY-MM-DD format")

        try:
            parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid calendar date")

        today = date.today()

        if parsed_date > today:
            raise ValueError("Date of birth cannot be in the future")

        return date_str

    @staticmethod
    def validate_int(value):
        try:
            value = int(value)
        except:
            raise ValueError("Value must be an integer")

        if value <= 0:
            raise ValueError("Value must be positive")

        return value
