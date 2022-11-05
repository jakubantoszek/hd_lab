import random

from tables.Guest import Guest
from tables.Hotel import Hotel
from tables.Reservation import Reservation
from tables.ReservationDetails import ReservationDetails
from tables.ReservationService import ReservationService
from tables.Worker import Worker
from tables.Room import Room
from datetime import datetime

reservesation_chances = {0.8: 1, 0.9: 2, 0.95: 3, 0.99: 4, 1: 5}


def create_guest_table(phones, mails, guests, number, start_id):
    # for i in range(5000):
    for i in range(number):
        guest = Guest(i + 1 + start_id, phones, mails, None)
        phones.append(guest.phone_number)
        mails.append(guest.email)
        guests.append(guest)


def create_hotel_table(hotels_list, hotels):
    for i in range(len(hotels)):
        hotel = Hotel(i + 1, hotels[i], None)
        hotels_list.append(hotel)


def create_worker_table(phones, mails, workers, number, start_id):
    for j in range(number):
        worker = Worker(j + start_id, phones, mails, None)
        phones.append(worker.phone_number)
        mails.append(worker.email)
        workers.append(worker)


def create_room_table(hotels, rooms):
    for i in range(1, len(hotels) + 1):
        for j in range(hotels[i - 1].no_of_rooms):
            room = Room(hotels[i - 1], j + 1, None)
            rooms.append(room)


def get_no_of_reservations():
    val = random.random()
    for key in reservesation_chances:
        if val < key:
            return reservesation_chances[key]

    return 5


def create_reservation_table(guests, period, reservations):
    for i in range(len(guests)):
        dates = []
        no_of_reservations = get_no_of_reservations()

        for j in range(no_of_reservations):
            reservation = Reservation(len(reservations) + 1 + len(reservations), guests[i].id, period, dates, None, 194)
            reservations.append(reservation)


def random_cleaners(cleaners):
    cl_1 = random.randrange(len(cleaners))
    cl_2 = random.randrange(len(cleaners))

    if cl_1 == cl_2:
        return random_cleaners(cleaners)

    return cl_1, cl_2


def create_reservation_service_table(positions_dict, reservations, services):
    for res in reservations:
        cleaner1, cleaner2 = random_cleaners(positions_dict['osoba sprzatajaca'])
        chambermaid = random.randrange(len(positions_dict['pokojowy']))
        managing_person = random.randrange(len(positions_dict['osoba zarzadzajaca']))

        reservation_workers = [positions_dict['osoba sprzatajaca'][cleaner1],
                               positions_dict['osoba sprzatajaca'][cleaner2],
                               positions_dict['pokojowy'][chambermaid],
                               positions_dict['osoba zarzadzajaca'][managing_person]]

        for worker in reservation_workers:
            reservation_service = ReservationService(res.id, worker.id, None)
            services.append(reservation_service)


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


def create_reservation_details_table(reservations, rooms_dict, dictionary, period, details):
    for res in reservations:
        no_of_rooms = rand_no_of_reservated_rooms()
        hotel_id = list(rooms_dict.keys())[random.randrange(len(rooms_dict.keys()))]

        for _ in range(no_of_rooms):
            hotel_rooms = rooms_dict[hotel_id]
            room = hotel_rooms[random.randrange(len(hotel_rooms))]

            while wrong_room(res, dictionary[(hotel_id, room.number)]):
                room = hotel_rooms[random.randrange(len(hotel_rooms))]

            reservation_details = ReservationDetails(res, hotel_id, room, None)
            dictionary[(hotel_id, room.number)].append(res)

            if res.check_in_date < datetime.strptime(period[1], '%d-%m-%Y %H:%M') < res.check_out_date:
                room.is_occupied = True

            details.append(reservation_details)
