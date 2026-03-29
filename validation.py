import re

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
<<<<<<< HEAD
        return password
=======
        return True
>>>>>>> bad3fdf44974894d018dc4f3333d79061ad43e06
    
    @staticmethod
    def validate_date(date):
        if not date:
            raise ValueError("Date cannot be empty")

    # simple format check: YYYY-MM-DD
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date):
            raise ValueError("Date must be in YYYY-MM-DD format")

    # Split into year, month, day
        year, month, day = map(int, date.split("-"))
<<<<<<< HEAD
        
    # Check valid year
        if year < 1900 or year > 2100:
            raise ValueError("Year must be between 1900 and 2100")
=======
>>>>>>> bad3fdf44974894d018dc4f3333d79061ad43e06

    # Check valid month
        if month < 1 or month > 12:
            raise ValueError("Month must be between 01 and 12")

    # Days in each month
        days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }

    # Check valid day
        if day < 1 or day > days_in_month[month]:
            raise ValueError("Invalid day for the given month")

        return date


    @staticmethod
    def validate_int(value):
        try:
            value = int(value)
            if value <= 0:
                raise ValueError("Value must be positive")
            return value
        except:
            raise ValueError("Value must be an integer")
        return value
