from datetime import datetime
import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    # шаблонная итерация
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
pprint.pprint(flights)
print()

# генератор
fts = {convert2ampm(k): v.title() for k, v in flights.items()}
pprint.pprint(fts)
print()

# генератор с фильтром
fts = {convert2ampm(k): v.title()
       for k, v in flights.items()
       if v == 'TREASURE CAY'}
pprint.pprint(fts)
print()

when = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
pprint.pprint(when)
print()
