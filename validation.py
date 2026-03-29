import re

class Validation:

    @staticmethod
    def validate_email(email):
        if not email:
            raise ValueError("Email cannot be empty")
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise ValueError("Invalid email format")
        return True

    @staticmethod
    def validate_name(name):
        if not name:
            raise ValueError("Name cannot be empty")
        if not name.isalpha():
            raise ValueError("Name must contain only letters")
        return True

    @staticmethod
    def validate_password(password):
        if not password:
            raise ValueError("Password cannot be empty")
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters")
        return True

    @staticmethod
    def validate_date(date):
        if not date:
            raise ValueError("Date cannot be empty")
        # simple format check: YYYY-MM-DD
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date):
            raise ValueError("Date must be in YYYY-MM-DD format")
        return True

    @staticmethod
    def validate_int(value):
        try:
            value = int(value)
            if value <= 0:
                raise ValueError("Value must be positive")
        except:
            raise ValueError("Value must be an integer")
        return True
