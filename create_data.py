from tables.Guest import Guest
from tables.Hotel import Hotel
from tables.Worker import Worker


def create_guest_table(phones, mails):
    for i in range(10000):
        guest = Guest(i + 1, phones, mails)
        phones.append(guest.phone_number)
        mails.append(guest.email)


def create_hotel_table():
    hotels = [['Warszawa', 'Łazienkowska'], ['Warszawa', 'Złota'], ['Warszawa', 'Toruńska'],
              ['Gdańsk', 'Toruńska'], ['Gdańsk', 'Grunwaldzka'], ['Gdynia', 'Świętojańska'],
              ['Gdynia', 'Legionów'], ['Łeba', 'Nadmorska'], ['Wrocław', 'Osobowicka'],
              ['Poznań', 'Koralowa'], ['Lublin', 'Szafirowa'], ['Kraków', 'Kasztanowa'],
              ['Gliwice', 'Akademicka'], ['Katowice', '11 Listopada'], ['Świdnik', 'Kopernika'],
              ['Łódź', 'Bandurskiego'], ['Szczecin', '26 Kwietnia'], ['Toruń', 'św. Józefa'],
              ['Rzeszów', '3 Maja'], ['Kielce', 'Sienkiewicza']]

    hotels_list = []
    for i in range(len(hotels)):
        hotel = Hotel(i + 1, hotels[i])
        hotels_list.append(hotel)

    return hotels_list


def create_worker_table(phones, mails):
    for j in range(1000):
        worker = Worker(j, phones, mails)
        phones.append(worker.phone_number)
        mails.append(worker.email)
        print(worker)
