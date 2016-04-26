from datetime import datetime, timedelta


def error(error_description):
    ' return error (in_second) per second'
    d = {'seco':1,'minu':60, 'hour':3600}
    sign = -1 if error_description[0] == '-' else +1
    desc = [d[w[:4]] if w[:4] in d else int(w) for w in error_description[1:].replace('at ','').split()]
    desc = map(float, desc)
    error = (desc[0] * desc[1]) / (desc[2] * desc[3])
    return sign * error

def broken_clock(starting_time, wrong_time, error_description):
    """(R - start_time)*(1+error) = wrong_time - start_time,
    solve for R (real time) = start_time + (wrong_time - start)/(1+error)"""
    start = datetime.strptime(starting_time, '%H:%M:%S')
    wrong = datetime.strptime(wrong_time, '%H:%M:%S')
    adjustment = (wrong - start).seconds / (1. + error(error_description))
    real_time = start + timedelta(seconds = adjustment)
    return datetime.strftime(real_time, '%H:%M:%S')


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
