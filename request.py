import os 
import sys

print '--------------------'
vers = raw_input("|version: ")
tier = raw_input("|tier: ")
mach = raw_input("|machine: ")
print '--------------------'

# if(len(sys.argv) == 2):
# 	tier = sys.argv[1]
# elif(len(sys.argv) == 3):
# 	tier = sys.argv[1]
# 	vers = sys.argv[2]

print mach + ':' + tier + ':' + vers
#os.system('curl  http://10.200.172.28:5000/request/' + tier + '/' + mach + '/' + vers)
