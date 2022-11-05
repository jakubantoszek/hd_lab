import random

male_names = []
male_surnames = []
female_names = []
female_surnames = []
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


def rand_gender():
    if random.random() < 0.5:
        return "male"
    return "female"


def get_names():
    with open('static/male_names.txt', encoding='utf8') as file:
        lista = file.readlines()

        for val in lista:
            male_names.append(val[:-1])

    with open('static/female_names.txt', encoding='utf8') as file:
        lista = file.readlines()

        for val in lista:
            female_names.append(val[:-1])


def get_surnames():
    with open('static/male_surnames.txt', encoding='utf8') as file:
        lista = file.readlines()

        for val in lista:
            male_surnames.append(val[:-1])

    with open('static/female_surnames.txt', encoding='utf8') as file:
        lista = file.readlines()

        for val in lista:
            female_surnames.append(val[:-1])


def random_name(gender):
    if gender == "male":
        x = random.randrange(len(male_names))
        return male_names[x]
    else:
        x = random.randrange(len(female_names))
        return female_names[x]


def random_surname(gender):
    if gender == "male":
        x = random.randrange(len(male_surnames))
        return male_surnames[x]
    else:
        x = random.randrange(len(female_surnames))
        return female_surnames[x]


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


def assign_rooms_to_hotels(hotels, rooms, dates_dict):
    dictionary = {}
    for hotel in hotels:
        dictionary[hotel.id] = []

    for room in rooms:
        dictionary[room.hotel_id].append(room)
        dates_dict[(room.hotel_id, room.number)] = []

    return dictionary


def save_to_bulk_file(class_name, values):
    directory = 'bulk/'
    with open(directory + class_name + '.bulk', 'w') as f:
        f.write(str(values[0]))
        for val in values[1:]:
            f.write('\n' + str(val))
