from utils import *

def get_gender(name):
    if name[-1] == 'a':
        return 'female'
    return 'male'


class Worker:
    def __init__(self, worker_id, numbers, mails, text):
        if text is None:
            self.id = worker_id + 1
            self.phone_number = random_phone_number(numbers)
            self.gender = rand_gender()
            self.name = random_name(self.gender)
            self.surname = random_surname(self.gender)
            self.email = random_email(self.name, self.surname, mails, True)
            self.position = random_position()
        else:
            values = text.split('|')
            self.id = values[0]
            self.phone_number = values[4]
            self.name = values[1]
            self.surname = values[2]
            self.gender = get_gender(self.name)
            self.email = values[3]
            self.position = values[5]

    def __str__(self):
        return "%s|%s|%s|%s|%s|%s" % (self.id, self.name, self.surname, self.email, self.phone_number, self.position)
