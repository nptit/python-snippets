import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    # TO DO
    prob_reproduce = 1.0 - CURRENTRABBITPOP * 1.0 / MAXRABBITPOP
    for rabbit in range(CURRENTRABBITPOP):
        if random.random() <= prob_reproduce:
            CURRENTRABBITPOP += 1

    if CURRENTRABBITPOP > MAXRABBITPOP:
        CURRENTRABBITPOP = MAXRABBITPOP

def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    prob_eaten = 1.0 * CURRENTRABBITPOP / MAXRABBITPOP
    for fox in range(CURRENTFOXPOP):
        if random.random() <= prob_eaten:
            # hunt success
            CURRENTRABBITPOP -= 1
            if CURRENTRABBITPOP < 10:
                CURRENTRABBITPOP = 10

            if random.random() <= 1.0 / 3.0:
                CURRENTFOXPOP += 1
        else:
            # hunt fail
            if random.random() <= 9.0 / 10.0:
                CURRENTFOXPOP -= 1
                # if CURRENTFOXPOP < 10:
                #     CURRENTFOXPOP = 10


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    popr = []
    popf = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        popr.append(CURRENTRABBITPOP)
        popf.append(CURRENTFOXPOP)

    return (popr, popf)

if __name__ == '__main__':
    # CURRENTFOXPOP = 300
    # CURRENTRABBITPOP = 50
    popr, popf = runSimulation(200)
    pylab.figure(1)
    pylab.plot(popr)
    pylab.plot(popf)

    coeff_r = pylab.polyfit(range(len(popr)), popr, 2)
    pylab.plot(pylab.polyval(coeff_r, range(len(popr))))

    coeff_f = pylab.polyfit(range(len(popf)), popf, 2)
    pylab.plot(pylab.polyval(coeff_f, range(len(popf))))
    pylab.show()
