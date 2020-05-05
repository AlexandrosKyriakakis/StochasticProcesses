import statistics as stat
import random
random.seed(2020)  # for reproducibility
from simple_markov_chain_lib import markov_chain

p = 1/6
for p in [1/6,1/12]:
    print ("p = ",p);
    # A dictionary for the initial distibution. 
    # We prescribe the initial distribution
    init_probs = {1: 1.0} 
    
    # A dictionary for the transition probability  matrix. 
    # Every state-key corresponds to a list with tuples of (Next_State,Probability) 
    markov_table = {
        1: {2: 1.},
        2: {2: 2/3, 3: 1/3},
        3: {1: p, 2: 1-p}
    }
    
    # Ok... we are ready know
    # Let's construct a Markov Chain. So let's call the constructor
    mc = markov_chain(markov_table, init_probs)
    for init in [1,3]:
        print ("Initial state =",init)
        init_probs = {init: 1.0} 
        for N in [50,200,20000]:
            print ("N = ",N)
            ## Experiment parameters
            #N = 1000     # number of samples
            steps = 20   # the target time
            counter = 0  # to count the number of times the event {X_40  = 1} occurs

            ## Simulation
            for i in range(N):
                mc.start()  # new experiment
                for j in range(steps):  mc.move()
                if mc.running_state == 1:  counter += 1

            phat = counter / N

            print(
                """
                We executed {0} times the first {1} steps of the markov chain
                and we captured the running state in state one {2} times.
                So we estimate the Pr[X_{1} = 1 | X_0 = 1] to be {3}
                """.format(N, steps, counter, phat)
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
                ## compute the SAMPLE mean and variance of the elements in our list keeping only 5 decimal digits