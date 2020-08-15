'''
https://py.checkio.org/en/mission/date-and-time-converter/

Computer date and time format consists only of numbers, for example: 21.05.2018
16:30 Humans prefer to see something like this: 21 May 2018 year, 16 hours 30
minutes Your task is simple - convert the input date and time from computer
format into a "human" format.

example

Input: Date and time as a string

Output: The same date and time, but in a more readable format

Precondition: 0 < date <= 31 0 < month <= 12 0 < year <= 3000 0 < hours < 24 0
< minutes < 60
'''


def date_time(time: str) -> str:
    m = ["January", "Febuary", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"]
    t = list(map(int, time.replace(' ', '.').replace(':', '.').split('.')))
    t[1] = m[int(t[1]) - 1]
    hour = 'hour' if t[3] == 1 else 'hours'
    minute = 'minute' if t[4] == 1 else 'minutes'
    return "{} {} {} year {} {} {} {}".format(t[0], t[1], t[2], t[3], hour,
                                              t[4], minute)


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))
    print(date_time('11.04.1812 01:01'))

    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert date_time("01.01.2000 00:00") ==\
        "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") ==\
        "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") ==\
        "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
