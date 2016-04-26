def predict_ghost(v):
    return 1 #340 points

## curve fitting not very good
import numpy as np
def predict_ghost(v):
    x = range(1, 11)
    y = v
    coeff = np.polyfit(x,y, 1)
    predict = np.poly1d(coeff)
    return predict(11.0)


def predict_ghost(v):
    #~1500 points
    last = v[-1]
    secondlast = v[-2]
    diff = last - secondlast
    return last + diff


def predict_ghost(y):
    x = range(1,11)
    slopes = [y[i] - y[i-1] for i in range(1,10)]
    avg_slope = float(sum(slopes)) / len(slopes)
    avg_intercept = (sum(y) - sum(x) * avg_slope) / 10.
    pred11 = avg_slope * 11.0 - avg_slope
    return pred11
    #print slopes




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
        y11 = predict_ghost(yv)
        x11 = 11.0
        pylab.figure(1)
        pylab.plot(xv,yv)
        pylab.plot([x11],[y11], marker='o', color='r')
        pylab.show()

    plot()
