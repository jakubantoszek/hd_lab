from utils import *
from create_data import *

if __name__ == '__main__':
    get_names()
    get_surnames()
    phones = []
    mails = []

    create_guests_table(phones, mails)
