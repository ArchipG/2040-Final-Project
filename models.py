class User:
    def __init__(self, email, first_name, last_name, password, dob):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.dob = dob

    def to_dict(self):
        return {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "dob": self.dob
        }


class Reservation:
    def __init__(self, email, num_days, from_date, to_date, num_persons, num_rooms):
        self.email = email
        self.num_days = num_days
        self.from_date = from_date
        self.to_date = to_date
        self.num_persons = num_persons
        self.num_rooms = num_rooms

    def to_dict(self):
        return {
            "email": self.email,
            "num_days": self.num_days,
            "from_date": self.from_date,
            "to_date": self.to_date,
            "num_persons": self.num_persons,
            "num_rooms": self.num_rooms
        }
