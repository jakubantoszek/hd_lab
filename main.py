from utils import *
from create_data import *

if __name__ == '__main__':
    get_names()
    get_surnames()
    set_positions()
    phones = []
    mails = []
    dates_dict = {}

    T0 = '01-01-2020 00:00'
    T1 = '01-04-2020 00:00'
    T2 = '01-07-2020 00:00'

    guests = create_guest_table(phones, mails)
    workers = create_worker_table(phones, mails)
    positions_dict = assign_workers_to_positions(workers)

    reservations = create_reservation_table(guests, [T0, T1])
    create_reservation_service_table(positions_dict, reservations)

    hotels = create_hotel_table()
    rooms = create_room_table(hotels)
    rooms_dict = assign_rooms_to_hotels(hotels, rooms, dates_dict)
    create_reservation_details_table(reservations, rooms_dict, dates_dict, [T0, T1])
