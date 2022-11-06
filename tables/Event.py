import random
from datetime import timedelta, datetime


def rand_hotel_id(hotels):
    return hotels[random.randrange(len(hotels))].id


def random_date(start, end):
    date_range = ((end - start).days * 3600 * 24) + (end - start).seconds
    random_second = random.randrange(date_range)
    return start + timedelta(seconds=random_second)


def rand_event_date(period, dates, hotel_id):
    event_date = random_date(datetime.strptime(period[0], '%d-%m-%Y %H:%M'),
                             datetime.strptime(period[1], '%d-%m-%Y %H:%M'))
    event_date -= timedelta(hours=event_date.hour, minutes=event_date.minute,
                            seconds=event_date.second) - timedelta(hours=random.randrange(9,21))

    while (hotel_id, event_date.date()) in dates:
        return rand_event_date(period, dates, hotel_id)

    return event_date


class Event:
    def __init__(self, event_id, hotels, period, name, description, event_type, dates):
        self.id = event_id
        self.hotel_id = rand_hotel_id(hotels)
        self.date = rand_event_date(period, dates, self.hotel_id)
        self.name = name
        self.description = description
        self.type = event_type
        self.max_no_of_persons = 10 * random.randrange(2, 11)
        self.no_of_participants = int(float(self.max_no_of_persons) * float(random.randrange(30, 101) / 100))
        dates.append((self.hotel_id, self.date.date()))

    def __str__(self):
        return "%s|%s|%s|%s|%s|%s|%s|%s" % (self.id, self.hotel_id, self.date,
                                            self.name, self.description,
                                            self.type, self.max_no_of_persons,
                                            self.no_of_participants)
