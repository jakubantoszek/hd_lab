import random

names = []
surnames = []
e_mails = ['gmail.com', 'interia.pl', 'o2.pl', 'wp.pl', 'onet.pl']
email_breaks = ['', '.', '-', '_']
polish_signs = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ó': 'o', 'ń': 'n', 'ś': 's',
                'ż': 'z', 'ź': 'z'}


def random_phone_number():
    number = ''
    first_letter = random.randrange(1, 10)
    number += str(first_letter)

    for _ in range(8):
        number += str(random.randrange(1, 10))

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


def random_email(name, surname):
    service = e_mails[random.randrange(len(e_mails))]
    email_break = email_breaks[random.randrange(len(email_breaks))]
    mail_name = remove_polish_signs(name).lower()
    mail_surname = remove_polish_signs(surname).lower()
    return mail_name + email_break + mail_surname + '@' + service


def remove_polish_signs(string):
    result = ''
    for sign in string:
        if sign in polish_signs:
            result += polish_signs[sign]
        else:
            result += sign

    return result


def xd():
    print(names)
    print(surnames)
