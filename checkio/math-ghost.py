def monotonic(slopes):
    return True if all([s > 0 for s in slopes]) or all([s < 0 for s in slopes]) else False

def mostly_monotonic(slopes):
    return True if sum([s > 0 for s in slopes]) >=7 or sum([s < 0 for s in slopes]) >=7 else False

def rangey(y):
    return max(y) - min(y)

def meany(y):
    return sum(y) / float(len(y))

def transformy(y):
    mean = meany(y)
    # shift to average
    y = [i*1.0 - mean for i in y]
    maxy, miny = max(y), min(y)
    # normalize
    yn = [i / (maxy-miny) for i in y]
    return yn



def predict_ghost(y):
    factor = 1.0
    x = range(1,11)
    slopes = [y[i] - y[i-1] for i in range(1,10)]
    pred0 = y[-1] + factor * (y[-1] - y[-2])
    mean = sum(y) / len(y)

    mean34 = (y[2] + y[3]) / 2.0
    mean4 = sum(y[-4:]) / 4.



    #pred1 = y[-1] + slopes[-1]
    #assert pred1 == pred0
    # print "x=", x
    # print "y=", y
    # print "slopes=", slopes
    # print "monotonic=", monotonic(slopes)
    # print "mostly_monotonic=", mostly_monotonic(slopes)
    # print "y range=", rangey(y)





    if mostly_monotonic(slopes):
        return y[-1] + 0.8 * (y[-1] - y[-2])
    else:
        #return choice([max(y), min(y), mean])
        return meany(y[-2:])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    from random import choice, random
    import math
    TESTS_QUANTITY = 30
    SCORE_DIST = 0.1

    def generate_formula(prob_x=0.5, prob_bracket=0.2, prob_trig=0.25):
        formula = "x"
        for _ in range(15):
            operation = choice(["+", "-", "*", "/"])
            formula += operation
            if random() < prob_x:
                formula += "x"
            else:
                formula += str(round(random() * 10, 3))
            if random() < prob_bracket:
                formula = "(" + formula + ")"
            if random() < prob_trig:
                formula = "math." + choice(["sin", "cos"]) + "(" + formula + ")"
        return formula

    def calculate_score(f):
        score = 0
        count = 0
        while count < TESTS_QUANTITY:
            formula_x = generate_formula()
            values = []
            for x in range(1, 12):
                try:
                    i = round(eval(formula_x), 3)
                    values.append(i)
                except OverflowError:
                    break
            else:
                if abs(max(values) - min(values)) >= 1:
                    score_distance = (max(values) - min(values)) * SCORE_DIST
                    user_result = f(values[:-1])
                    distance = abs(user_result - values[-1])
                    if distance < score_distance:
                        score += round(100 * ((score_distance - distance) / score_distance))
                    count += 1
        print("Total score: {}".format(score))
        return score

    calculate_score(predict_ghost)

    import pylab
    def plot():
        formula_x = generate_formula()
        xv = map(float, range(1, 12))
        yv = [eval(formula_x) for x in xv]
        #print xv, yv
        pylab.figure(1)
        pylab.plot(xv[:10],transformy(yv[:10]))
        pylab.show()

        y11 = predict_ghost(yv[:10])
        x11 = 11.0
        pylab.figure(2)
        pylab.plot(xv,yv)
        pylab.plot([x11],[y11], marker='o', color='r')
        print "error in prediction: ", 100 * (yv[-1] - y11) / yv[-1]
        pylab.show()

    plot()
