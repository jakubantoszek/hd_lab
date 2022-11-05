from tables.Guest import Guest
from tables.Hotel import Hotel
from tables.Reservation import Reservation
from tables.ReservationDetails import ReservationDetails
from tables.ReservationService import ReservationService
from tables.Worker import Worker
from tables.Room import Room


def read_guests():
    guests = []
    with open('bulk/guest.bulk') as file:
        content = file.readlines()
        for line in content:
            guests.append(Guest(None, None, None, line.replace('\n', '')))

    return guests


def read_hotels():
    hotels = []
    with open('bulk/hotel.bulk') as file:
        content = file.readlines()
        for line in content:
            hotels.append(Hotel(None, None, line.replace('\n', '')))

    return hotels


def read_reservations():
    reservations = []
    with open('bulk/reservation.bulk') as file:
        content = file.readlines()
        for line in content:
            reservations.append(Reservation(None, None, None, None, line.replace('\n', '')))

    return reservations


def read_reservations_details():
    reservations_details = []
    with open('bulk/reservation_details.bulk') as file:
        content = file.readlines()
        for line in content:
            reservations_details.append(ReservationDetails(None, None, None, line.replace('\n', '')))

    return reservations_details


def read_reservations_service():
    reservations_service = []
    with open('bulk/reservation_service.bulk') as file:
        content = file.readlines()
        for line in content:
            reservations_service.append(ReservationService(None, None, line.replace('\n', '')))

    return reservations_service


def read_rooms():
    rooms = []
    with open('bulk/room.bulk') as file:
        content = file.readlines()
        for line in content:
            rooms.append(Room(None, None, line.replace('\n', '')))

    return rooms


def read_workers():
    workers = []
    with open('bulk/worker.bulk') as file:
        content = file.readlines()
        for line in content:
            workers.append(Worker(None, None, None, line.replace('\n', '')))

    return workers
