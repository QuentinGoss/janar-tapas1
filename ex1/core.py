import env
import os
import pantherine as purr

###############################
# Initilize anything that needs to happen at step 0 here.
###############################
def initialize(traci):
    os.system("cls")
    print("Initializing...")

    print("Initialization complete!")
    return
# end def intialize


###############################
# Anything that happens within the TraCI control loop goes here.
# One pass of the loop == 1 timestep.
# Return False to finalize the simulation
###############################
def timestep(traci,n_step):
    return True
# end timestep

###############################
# Finalize the Simulation
###############################
def finalize():
    
    return
# End finalize
