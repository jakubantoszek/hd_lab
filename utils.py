import random

names = []
surnames = []
e_mails = ['gmail.com', 'interia.pl', 'o2.pl', 'wp.pl', 'onet.pl']
email_breaks = ['', '.', '-', '_']
stars = [5, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2]
polish_signs = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ó': 'o', 'ń': 'n', 'ś': 's',
                'ż': 'z', 'ź': 'z'}
positions = [('osoba sprzątająca', 400), ('pokojowy', 200), ('osoba zarządzająca', 100)]
positions_list = []
hotel_capacity = []
ten_rooms_capacities = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
room_capacity = {}


def random_phone_number(prev_numbers):
    number = ''
    first_letter = random.randrange(1, 10)
    number += str(first_letter)

    for _ in range(8):
        number += str(random.randrange(1, 10))

    if number in prev_numbers:
        return random_phone_number(prev_numbers)

    return number


def get_names():
    with open('static/names.txt') as file:
        lista = file.readlines()

        for val in lista:
            names.append(val[:-1])


def get_surnames():
    with open('static/surnames.txt') as file:
        lista = file.readlines()

        for val in lista:
            surnames.append(val[:-1])


def random_name():
    x = random.randrange(len(names))
    return names[x]


def random_surname():
    x = random.randrange(len(surnames))
    return surnames[x]


def set_positions():
    for i in range(len(positions)):
        for j in range(positions[i][1]):
            positions_list.append(positions[i][0])


def random_email(name, surname, prev_mails, is_worker):
    if is_worker:
        service = 'anj.pl'
    else:
        service = e_mails[random.randrange(len(e_mails))]

    email_break = email_breaks[random.randrange(len(email_breaks))]
    mail_name = remove_polish_signs(name).lower()
    mail_surname = remove_polish_signs(surname).lower()

    mail = mail_name + email_break + mail_surname + '@' + service
    if mail in prev_mails:
        return random_email(name, surname, prev_mails, is_worker)

    return mail


def remove_polish_signs(string):
    result = ''
    for sign in string:
        if sign in polish_signs:
            result += polish_signs[sign]
        else:
            result += sign

    return result


def random_building_number():
    return random.randrange(1, 100)


def random_stars():
    idx = random.randrange(len(stars))
    val = stars[idx]
    del stars[idx]
    return val


def random_position():
    idx = random.randrange(len(positions_list))
    val = positions_list[idx]
    del positions_list[idx]
    return val


def rand_hotels_capacity():
    return random.randrange(5, 21) * 10


def get_hotel_rooms_capacities(hotel_cap):
    results = []

    for j in range(10):
        for i in range(int(hotel_cap / 10)):
            results.append(ten_rooms_capacities[j])

    return results


def random_is_occupied():
    if random.random() < 0.6:
        return True

    return False


def assign_workers_to_positions(workers):
    dictionary = {'osoba sprzatajaca': [], 'pokojowy': [], 'osoba zarzadzajaca': []}
    for worker in workers:
        if worker.position == 'osoba sprzątająca':
            dictionary['osoba sprzatajaca'].append(worker)
        elif worker.position == 'pokojowy':
            dictionary['pokojowy'].append(worker)
        else:
            dictionary['osoba zarzadzajaca'].append(worker)

    return dictionary


def assign_rooms_to_hotels(hotels, rooms):
    dictionary = {}
    for hotel in hotels:
        dictionary[hotel.id] = []

    for room in rooms:
        dictionary[room.hotel_id].append(room)

    return dictionary


def xd():
    print(hotel_capacity)
