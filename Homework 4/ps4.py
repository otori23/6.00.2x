# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delays = [0, 75, 150, 300]
    for i in range(len(delays)):
        print 'Run one drug simulation for delay: ' + str(delays[i])
        pylab.subplot(2, 2, i+1)
        virusPopulations = executeTreatment(numTrials=numTrials, treatment=oneDrugTreatment, delay=delays[i])
        popMin = min(virusPopulations)
        popMax = max(virusPopulations)
        popMean = numpy.mean(virusPopulations)
        popStd = numpy.std(virusPopulations)
    
        pylab.hist(virusPopulations, bins = 10)

        pylab.xlim(0, 600)        
        xmin,xmax = pylab.xlim()
        ymin,ymax = pylab.ylim()   
        
        pylab.xlabel('Virus population')
        pylab.ylabel('Number of Occrences')
        pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2, 'Delay = ' + str(delays[i]) + '\nMin = ' + str(popMin) + '\nMax = ' + str(popMax) + '\nMean = ' + str(popMean) + '\nStd = ' + str(popStd)) 
   
    pylab.show()
        
#
# PROBLEM 2
#
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
    delays = [0, 75, 150, 300]
    for i in range(len(delays)):
        print 'Run two drug simulation for delay: ' + str(delays[i])
        pylab.subplot(2, 2, i+1)
        virusPopulations = executeTreatment(numTrials=numTrials, treatment=twoDrugTreatment, delay=delays[i])
        popMin = min(virusPopulations)
        popMax = max(virusPopulations)
        popMean = numpy.mean(virusPopulations)
        popStd = numpy.std(virusPopulations)
    
        pylab.hist(virusPopulations, bins = 10)

        pylab.xlim(0, 600)        
        xmin,xmax = pylab.xlim()
        ymin,ymax = pylab.ylim()   
        
        pylab.xlabel('Virus population')
        pylab.ylabel('Number of Occrences')
        pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2, 'Delay = ' + str(delays[i]) + '\nMin = ' + str(popMin) + '\nMax = ' + str(popMax) + '\nMean = ' + str(popMean) + '\nStd = ' + str(popStd)) 
   
    pylab.show()

def oneDrugTreatment(delay):
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    numStepsPostDrug = 150
    
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for v in range(numViruses)]
    patient = TreatedPatient(viruses, maxPop)
        
    for i in range(delay):
        patient.update()
            
    patient.addPrescription('guttagonol')   
    
    for i in range(numStepsPostDrug - 1):
        patient.update()

    return patient.update()

def twoDrugTreatment(delay):
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    numStepsPreFirstDrug = 150
    numStepsPostDrug = 150
    
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for v in range(numViruses)]
    patient = TreatedPatient(viruses, maxPop)
        
    for i in range(numStepsPreFirstDrug):
        patient.update()
                
    patient.addPrescription('guttagonol')   
    
    for i in range(delay):
        patient.update()
    
    patient.addPrescription('grimpex') 
            
    for i in range(numStepsPostDrug - 1):
        patient.update()

    return patient.update()
    
def executeTreatment(numTrials, treatment, delay):
    virusPopulations = [0] * numTrials
    
    for i in range(numTrials):
        virusPopulations[i] = treatment(delay)
    
    return virusPopulations

def main():
    random.seed(0)
    #simulationDelayedTreatment(100)
    simulationTwoDrugsDelayedTreatment(100)
    
if __name__ == '__main__':
    main()