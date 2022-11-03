from utils import *
from create_data import *

if __name__ == '__main__':
    get_names()
    get_surnames()
    set_positions()
    phones = []
    mails = []

    # create_guest_table(phones, mails)
    hotels = create_hotel_table()
    # create_worker_table(phones, mails)
    create_room_table(hotels)
