import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, flav_id, auth_ip):
		i = 0
		client = Client()
		keys = client.keys.get_all()
		curr_token = client.keys.get_by_name(name='curr_token')
		url = 'http://'+auth_ip+':8774/v2.1/flavors'
		headers = {'X-Auth-Token': curr_token.value }
		try:
			r = requests.get(url, headers=headers)
			print r
			token=r.json()
			length = len(token['flavors'])
			if flav_id == "default" :
				while i < length :
					print token['flavors'][i]['name']+":"+token['flavors'][i]['id']
					i = i + 1
			else :
				while i < length :
					if token['flavors'][i]['name'] == flav_id :              
 						print token['flavors'][i]['name']+":"+token['flavors'][i]['id']
                			i = i + 1	
		except:
			return(1)




