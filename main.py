from utils import *
from create_data import *
from excel import *

if __name__ == '__main__':
    get_names()
    get_surnames()
    set_positions([40000, 20000, 10000])

    phones = []
    mails = []
    dates_dict = {}
    hotels_const = [['Warszawa', 'Łazienkowska'], ['Warszawa', 'Złota'], ['Warszawa', 'Toruńska'],
                    ['Gdańsk', 'Toruńska'], ['Gdańsk', 'Grunwaldzka'], ['Gdynia', 'Świętojańska'],
                    ['Gdynia', 'Legionów'], ['Łeba', 'Nadmorska'], ['Wrocław', 'Osobowicka'],
                    ['Poznań', 'Koralowa'], ['Lublin', 'Szafirowa'], ['Kraków', 'Kasztanowa'],
                    ['Gliwice', 'Akademicka'], ['Katowice', '11 Listopada'], ['Świdnik', 'Kopernika'],
                    ['Łódź', 'Bandurskiego'], ['Szczecin', '26 Kwietnia'], ['Toruń', 'św. Józefa'],
                    ['Rzeszów', '3 Maja'], ['Kielce', 'Sienkiewicza']]

    guests = []
    workers = []
    reservations = []
    reservation_service = []
    hotels = []
    rooms = []
    reservation_details = []
    events = []

    T0 = '01-01-2020 00:00'
    T1 = '01-04-2020 00:00'
    T2 = '01-07-2020 00:00'

    create_hotel_table(hotels, hotels_const)
    excel_main(hotels, [T0, T1], events, 0)

    create_guest_table(phones, mails, guests, 50000, 0)
    create_worker_table(phones, mails, workers, 70000, 0)
    positions_dict = assign_workers_to_positions(workers)

    create_reservation_table(guests, [T0, T1], reservations)
    create_reservation_service_table(positions_dict, reservations, reservation_service)

    create_room_table(hotels, rooms)
    rooms_dict = assign_rooms_to_hotels(hotels, rooms, dates_dict)
    create_reservation_details_table(reservations, rooms_dict, dates_dict, [T0, T1],
                                     reservation_details)

    dictionary = {'guest': guests, 'worker': workers, 'reservation': reservations,
                  'reservation_service': reservation_service, 'hotel': hotels,
                  'room': rooms, 'reservation_details': reservation_details}

    for key in dictionary:
        save_to_bulk_file(key, dictionary[key])
