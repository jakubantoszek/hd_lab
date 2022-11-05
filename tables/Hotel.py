from utils import *


class Hotel:
    def __init__(self, hotel_id, address, text):
        if text is None:
            self.id = hotel_id
            self.city = address[0]
            self.street = address[1]
            self.building_number = random_building_number()
            self.stars = random_stars()

            self.no_of_rooms = rand_hotels_capacity()
            self.rooms_capacity = get_hotel_rooms_capacities(self.no_of_rooms)
        else:
            values = text.split('|')
            self.id = values[0]
            self.city = values[1]
            self.street = values[2]
            self.building_number = values[3]
            self.stars = values[4]

            self.no_of_rooms = 0
            self.rooms_capacity = 0

    def __str__(self):
        return "%s|%s|%s|%s|%s" % (self.id, self.city, self.street,
                                   self.building_number, self.stars)
