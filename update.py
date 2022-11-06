import random
from read_bulks import *
from update_utils import *
from utils import *
from create_data import *


def update(data, prev_mails, prev_numbers, positions_dict):
    update_guests(data['guest'], prev_mails, prev_numbers)
    update_workers(data['worker'], prev_mails, prev_numbers, positions_dict)
    update_reservation(data['reservation'])
    update_reservation_details(data['reservation_details'])


def inserts(data, prev_mails, prev_numbers, old_reservations):
    T1 = '01-04-2020 00:00'
    T2 = '01-07-2020 00:00'
    dates_dict = {}
    rooms_dict = assign_rooms_to_hotels(data['hotel'], data['room'], dates_dict)
    assign_dates_to_rooms(dates_dict, data['reservation_details'], data['reservation'])
    positions_dict = assign_workers_to_positions(data['worker'])

    # guest: 15000, worker: 5000
    create_guest_table(prev_numbers, prev_mails, data['guest'], 5000, len(data['guest']))
    create_worker_table(prev_numbers, prev_mails, data['worker'], 7000, len(data['worker']))
    update_reservation_table(data['guest'], [T1, T2], data['reservation'], data['guest'][:50000], data['guest'][50000:])
    update_reservation_details_table(data['reservation'][old_reservations:], rooms_dict, dates_dict,
                                     [T1, T2], data['reservation_details'])
    create_reservation_service_table(positions_dict, data['reservation'][old_reservations:],
                                     data['reservation_service'])


def update_guests(guests, prev_mails, prev_numbers):
    # Nazwisko: 500, e-mail: 1000, numer telefonu: 2500
    with open('static/female_surnames.txt', encoding='utf8') as file:
        content = file.readlines()

        surnames = 0
        changed_surnames_ids = []
        while surnames < 500:
            val = random.randrange(len(guests))
            guest = guests[val]

            if guest.gender == 'female' and guest.id not in changed_surnames_ids:
                line = random.randrange(len(content))
                while content[line][:-1] == guest.surname:
                    line = random.randrange(len(content))

                guest.surname = content[line][:-1]
                changed_surnames_ids.append(guest.id)
                surnames += 1

    emails = 0
    changed_emails_ids = []
    while emails < 2000:
        guest = guests[random.randrange(len(guests))]
        if guest.id not in changed_emails_ids:
            new_email = random_email(guest.name, guest.surname, prev_mails, False)
            while new_email == guest.email:
                new_email = random_email(guest.name, guest.surname, prev_mails, False)

            guest.email = new_email
            emails += 1

    numbers = 0
    changed_numbers_ids = []
    while numbers < 5000:
        guest = guests[random.randrange(len(guests))]
        if guest.id not in changed_numbers_ids:
            new_number = random_phone_number(prev_numbers)
            while new_number == guest.phone_number:
                new_number = random_phone_number(prev_numbers)

            guest.phone_number = new_number
            numbers += 1


def update_workers(workers, prev_mails, prev_numbers, positions_dict):
    # Nazwisko: 500, e-mail: 1000, numer telefonu: 2500
    with open('static/female_surnames.txt', encoding='utf8') as file:
        content = file.readlines()

        surnames = 0
        changed_surnames_ids = []
        while surnames < 500:
            val = random.randrange(len(workers))
            worker = workers[val]

            if worker.gender == 'female' and worker.id not in changed_surnames_ids:
                line = random.randrange(len(content))
                while content[line][:-1] == worker.surname:
                    line = random.randrange(len(content))

                worker.surname = content[line][:-1]
                changed_surnames_ids.append(worker.id)
                surnames += 1

    emails = 0
    changed_emails_ids = []
    while emails < 2000:
        worker = workers[random.randrange(len(workers))]
        if worker.id not in changed_emails_ids:
            new_email = random_email(worker.name, worker.surname, prev_mails, True)
            while new_email == worker.email:
                new_email = random_email(worker.name, worker.surname, prev_mails, True)

            worker.email = new_email
            emails += 1

    numbers = 0
    changed_numbers_ids = []
    while numbers < 5000:
        worker = workers[random.randrange(len(workers))]
        if worker.id not in changed_numbers_ids:
            new_number = random_phone_number(prev_numbers)
            while new_number == worker.phone_number:
                new_number = random_phone_number(prev_numbers)

            worker.phone_number = new_number
            numbers += 1

    # awanse po 1000
    cleaners = 0
    cleaners_list = positions_dict['osoba sprzatajaca']
    changed_cleaner_ids = []
    while cleaners < 1000:
        cleaner = cleaners_list[random.randrange(len(cleaners_list))]
        if cleaner.id not in changed_cleaner_ids:
            changed_cleaner_ids.append(cleaner.id)
            cleaner.position = 'pokojowy'
            cleaners += 1

    chambermaids = 0
    chambermaids_list = positions_dict['pokojowy']
    changed_chambermaid_ids = []
    while chambermaids < 1000:
        chambermaid = chambermaids_list[random.randrange(len(chambermaids_list))]
        if chambermaid.id not in changed_chambermaid_ids:
            changed_chambermaid_ids.append(chambermaid.id)
            chambermaid.position = 'osoba zarzadzajaca'
            chambermaids += 1


def update_reservation(reservations):
    payment_method_changes = 0
    changes_id = []

    # 3000
    while payment_method_changes < 3000:
        res = reservations[random.randrange(len(reservations))]
        if res.payment_method in ['karta', 'gotówka'] and res.id not in changes_id:
            if res.payment_method == 'karta':
                res.payment_method = 'gotówka'
            else:
                res.payment_method = 'karta'

            changes_id.append(res.id)
            payment_method_changes += 1


def update_reservation_details(reservations_details):
    numbers_changes = 0
    changes_id = []

    # 1500
    while numbers_changes < 1500:
        res = reservations_details[random.randrange(len(reservations_details))]
        if res.no_of_adults + res.no_of_children > 2 and (res.reservation_id, res.hotel_id, res.room_number) not in changes_id:
            res.no_of_adults, res.no_of_children = rand_children_and_adults_change(res.no_of_children, res.no_of_adults)
            changes_id.append((res.reservation_id, res.hotel_id, res.room_number))
            numbers_changes += 1
