import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, serv_id, auth_ip):
		i = 0
		client = Client()
		keys = client.keys.get_all()
		proj_id = client.keys.get_by_name(name='curr_project_id')
		curr_token = client.keys.get_by_name(name='curr_token')
		print proj_id.value+'\n'
		print curr_token.value+'\n'
		url = 'http://'+auth_ip+'/v2.1/'+proj_id.value+'/servers'
		print url+'\n'
		headers = {'X-Auth-Token': curr_token.value }
		try:
			r = requests.get(url, headers=headers)
			print r
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




