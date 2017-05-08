import sys
import os
from st2client.client import Client
from st2actions.runners.pythonrunner import Action

class InternalDelIntf(Action):
	def run(self, chain1):
		try:
			i = 0
			while i < len(chain1):
				print(chain1[i])
				i = i + 1
		except:
			return(1)
