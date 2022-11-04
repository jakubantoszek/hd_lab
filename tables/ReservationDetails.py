import random


def rand_children_and_adults(room_capacity):
    adults = random.randrange(1, room_capacity + 1)
    children = room_capacity - adults

    if room_capacity == 1:
        return adults, children

    if random.random() < 0.5:
        if children == 0 or adults == 1:
            return adults, children
        if random.random() < 0.5:
            return adults - 1, children
        else:
            return adults, children - 1
    return adults, children


class ReservationDetails:
    def __init__(self, reservation, hotel_id, room):
        self.reservation_id = reservation.id
        self.hotel_id = hotel_id
        self.room_number = room.number
        self.no_of_adults, self.no_of_children = rand_children_and_adults(room.max_no_of_guests)
        self.check_in_date = reservation.check_in_date
        self.check_out_date = reservation.check_out_date

    def __str__(self):
        return "%s|%s|%s|%s|%s|%s|%s" % (self.reservation_id, self.hotel_id, self.room_number,
                                         self.no_of_adults, self.no_of_children, self.check_in_date,
                                         self.check_out_date)
