from utils import *


def rand_capacity(capacities):
    val = random.randrange(len(capacities))
    result = capacities[val]
    del capacities[val]
    return result


def calculate_price(hotel_stars, capacity):
    return capacity * (hotel_stars - 1) * 100


class Room:
    def __init__(self, hotel, number, text):
        if text is None:
            self.hotel_id = hotel.id
            self.number = number
            self.room_type_id = random.randrange(1, 4)
            self.is_occupied = False
            self.max_no_of_guests = rand_capacity(hotel.rooms_capacity)
            self.price = calculate_price(hotel.stars, self.max_no_of_guests)
        else:
            values = text.split('|')
            self.hotel_id = values[0]
            self.number = values[1]
            self.room_type_id = values[2]
            self.is_occupied = values[3]
            self.max_no_of_guests = values[4]
            self.price = values[5]

    def __str__(self):
        return "%s|%s|%s|%s|%s|%s" % (self.hotel_id, self.number, self.room_type_id,
                                      int(self.is_occupied), self.max_no_of_guests, self.price)
