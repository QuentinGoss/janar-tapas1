# options.py
# Author: Quentin Goss
# The options parser options are here
import optparse
import env
import sys
import os
import pantherine as purr

def get_options():
    opt_parser = optparse.OptionParser()
    # GUI
    opt_parser.add_option("--nogui",action="store_true",default=False, help="run the commandline version of sumo")
    #
    opt_parser.add_option('--seed',type='int',dest='seed',default=8635839050,help='Random Seed')
    opt_parser.add_option('--map-dir',type='string',dest='map_dir',default=None,help='Directory of SUMO map files')
    #
    options, args = opt_parser.parse_args()

    # Validate Options
    if options.map_dir == None:
        print('Please specify a map directory with --map-dir')
        sys.exit(1)
    
    env.map_dir = options.map_dir
    return options
