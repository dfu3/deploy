import os
import sys

vers = 'v7'
tier = 'qa'
mach = 'back'

if(len(sys.argv) == 2):
	tier = sys.argv[1]
elif(len(sys.argv) == 3):
	tier = sys.argv[1]
	vers = sys.argv[2]

os.system('curl  http://10.200.172.51:5000/request/' + tier + '/' + mach + '/' + vers)
