# vehicle.py

class Vehicle(object):
    vid = str()
    vid_sumo = str()
    n_veh = 0
    depart_time = None
    arrival_time = None
    
    def __init__(self,vid):
        self.vid = vid
        return
    
    # Adds a SUMO vehicle
    # @param traci = traci instance
    # @param string src = Source Edge ID
    # @param string dst = Destination Edge ID
    # @param double depart = Depart Time
    def add(self,traci,src,dst,depart):
        # Create 1-edge route
        rid = "oer_%d" % (traci.route.getIDCount())
        traci.route.add(rid,[src])
        
        # Add the vehicle to the route
        self.vid_sumo = self.vid
        self.n_veh += 1
        traci.vehicle.add(self.vid_sumo,rid,depart=depart)
        
        # Change target
        traci.vehicle.changeTarget(self.vid_sumo,dst)
        return    
    
    # Checks if the vehicle exists in the sumo instance 
    # @param traci = traci instance
    def exists(self,traci):
        try:
            traci.vehicle.getSpeed(self.vid_sumo)
        except:
            return False
        return True
    
    # Checks if the vehicle has departed
    # @param traci = traci instance
    def departed(self,traci):
        if self.depart_time == None:
            if traci.vehicle.getRouteIndex(self.vid_sumo) < 0:
                return False
            else:
                self.depart_time = traci.simulation.getTime()
                return True
        return True
    
    # Checks if the vehicle has arrived
    # @param traci = traci instance
    def arrived(self,traci):
        if not arrival_time == None:
            if (not depart_time == None) and (not self.exists(traci)):
                self.arrival_time = traci.simulation.getTime()
                return True
            else:
                return False
        return False
    pass
