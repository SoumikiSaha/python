n = int(input())

sports = []
for _ in range(n):
    sports.append(input().split(','))

schedule = []
day = 1
session = 'FN'

for i, sport in enumerate(sports, 1):
    while sport:
        if session == 'FN':
            schedule.append(f'Sport {i} Day {day} FN')
            schedule.append(' '.join(sport[:9]))
            sport = sport[9:]
            session = 'AN'
        else:
            schedule.append(f'Sport {i} Day {day} AN')
            schedule.append(' '.join(sport[:9]))
            sport = sport[9:]
            session = 'FN'
            day += 1

for item in schedule:
    print(item)