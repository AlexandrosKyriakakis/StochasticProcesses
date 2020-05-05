import statistics as stat
import numpy as np
import random
random.seed(2020)  # for reproducibility
from simple_markov_chain_lib import markov_chain

p = 0.6
q = 1-p
        #   0       1       2       3       4      
States = ["0-0", "15-0", "0-15", "30-0", "15-15",
        #  5       6       7       8       9     
         "0-30", "40-0","30-15","15-30","0-40",
        #   10      11       12     13      14   
         "40-15","Deuce", "15-40","GameA","AdvA",
        #    15      16            
           "AdvB","GameB"]
# A dictionary for the initial distibution. 
# We prescribe the initial distribution
# A dictionary for the transition probability  matrix. 
# Every state-key corresponds to a list with tuples of (Next_State,Probability) 
p = 0.5
q = 0.5
markov_table = {
    States[0]: {States[1]: p, States[2]: q},
    States[1]: {States[3]: p, States[4]: q},
    States[2]: {States[4]: p, States[5]: q},
    States[3]: {States[6]: p, States[7]: q},
    States[4]: {States[7]: p, States[8]: q},
    States[5]: {States[8]: p, States[9]: q},
    States[6]: {States[13]: p, States[10]: q},
    States[7]: {States[10]: p, States[11]: q},
    States[8]: {States[11]: p, States[12]: q},
    States[9]: {States[12]: p, States[16]: q},
    States[10]: {States[13]: p, States[14]: q},
    States[11]: {States[14]: p, States[15]: q},
    States[12]: {States[15]: p, States[16]: q},
    States[13]: {States[13]: 1.},
    States[14]: {States[13]: p, States[11]: q},
    States[15]: {States[11]: p, States[16]: q},
    States[16]: {States[16]: 1.}
}
init_probs = {States[0]: 1.0} 
# Ok... we are ready know
# Let"s construct a Markov Chain. So let"s call the constructor
mc = markov_chain(markov_table, init_probs)
for N in [50,200,20000]:
    print ("N = ",N)
    ## Experiment parameters
    #N = 1000     # number of samples
    steps = 0  # the target time
    stepsTrack = []
    counter = 0  # to count the number of times the event {X_40  = 1} occurs

    ## Simulation
    for i in range(N):
        mc.start()  # new experiment
        while(mc.running_state not in [States[13],States[16]]):  
            mc.move()
            steps += 1
        if mc.running_state == States[13]:  
            counter += 1
            stepsTrack.append(steps)
        steps = 0
    phat = counter / N

    print(
        """
        We executed {0} times the first {1} steps until game ends of the markov chain
        and we captured the running state in state {4} {2} times.
        So we estimate the Pr[X_{1} = {4} | X_0 = {5}] to be {3}
        """.format(N, int(np.round(np.mean(stepsTrack))), counter, phat,States[13],States[0])
    )

    ## import the library statistics. We will use it to compute the mean and variance of our list
    estimates=[] ## create the empty list estimates.
    for i in range(N): estimates.append(random.gauss(0,1)) 
        ## in each of 100 runs generate a sample from the standard normal distribution and append it to the list estimates
    print(
        """ 
        The sample mean is {0:.5f} and the sample variance is {1:.5f}
        """.format(stat.mean(estimates), stat.variance(estimates))
    )
myarray = np.array([
     #0 1 2 3 4 5 6 7 8 9 10  11 12 13 14 15 16
     [0,p,q,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0], #0
     [0,0,0,p,q,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0], #1
     [0,0,0,0,p,q,0,0,0,0, 0, 0, 0, 0, 0, 0, 0], #2 
     [0,0,0,0,0,0,p,q,0,0, 0, 0, 0, 0, 0, 0, 0], #3
     [0,0,0,0,0,0,0,p,q,0, 0, 0, 0, 0, 0, 0, 0], #4
     [0,0,0,0,0,0,0,0,p,q, 0, 0, 0, 0, 0, 0, 0], #5
     [0,0,0,0,0,0,0,0,0,0, q, 0, 0, p, 0, 0, 0], #6
     [0,0,0,0,0,0,0,0,0,0, p, q, 0, 0, 0, 0, 0], #7
     [0,0,0,0,0,0,0,0,0,0, 0, p, q, 0, 0, 0, 0], #8
     [0,0,0,0,0,0,0,0,0,0, 0, 0, p, 0, 0, 0, q], #9
     [0,0,0,0,0,0,0,0,0,0, 0, 0, 0, p, q, 0, 0], #10
     [0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, p, q, 0], #11
     [0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, p, q], #12
     [0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 1., 0, 0, 0], #13
     [0,0,0,0,0,0,0,0,0,0, 0, q, 0, p, 0, 0, 0], #14
     [0,0,0,0,0,0,0,0,0,0, 0, p, 0, 0, 0, 0, q], #15
     [0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 1.]  #16
])
for i in range(1000): myarray = myarray.dot(myarray)        ## compute the SAMPLE mean and variance of the elements in our list keeping only 5 decimal digits
print (myarray)

