# janar-tapas1
 Learning Project for SUMO Intro

This is an introduction to using SUMO and TraCI. Please copy the directory `ex1`, a bare-bones TraCI project that is as simple as I can make it.

## Installation
You must have Python 3.x, and SUMO installed. The SUMO tools directory should be in your system path (Which should be automatically done during SUMO installation). 

## The structure of a project
Provided are two .bat files for running your project. One for a gui (`test.bat`), and one for no-gui (`test-nogui.bat`). Setting up Traci, importing the libraries, and setting up the SUMO street network is already taken of. The only file that you need to edit is `core.py`, (and any python scripts you create).

### core.py
Inside `core.py` are three simple methods. `initialize`, `timestep`, and `finalize`.

#### initialize
This is timestep 0, the start of the simulation. Any code that needs to happen before the simulation runs goes here. The bulk of preprocessing should happen here.

#### timestep
This function is called every 1 second of simulation time, or 1 timestep. The simulation runs until this method returns `False`.

#### finalize
When `timestep` returns `false` and the Simulation concludes, this method is called before the TraCI server is detached. Write output files in this method.

## Task 1
The goals of this first task are the following:
- Familiarize yourself with SUMO and TraCI
- Understand the three stages of simulation, `initialize`, `timestep`, and `finalize`.

In `TAPASCologne-0.32.0` directory, there is a file `cologne6to8.trips.xml`. It's a really long file that you can open with `lister.exe` (useful for reading long files quickly). This file contains route information, *from* is a source edge ID and *to* is a destination edge ID. The following chunk of code will read in this trip data into a Python dictionary:
```
import pantherine as purr
trips = purr.readXMLtag(
    purr.mrf(env.map_dir,r'*6to8.trips.xml'),
    'trip'
)
purr.head(trips,10)
purr.pause()
```

Create 100 vehicles with routes that correspond to the first 100 trips of `cologne6to8.trips.xml`. When all of the vehicles have reached their destinations, return `False` in the `timestep` method to end the simulation. Use `vehicle.py` as a guidline.

#### Usefull Links
https://sumo.dlr.de/docs/TraCI.html
