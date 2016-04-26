# import random

# def noReplacementSimulation(numTrials):
#     '''
#     Runs numTrials trials of a Monte Carlo simulation
#     of drawing 3 balls out of a bucket containing
#     3 red and 3 green balls. Balls are not replaced once
#     drawn. Returns the a decimal - the fraction of times 3
#     balls of the same color were drawn.
#     '''
#     same_color = lambda draw: all(b=='r' for b in draw) or all(b=='g' for b in draw)

#     nhits = 0
#     for _ in range(numTrials):
#         balls = ['r','r','r', 'g', 'g', 'g']
#         i = 0
#         r = []
#         for _ in range(3):
#             draw = random.choice(range(6 - i))
#             r.append(balls[draw])
#             balls.pop(draw)
#             i += 1
#         if same_color(r):
#             nhits += 1
#     return float(nhits) / numTrials


# print noReplacementSimulation(10000)


import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    same_color = lambda draw: all(b=='r' for b in draw) or all(b=='g' for b in draw)

    nhits = 0
    nballs = 8
    for _ in range(numTrials):
        balls = ['r','r','r', 'r', 'g', 'g', 'g', 'g']
        i = 0
        r = []
        for _ in range(3):
            draw = random.choice(range(nballs - i))
            r.append(balls[draw])
            balls.pop(draw)
            i += 1
        if same_color(r):
            nhits += 1
    return float(nhits) / numTrials


print noReplacementSimulation(10000)
