from update import *

if __name__ == '__main__':
    guests = read_guests()
    workers = read_workers()
    reservations = read_reservations()
    reservation_service = read_reservations_service()
    hotels = read_hotels()
    rooms = read_rooms()
    reservation_details = read_reservations_details()
    prev_mails = get_emails(workers, guests)
    prev_numbers = get_numbers(workers, guests)
    positions_dict = assign_workers_to_positions(workers)

    dictionary = {'guest': guests, 'worker': workers, 'reservation': reservations,
                  'reservation_service': reservation_service, 'hotel': hotels,
                  'room': rooms, 'reservation_details': reservation_details}

    update(dictionary, prev_mails, prev_numbers, positions_dict)
    for key in dictionary:
        update_bulk_file(key, dictionary[key])
