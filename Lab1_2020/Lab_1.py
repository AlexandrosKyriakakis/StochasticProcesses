from simple_markov_chain_lib import markov_chain  # import markov chain simulator
rooms = ["Kitchen", "Library", "Livingroom", "Bedroom", "Bathroom"]
# Transition Table
markov_table = {
    rooms[0]: {rooms[1]: .5, rooms[2]: .5},  
    rooms[1]: {rooms[0]: .5, rooms[2]: .5},
    rooms[2]: {rooms[0]: .25, rooms[1]: .25, rooms[3]: .25, rooms[4]: .25, },
    rooms[3]: {rooms[2]: 1.},
    rooms[4]: {rooms[2]: 1.}
}

# Initial Distribution
init_dist = {rooms[3]: 1.}  # we start from state 0 with probability 1

mc = markov_chain(markov_table, init_dist)
counterKitchen = 0
counterBed = 0
mc.start()
print("At time {} the chain is in state {}".format(mc.steps, mc.running_state))
N = 20
#N = 1000000
for i in range(N):
    mc.move()
    if (mc.running_state == "Kitchen"): counterKitchen += 1
    if (mc.running_state == "Bedroom"): counterBed += 1
    print("At time {} the chain is in state {}".format(mc.steps, mc.running_state))
print("P[x = Kitchen] = ",counterKitchen/N," P[x = Bedroom] = ", counterBed/N)


