import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, serv_id, proj_id, curr_token, auth_ip):
		i = 0
		client = Client()
		url = 'http://'+auth_ip+'/v2.1/'+proj_id+'/servers'
		headers = {'X-Auth-Token': curr_token }
		try:
			r = requests.get(url, headers=headers)
			token=r.json()
			length = len(token['servers'])
			if serv_id == "default" :
				while i < length :
					print token['servers'][i]['name']+":"+token['servers'][i]['id']
					i = i + 1
			else :
				while i < length :
					if token['servers'][i]['id'] == serv_id :              
 						print token['servers'][i]['name']+":"+token['servers'][i]['id']
                			i = i + 1	
		except:
			return(1)




