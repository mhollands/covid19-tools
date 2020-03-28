# covid19-tools
Python script to quickly plot data from around the world. Uses https://covid19api.com API. 

# Structure
core.py - main python functions

covid19.py - command line interface

# Development
Import core.py into your code to use functions

# Use from command line
run 'python3 covid19.py' to use command line tool.

With no arguments, script will print available countries.

Specify a country and the script will print available provinces.

-c/--country <country> - specify country
  
-p/--province <province> - specify province
  
-g/--graph - draws a graph

-s/--save - save data to file

-d/--delta - plot deltas instead of absolute values

e.g. python3 covid19.py -c US -p California -g -s

# Dependencies
There are various libraries required.
