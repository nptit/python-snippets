# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics

import numpy
import random
import pylab

'''
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        return True if random.random() < self.clearProb else False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        reproduce_prob = self.maxBirthProb * (1 - popDensity)
        if random.random() < reproduce_prob:
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
            #return self
        else:
            raise NoChildException



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

        # TODO

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population.
        returns: The total virus population (an integer)
        """
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """
        # update v list based on death of viruses
        newv = [v for v in self.viruses if not v.doesClear()]
        # calculate population density
        curr_popDen = 1.0 * len(newv) / self.maxPop
        offsprings = []
        for v in newv:
            try:
                offsprings.append(v.reproduce(curr_popDen))
            except NoChildException:
                pass
        self.viruses = newv + offsprings
        return len(self.viruses)

    # def update(self):
    #     self.viruses = [v for v in self.viruses if not v.doesClear()]
    #     popDensity = len(self.viruses) / float(self.maxPop)
    #     for v in self.viruses[:]:
    #         try:
    #             self.viruses.append(v.reproduce(popDensity))
    #         except NoChildException:
    #             pass
    #     return len(self.viruses)

# v1 = SimpleVirus(0.5, 0.5)
# v2 = SimpleVirus(0.5, 0.5)
# v3 = SimpleVirus(0.5, 0.5)
# v4 = SimpleVirus(0.5, 0.5)

# print v1.doesClear(), v2.doesClear(), v3.doesClear(), v4.doesClear()

# p = Patient([v1,v2,v3,v4], 20)
# print len(p.viruses)
# p.update()
# print len(p.viruses)

#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    trial_results = []
    for i in range(numTrials):
        viruses = [SimpleVirus(maxBirthProb, clearProb) for _ in range(numViruses)]
        patient = Patient(viruses, maxPop)
        pop_over_time =[]
        for time in range(300):
            pop_over_time.append(patient.update())
        trial_results.append(pop_over_time)

    # calculate average over time from numTrials
    avgPop_over_time = [1.0 * sum(pop_at_time) / numTrials for pop_at_time in zip(*trial_results)]

    pylab.figure(1)
    pylab.plot(avgPop_over_time)
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.title("SimpleVirus simulation")
    pylab.legend("nvirues - No drug")
    pylab.show()
    #return avgPop_over_time

#print simulationWithoutDrug(100, 1000, 0.1, 0.05, 5)



#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return drug in self.resistances and self.resistances[drug]


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:

        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        if all(self.isResistantTo(drug) for drug in activeDrugs):
            reproduce_prob = self.maxBirthProb * (1 - popDensity)
            if random.random() < reproduce_prob:
                new_resistances = {}
                for d, r in self.resistances.items():
                    if random.random() < 1. - self.mutProb:
                        new_resistances[d] = r
                    else:
                        new_resistances[d] = not r
                return ResistantVirus(self.maxBirthProb, self.clearProb, new_resistances, self.mutProb)

        raise NoChildException

# rv = ResistantVirus(0.5, 0.5, {'guttagonol':True, 'srinol':False}, 0.9)
# print rv.getMutProb(), rv.isResistantTo('srinol')
# rv.reproduce(0.2, ['guttagonol'])

# virus = ResistantVirus(1.0, 0.0, {}, 0.0)
# v1 = virus.reproduce(0.0, [])
# print virus.doesClear()

# virus = ResistantVirus(1.0, 1.0, {"drug1":True, "drug2":False}, 0.0)
# print virus.isResistantTo('drug3')
# virus.reproduce(0, [])

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.drugs = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        return len([v for v in self.viruses if all(v.isResistantTo(d) for d in drugResist)])


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        # update v list based on death of viruses
        newv = [v for v in self.viruses if not v.doesClear()]
        # calculate population density
        curr_popDen = 1.0 * len(newv) / self.maxPop
        offsprings = []
        for v in newv:
            try:
                offsprings.append(v.reproduce(curr_popDen, self.drugs))
            except NoChildException:
                pass
        self.viruses = newv + offsprings
        return len(self.viruses)

# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """
    trial_results_popt = []
    trial_results_popr = []
    for i in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances.copy(), mutProb) for _ in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)
        popt_over_time = []
        popr_over_time = []

        for time in range(300):
            if time == 150:
                patient.addPrescription('guttagonol')
            patient.update()
            popt_over_time.append(patient.getTotalPop())
            popr_over_time.append(patient.getResistPop(['guttagonol']))

        trial_results_popt.append(popt_over_time)
        trial_results_popr.append(popr_over_time)

    # calculate average over time from numTrials
    avgPop_over_time_t = [1.0 * sum(pop_at_time) / numTrials for pop_at_time in zip(*trial_results_popt)]
    avgPop_over_time_r = [1.0 * sum(pop_at_time) / numTrials for pop_at_time in zip(*trial_results_popr)]
    print avgPop_over_time_t
    print avgPop_over_time_r

    pylab.figure(1)
    pylab.plot(avgPop_over_time_t, label="total virus population")
    pylab.plot(avgPop_over_time_r, label="drug resistant population")
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Num of Viruses")
    pylab.legend()
    pylab.show()

if __name__ == '__main__':
    simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
    #simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 10)
    #simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
    #simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
    #simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)
    exit()
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    mutProb = 0.005
    resistances = {'guttagonol': False}
    numTrials = 10
    simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials)

