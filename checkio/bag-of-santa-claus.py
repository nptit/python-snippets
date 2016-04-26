def choose_good_gift(current_gift, gifts_in_bag, gift_number):
    'https://en.wikipedia.org/wiki/Secretary_problem'
    global checked
    try:
        checked.append(current_gift)
    except:
        checked = []
        checked.append(current_gift)

    if len(checked) >= int(gifts_in_bag / 2):
        if current_gift >= max(checked):
            checked = []
            return True

    if len(checked) == gifts_in_bag:
            checked = []
            return True

    return False


def choose_good_gift(current, n, i):
    global max_gift
    # ignore first int(n*0.3678) gifts, and record max value.
    if i < int(n * 0.3678):
        max_gift = current if i == 1 else max(current, max_gift)
        return False

    return i == n or current > max_gift







if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for auto-testing
    from random import random, randint, uniform

    scale = (random() + random()) ** randint(0, 1024)

    standings = gift_count = best_gifts = 0
    #bag_count = 2000
    bag_count = 30

    for i in range(bag_count):
        gifts_in_bag = randint(10, 1000)
        # print "bag ", i
        #gifts_in_bag = randint(2, 4)
        gift_count += gifts_in_bag

        gifts = []
        selected_gift = None
        for i in range(gifts_in_bag):
            new_gift = uniform(0., scale)
            gifts.append(new_gift)
            decision = choose_good_gift(new_gift, gifts_in_bag, i + 1)
            if decision:
                selected_gift = new_gift
                gifts.extend([uniform(0., scale) for _ in range(gifts_in_bag - i - 1)])
                break
        if selected_gift is None:
            priority = len(gifts)
        else:
            priority = sum(selected_gift < x for x in gifts)
        standings += priority
        best_gifts += not priority
    print('You do won {:n} best gifts from {:n} bags with {:,} gifts!\n'
          'It seems like for bags of {:n} gifts -\n'
          'you would choose the second best gift, silver ;)'
          .format(best_gifts, bag_count, gift_count, round(gift_count / standings) + 1))
