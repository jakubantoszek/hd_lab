from utils import *


class Hotel:
    def __init__(self, hotel_id, address):
        self.id = hotel_id
        self.city = address[0]
        self.street = address[1]
        self.building_number = random_building_number()
        self.stars = random_stars()

    def __str__(self):
        return "%s|%s|%s|%s|%s" % (self.id, self.city, self.street,
                                   self.building_number, self.stars)
