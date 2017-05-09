import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, auth_ip, port_id,ips):
		i = 0
		client = Client()
		keys = client.keys.get_all()
		proj_id = client.keys.get_by_name(name='curr_project_id').value
		curr_token = client.keys.get_by_name(name='curr_token').value
		print (curr_token)
		url = 'http://'+auth_ip+':9696/v2.0/ports/'+port_id
		print url
		payload ={"port":{}}
		payload ['port']['allowed_address_pairs'] = [dict(ip_address=ip) for ip in ips]
		print payload
		headers = {'X-Auth-Token': curr_token , 'Content-Type': 'application/json' }
		try:
			r=requests.put(url, data=json.dumps(payload), headers=headers)
			print r
		except:
			return(1)




