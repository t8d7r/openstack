import sys
import os
from st2actions.runners.pythonrunner import Action
try:
	print str(sys.argv[1])+str(sys.argv[2])+str(sys.argv[3])
except:
	exit(1)
