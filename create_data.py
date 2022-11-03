from tables.Guest import Guest


def create_guests_table(phones, mails):
    for i in range(1000000):
        guest = Guest(i, phones, mails)
        phones.append(guest.phone_number)
        mails.append(guest.email)
