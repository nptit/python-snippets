__author__ = 'qxu'

import re
def get_start_time(schedules, duration):
    minopen = [1] * (60 * 19 - 60 * 9)  # an array all minutes available
    schedules = [[[tomins(x) for x in y] for y in z] for z in schedules]
    print schedules, len(minopen)
    for person in schedules:
        for slot in person:
           a,b=slot
           minopen[a:b]=[0]*(b-a)
    # now scan minopen array for consecutive 1's that is greater than duration
    xp = "".join(map(str, minopen))
    for it in re.finditer(r'1+',xp):
        if it.end()-it.start() >= duration:
            return totimestr(it.start())
    return None

def tomins(string):
    # shift the starting time to 7am, which is point 0
    [hrs, mins] = [int(x) for x in string.split(":")]
    return 60 * hrs + mins-60*9

def totimestr(minutes):
    h,m=divmod(minutes+60*9, 60)
    return '{:0>2d}:{:0>2d}'.format(h,m)


schedules = [
    [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
    [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
    [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]

print get_start_time(schedules, 60)
# print get_start_time(schedules, 90)

schedules = [
    [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
    [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
    [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]
print get_start_time(schedules, 60)