from utils import *


class Guest:
    def __init__(self, guest_id, numbers, mails):
        self.id = guest_id
        self.phone_number = random_phone_number(numbers)
        self.name = random_name()
        self.surname = random_surname()
        self.email = random_email(self.name, self.surname, mails, False)

    def __str__(self):
        return "%s|%s|%s|%s|%s" % (self.id, self.phone_number, self.name, self.surname, self.email)
