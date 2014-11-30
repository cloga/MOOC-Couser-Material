# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        

def init_patient(maxBirthProb = 0.1, clearProb = 0.05, mutProb = 0.005, numViruses = 100, maxPop = 1000, resistances =  {'guttagonol': False, 'grimpex': False}):
    viruses = []
    for dummy_n in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    patient = TreatedPatient(viruses, maxPop)
    return patient

def get_pop_list(init_step, numTrials):
    '''
    generate pop list
    patient : base virus
    init_step : step before inject
    numTrials : 
    return : pop_list
    '''
    pop_list = []
    for _ in range(numTrials):
        patient = init_patient()
        for _ in range(init_step):
            pop = patient.update()
        patient.addPrescription('guttagonol')
        for _ in range(init_step, init_step + 150):
            pop = patient.update() # # of virus
        pop_list.append(pop)
    return pop_list

    
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)

    Use the following parameters to initialize a TreatedPatient:
    viruses, a list of 100 ResistantVirus instances
    maxPop, maximum sustainable virus population = 1000
    
    Each ResistantVirus instance in the viruses list should be initialized with the following parameters:
    maxBirthProb, maximum reproduction probability for a virus particle = 0.1
    clearProb, maximum clearance probability for a virus particle = 0.05
    resistances, The virus's genetic resistance to drugs in the experiment = {'guttagonol': False}
    mutProb, probability of a mutation in a virus particle's offspring = 0.005
    """
    pop_list = {}
    resistant_pop_list = {}
    init_step_list = [300, 150, 75, 0]
    for index, init_step in enumerate(init_step_list):
        pop_list[init_step] = get_pop_list(init_step, numTrials)
        pylab.subplot(2, 2, index + 1)
        pylab.hist(pop_list[init_step])
        pylab.title('histogram of init step ' + str(init_step))
        pylab.xlabel('bin')
        pylab.ylabel('frequency')
    pylab.show()
    return pop_list
    
    # TODO
# pop_list = simulationDelayedTreatment(100)

init_step = 150
pop_list = []
resistant_pop_list = {}
numTrials = 100

maxPop = 5000
for _ in range(numTrials):
    patient = init_patient(maxPop=maxPop)
    for _ in range(init_step):
        pop = patient.update()
    patient.addPrescription('guttagonol')
    for _ in range(init_step, init_step + 150):
        pop = patient.update() # # of virus
    pop_list.append(pop)
pylab.hist(pop_list)
pylab.title('histogram of maxPop ' + str(maxPop))
pylab.xlabel('bin')
pylab.ylabel('frequency')
pylab.show()


#
# PROBLEM 2
#

def get_pop_list2(init_step, numTrials):
    '''
    generate pop list
    patient : base virus
    init_step : step before inject
    numTrials : 
    return : pop_list
    '''
    pop_list = []
    for _ in range(numTrials):
        patient = init_patient()
        for _ in range(150):
            pop = patient.update()
        patient.addPrescription('guttagonol')
        for _ in range(init_step):
            pop = patient.update()
        patient.addPrescription('grimpex')
        for _ in range(init_step, init_step + 150):
            pop = patient.update() # # of virus
        pop_list.append(pop)
    return pop_list

def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    pop_list = {}
    resistant_pop_list = {}
    init_step_list = [300, 150, 75, 0]
    for index, init_step in enumerate(init_step_list):
        pop_list[init_step] = get_pop_list(init_step, numTrials)
        pylab.subplot(2, 2, index + 1)
        pylab.hist(pop_list[init_step])
        pylab.title('histogram of init step ' + str(init_step))
        pylab.xlabel('bin')
        pylab.ylabel('frequency')
    pylab.show()
    return pop_list

pop_list = simulationDelayedTreatment(100)