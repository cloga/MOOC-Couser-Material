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
    rabbit_reproduction_rate = 1 - 1.0 * CURRENTRABBITPOP / MAXRABBITPOP
    CURRENTRABBITPOP = int((1 + rabbit_reproduction_rate) * CURRENTRABBITPOP)
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
    rabbitGrowth()
    fox_eat_rabbit_rate = 1.0 * CURRENTRABBITPOP / MAXRABBITPOP
    fox_eat_rabbit = int(CURRENTFOXPOP * fox_eat_rabbit_rate)
    if (CURRENTRABBITPOP - fox_eat_rabbit) > 10:
        CURRENTRABBITPOP = CURRENTRABBITPOP - fox_eat_rabbit
        CURRENTFOXPOP = CURRENTFOXPOP + fox_eat_rabbit / 3
        CURRENTFOXPOP = CURRENTFOXPOP - (CURRENTFOXPOP - fox_eat_rabbit) / 10
    else:
        CURRENTFOXPOP = CURRENTFOXPOP - (CURRENTFOXPOP) / 10
            
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
    rabbit_populations = []
    fox_populations = []
    for i in range(numSteps):
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return rabbit_populations, fox_populations

