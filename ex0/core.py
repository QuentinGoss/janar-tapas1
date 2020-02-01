import env
import os
import pantherine as purr
import vehicle

###############################
# Initilize anything that needs to happen at step 0 here.
###############################
def initialize(traci):
    os.system("cls")
    print("Initializing...")
    
    trips = purr.readXMLtag(purr.mrf(env.map_dir,r"*.trips.xml"),"trip")
    
    total = len(trips) - 1
    print('Number of trips:',len(trips))
    for i,trip in enumerate(trips):
        veh = vehicle.Vehicle("veh%d" % (i))
        try:
            veh.add(traci,trip['from'],trip['to'],trip['depart'])
        except:
            pass
        env.vehicles.append(veh)
        purr.update(i,total)

    print("Initialization complete!")
    return
# end def intialize


###############################
# Anything that happens within the TraCI control loop goes here.
# One pass of the loop == 1 timestep.
# Return False to finalize the simulation
###############################
def timestep(traci,n_step):
    if traci.simulation.getTime() > 28799 and traci.vehicle.getIDCount() == 0:
        return False
    return True
# end timestep

###############################
# Finalize the Simulation
###############################
def finalize():
    
    return
# End finalize
