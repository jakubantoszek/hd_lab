from utils import *


class Worker:
    def __init__(self, worker_id, numbers, mails):
        self.id = worker_id + 1
        self.phone_number = random_phone_number(numbers)
        self.name = random_name()
        self.surname = random_surname()
        self.email = random_email(self.name, self.surname, mails, True)
        self.position = random_position()

    def __str__(self):
        return "%s|%s|%s|%s|%s" % (self.id, self.phone_number, self.name, self.surname, self.email)
