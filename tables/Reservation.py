import random
from datetime import datetime, timedelta

payment_methods = ['BLIK', 'przelew', 'karta', 'gotówka']
CHECK_IN_HOUR = 12
CHECK_OUT_HOUR = 9


def rand_is_canceled():
    if random.random() < 0.05:
        return True
    return False


def rand_payment_method():
    return payment_methods[random.randrange(4)]


def reservation_date_in_period():
    if random.random() < 0.6:
        return False
    return True


def random_date(start, end):
    date_range = ((end - start).days * 3600 * 24) + (end - start).seconds
    random_second = random.randrange(date_range)
    return start + timedelta(seconds=random_second)


def rand_reservation_date(period):
    if reservation_date_in_period():
        return random_date(datetime.strptime(period[0], '%d-%m-%Y %H:%M'),
                           datetime.strptime(period[1], '%d-%m-%Y %H:%M'))
    else:
        return random_date(datetime.strptime(period[0], '%d-%m-%Y %H:%M') - timedelta(days=194),
                           datetime.strptime(period[1], '%d-%m-%Y %H:%M'))


def rand_check_in_date(reservation_date):
    check_in_date = random_date(reservation_date + timedelta(days=1),
                                reservation_date + timedelta(days=180))

    check_in_date -= timedelta(hours=check_in_date.hour, minutes=check_in_date.minute,
                               seconds=check_in_date.second) - timedelta(hours=CHECK_IN_HOUR)

    return check_in_date


def rand_check_out_date(check_in_date):
    reservation_days = random.randrange(1, 15)
    check_out_date = check_in_date + timedelta(days=reservation_days)

    check_out_date -= timedelta(hours=check_out_date.hour, minutes=check_out_date.minute,
                                seconds=check_out_date.second) - timedelta(hours=CHECK_OUT_HOUR)

    return check_out_date


def rand_dates(period, guest_reservations_dates):
    reservation_date = rand_reservation_date(period)
    check_in_date = rand_check_in_date(reservation_date)
    check_out_date = rand_check_out_date(check_in_date)

    for date in guest_reservations_dates:
        if max(date[0], check_in_date) <= min(date[1], check_out_date):
            return rand_dates(period, guest_reservations_dates)

    return reservation_date, check_in_date, check_out_date


class Reservation:
    def __init__(self, reservation_id, guest_id, period, guest_reservations_dates, text):
        if text is None:
            self.id = reservation_id
            self.guest_id = guest_id
            self.reservation_date, self.check_in_date, self.check_out_date = \
                rand_dates(period, guest_reservations_dates)
            self.is_canceled = rand_is_canceled()
            self.payment_method = rand_payment_method()

            guest_reservations_dates.append((self.check_in_date, self.check_out_date))
        else:
            values = text.split('|')
            self.id = values[0]
            self.guest_id = values[1]
            self.reservation_date, self.check_in_date, self.check_out_date = values[2], values[3], values[4]
            self.is_canceled = values[5]
            self.payment_method = values[6]

    def __str__(self):
        return "%s|%s|%s|%s|%s|%s|%s" % (self.id, self.guest_id, self.reservation_date,
                                         self.check_in_date, self.check_out_date,
                                         int(self.is_canceled), self.payment_method)