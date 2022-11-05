import random

from tables.Reservation import Reservation


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
    directory = 'bulk_t2/'
    with open(directory + class_name + '.bulk', 'w') as f:
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
            print('xd')
            reservation = Reservation(len(reservations) + 1, list_of_new_guests[i].id, period, dates, None, 0)
            reservations.append(reservation)

    for i in range(len(list_of_old_guests)):
        no_of_reservations = get_no_of_reservations({0.85: 0, 0.98: 1, 1: 2})

        for j in range(no_of_reservations):
            reservation = Reservation(len(reservations) + 1, list_of_old_guests[i].id, period, dates, None, 0)
            reservations.append(reservation)
