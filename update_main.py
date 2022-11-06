from update import *
from excel import *

if __name__ == '__main__':
    get_names()
    get_surnames()
    set_positions([4000, 2000, 1000])

    events = []
    T1 = '01-04-2020 00:00'
    T2 = '01-07-2020 00:00'

    hotels = read_hotels()
    # excel_main(hotels, [T1, T2], events, 1000)

    guests = read_guests()
    workers = read_workers()
    positions_dict = assign_workers_to_positions(workers)

    reservations = read_reservations()
    no_of_old_reservations = len(reservations)
    reservation_service = read_reservations_service()
    rooms = read_rooms()
    reservation_details = read_reservations_details()
    prev_mails = get_emails(workers, guests)
    prev_numbers = get_numbers(workers, guests)

    dictionary = {'guest': guests, 'worker': workers, 'reservation': reservations,
                  'reservation_service': reservation_service, 'hotel': hotels,
                  'room': rooms, 'reservation_details': reservation_details}

    update(dictionary, prev_mails, prev_numbers, positions_dict)
    inserts(dictionary, prev_mails, prev_numbers, no_of_old_reservations)
    for key in dictionary:
        update_bulk_file(key, dictionary[key])
