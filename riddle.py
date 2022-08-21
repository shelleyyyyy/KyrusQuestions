
weekday = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
pointer = 0

month = [
    ['jan', 31],
    ['feb', 28],
    ['mar', 31],
    ['apr', 30],
    ['may', 31],
    ['jun', 30],
    ['jul', 31],
    ['aug', 31],
    ['sep', 30],
    ['oct', 31],
    ['nov', 30],
    ['dec', 31],
]

month_point = 0
month_counter = 1

year_track = 1901
year_count = 1

answer_counter = 0


def iterate_weekday():
    global pointer, weekday

    pointer = pointer + 1

    if pointer > 6:
        pointer = 0


def iterate_month():
    global month, month_point, month_counter, answer_counter

    if month[month_point][1] == month_counter:
        if month[month_point][0] == 'dec':
            month_point = 0

        month_counter = 1
        month_point = month_point + 1

    else:

        month_counter = month_counter + 1


def iterate_year():
    global year_track, year_count, month

    if year_count == 365:
        year_track = year_track + 1
        year_count = 1

    if year_track % 400 == 0:
        month[1][1] = 29
    else:
        month[1][1] = 28

    year_count = year_count + 1


while True:
    if weekday[pointer] == 'sun' and month_counter == 1:
        # print("it is the first of ", month[month_point][0], " and it is a ", weekday[pointer])
        answer_counter = answer_counter + 1

    if year_track == 2000 and month[month_point][1] == month_counter and month[month_point][0] == 'dec':
        print("there are ", answer_counter, " sundays that fell on the first of the month")
        exit(0)

    iterate_month()
    iterate_weekday()
    iterate_year()
