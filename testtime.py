import datetime


def get_time(days):
    a = str(datetime.date.today()-datetime.timedelta(days=days))
    return a
    # print(a+" 11", type(a))
# type(datetime.now())


print(get_time(5))
