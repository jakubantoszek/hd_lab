from utils import *

if __name__ == '__main__':
    get_names()
    get_surnames()
    for i in range(100):
        print(random_email(random_name(), random_surname()))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
