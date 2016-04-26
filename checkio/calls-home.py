import math
from collections import defaultdict

def round2min(seconds):
    'round seconds into minutes'
    return math.ceil(seconds / 60.0)

def cost(mins):
    return mins if mins <= 100 else 2 * mins - 100

def total_cost(calls):
    'sort calls by day, then aggregate the cost by day'
    callsbyday = defaultdict(list)
    calls = [c.split() for c in calls]
    for d, _, l in calls:
        callsbyday[d].append(round2min(int(l)))

    return int(sum([cost(sum(v)) for v in callsbyday.values()]))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost((u"2014-02-05 01:00:00 60",
                       u"2014-02-05 02:00:00 60",
                       u"2014-02-05 03:00:00 60",
                       u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"
