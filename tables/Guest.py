from utils import *


class Guest:
    def __init__(self, no_of_guests):
        self.id = no_of_guests + 1
        self.phone_number = random_phone_number()
        self.name = random_name()
        self.surname = random_surname()
        self.email = random_email(self.name, self.surname)

