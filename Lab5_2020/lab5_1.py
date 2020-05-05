import numpy as np
from simple_markov_chain_lib import markov_chain

## Build Markov Chain
markov_table = {
    1: {2: 0.5, 3: 0.5},
    2: {1: 1/3, 4: 2/3},
    3: {3: 0.8, 4: 0.2},
    4: {1: 0.6, 4: 0.4}
}

for starting in [1,2,3,4]:
    init_dist = {starting: 1.0} #the chain starts from state 1 since we are interested in excursions around state 1.

    mc = markov_chain(markov_table, init_dist)

    N = 100_000

    ##Initialize the dictionary "visits". Every state is a key of this dictionary, with value 0
    visits = {state: 0 for state in (1, 2, 3, 4)} 

    mc.start()
    completed = 0
    stoppingTimeCounter = 0
    stoppingTimes = []
    ##Simulate N excursions. Every time we complete an excursion we increase completed by 1.
    while completed < N:
        visits[mc.running_state] += 1
        mc.move()
        stoppingTimeCounter += 1
        if mc.running_state == starting:
            stoppingTimes.append(stoppingTimeCounter)
            stoppingTimeCounter = 0
            completed +=1

    print("Invariant Distribution starting from {}:".format(starting))
    for x, y in visits.items():
        print("%d: %.3f" % (x, (y / N)/np.mean(stoppingTimes)))

