import random
from read_bulks import *
from update_utils import *
from utils import *


def update(data, prev_mails, prev_numbers, positions_dict):
    update_guests(data['guest'], prev_mails, prev_numbers)
    update_workers(data['worker'], prev_mails, prev_numbers, positions_dict)
    update_reservation(data['reservation'])
    update_reservation_details(data['reservation_details'])


def update_guests(guests, prev_mails, prev_numbers):
    # Nazwisko: 50, e-mail: 200, numer telefonu: 500
    with open('static/female_surnames.txt', encoding='utf8') as file:
        content = file.readlines()

        surnames = 0
        changed_surnames_ids = []
        while surnames < 5:
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
    while emails < 20:
        guest = guests[random.randrange(len(guests))]
        if guest.id not in changed_emails_ids:
            new_email = random_email(guest.name, guest.surname, prev_mails, False)
            while new_email == guest.email:
                new_email = random_email(guest.name, guest.surname, prev_mails, False)

            guest.email = new_email
            emails += 1

    numbers = 0
    changed_numbers_ids = []
    while numbers < 50:
        guest = guests[random.randrange(len(guests))]
        if guest.id not in changed_numbers_ids:
            new_number = random_phone_number(prev_numbers)
            while new_number == guest.phone_number:
                new_number = random_phone_number(prev_numbers)

            guest.phone_number = new_number
            numbers += 1


def update_workers(workers, prev_mails, prev_numbers, positions_dict):
    # Nazwisko: 50, e-mail: 200, numer telefonu: 500
    with open('static/female_surnames.txt', encoding='utf8') as file:
        content = file.readlines()

        surnames = 0
        changed_surnames_ids = []
        while surnames < 5:
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
    while emails < 20:
        worker = workers[random.randrange(len(workers))]
        if worker.id not in changed_emails_ids:
            new_email = random_email(worker.name, worker.surname, prev_mails, True)
            while new_email == worker.email:
                new_email = random_email(worker.name, worker.surname, prev_mails, True)

            worker.email = new_email
            emails += 1

    numbers = 0
    changed_numbers_ids = []
    while numbers < 50:
        worker = workers[random.randrange(len(workers))]
        if worker.id not in changed_numbers_ids:
            new_number = random_phone_number(prev_numbers)
            while new_number == worker.phone_number:
                new_number = random_phone_number(prev_numbers)

            worker.phone_number = new_number
            numbers += 1

    cleaners = 0
    cleaners_list = positions_dict['osoba sprzatajaca']
    changed_cleaner_ids = []
    while cleaners < 10:
        cleaner = cleaners_list[random.randrange(len(cleaners_list))]
        if cleaner.id not in changed_cleaner_ids:
            changed_cleaner_ids.append(cleaner.id)
            cleaner.position = 'pokojowy'
            cleaners += 1

    chambermaids = 0
    chambermaids_list = positions_dict['pokojowy']
    changed_chambermaid_ids = []
    while chambermaids < 10:
        chambermaid = chambermaids_list[random.randrange(len(chambermaids_list))]
        if chambermaid.id not in changed_chambermaid_ids:
            changed_chambermaid_ids.append(chambermaid.id)
            chambermaid.position = 'osoba zarzadzajaca'
            chambermaids += 1


def update_reservation(reservations):
    payment_method_changes = 0
    changes_id = []

    while payment_method_changes < 30:
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

    while numbers_changes < 15:
        res = reservations_details[random.randrange(len(reservations_details))]
        if res.no_of_adults + res.no_of_children > 2 and (res.reservation_id, res.hotel_id, res.room_number) not in changes_id:
            res.no_of_adults, res.no_of_children = rand_children_and_adults_change(res.no_of_children, res.no_of_adults)
            changes_id.append((res.reservation_id, res.hotel_id, res.room_number))
            numbers_changes += 1
