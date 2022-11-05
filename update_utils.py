import random


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
