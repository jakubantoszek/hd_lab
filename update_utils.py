import random
from datetime import datetime

from tables.Reservation import Reservation
from tables.ReservationDetails import ReservationDetails


def get_emails(workers, guests):
    emails = []
    for worker in workers:
        emails.append(worker.email)

    for guest in guests:
        emails.append(guest.email)

    return emails


def get_numbers(workers, guests):
    numbers = []
    for worker in workers:
        numbers.append(worker.phone_number)

    for guest in guests:
        numbers.append(guest.phone_number)

    return numbers


def update_bulk_file(class_name, values):
    directory = 'bulk/'
    with open(directory + class_name + '_update.bulk', 'w') as f:
        f.write(str(values[0]))
        for val in values[1:]:
            f.write('\n' + str(val))


def rand_children_and_adults_change(children, adults):
    if adults == 1:
        return adults, children - 1
    if random.random() < 0.5:
        return adults - 1, children
    else:
        return adults, children - 1


def rand_children_and_adults_change2(children, adults):
    if random.random() < 0.5:
        return adults + 1, children
    else:
        return adults, children + 1


def get_no_of_reservations(reservesation_chances):
    val = random.random()
    for key in reservesation_chances:
        if val < key:
            return reservesation_chances[key]


def get_all_dates_of_reservations(reservations_list):
    dates = []
    for res in reservations_list:
        dates.append((res.check_in_date, res.check_out_date))

    return dates


def update_reservation_table(guests, period, reservations, list_of_old_guests, list_of_new_guests):
    dates = get_all_dates_of_reservations(reservations)

    for i in range(len(list_of_new_guests)):
        no_of_reservations = get_no_of_reservations({0.8: 1, 0.9: 2, 0.95: 3, 0.99: 4, 1: 5})

        for j in range(no_of_reservations):
            reservation = Reservation(len(reservations) + 1, list_of_new_guests[i].id, period, dates, None, 0)
            reservations.append(reservation)

    for i in range(len(list_of_old_guests)):
        no_of_reservations = get_no_of_reservations({0.85: 0, 0.98: 1, 1: 2})

        for j in range(no_of_reservations):
            reservation = Reservation(len(reservations) + 1, list_of_old_guests[i].id, period, dates, None, 0)
            reservations.append(reservation)


def rand_no_of_reservated_rooms():
    val = random.random()
    if val < 0.75:
        return 1
    elif val < 0.90:
        return 2
    elif val < 0.97:
        return 3
    return 4


def wrong_room(reservation, room_reservations):
    ret = False

    for res in room_reservations:
        if max(res.check_in_date, reservation.check_in_date) <= \
                min(res.check_out_date, reservation.check_out_date):
            ret = True

    return ret


def update_reservation_details_table(reservations, rooms_dict, dictionary, period, details):
    for res in reservations:
        no_of_rooms = rand_no_of_reservated_rooms()
        hotel_id = list(rooms_dict.keys())[random.randrange(len(rooms_dict.keys()))]

        for _ in range(no_of_rooms):
            hotel_rooms = rooms_dict[hotel_id]
            room = hotel_rooms[random.randrange(len(hotel_rooms))]

            x = 0
            while wrong_room(res, dictionary[(hotel_id, room.number)]):
                if x % 2 == 0:
                    room = hotel_rooms[random.randrange(len(hotel_rooms))]
                else:
                    res.reservation_date, res.check_in_date, res.check_out_date = res.rand_dates(period, 0)
                x += 1

            reservation_details = ReservationDetails(res, hotel_id, room, None)
            dictionary[(hotel_id, room.number)].append(res)

            if res.check_in_date < datetime.strptime(period[1], '%d-%m-%Y %H:%M') < res.check_out_date:
                room.is_occupied = True

            details.append(reservation_details)


def get_object_from_reservation_id(res_id, reservations):
    return reservations[int(res_id) - 1]


def assign_dates_to_rooms(dictionary, reservation_details, reservations):
    for details in reservation_details:
        res = get_object_from_reservation_id(details.reservation_id, reservations)
        dictionary[(details.hotel_id, details.room_number)].append(res)
