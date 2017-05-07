import sys
import os
from st2client.client import Client
from st2actions.runners.pythonrunner import Action

class InternalDelIntf(Action):
	def run(self, chain1, chain2, chain3):
		try:
			print str(chain1)+str(chain2)+str(chain3)
		except:
			return(1)
