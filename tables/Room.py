import random

from utils import *


def rand_capacity(capacities):
    val = random.randrange(len(capacities))
    result = capacities[val]
    del capacities[val]
    return result


def calculate_price(hotel_stars, capacity):
    return capacity * (hotel_stars - 1) * 100


class Room:
    def __init__(self, hotel, number, capacities):
        self.hotel_id = hotel.id
        self.number = number
        self.room_type_id = random.randrange(1, 4)
        self.is_occupied = random_is_occupied()
        self.max_no_of_guests = rand_capacity(capacities)
        self.price = calculate_price(hotel.stars, self.max_no_of_guests)

    def __str__(self):
        return "%s|%s|%s|%s|%s|%s" % (self.hotel_id, self.number, self.room_type_id,
                                      self.is_occupied, self.max_no_of_guests, self.price)
