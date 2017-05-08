import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, auth_ip, net_name, net_cidr):
		i = 0
		paytemp = "["
		client = Client()
		keys = client.keys.get_all()
		curr_token = client.keys.get_by_name(name='curr_token').value
		proj_id = client.keys.get_by_name(name='curr_project_id').value
		print (curr_token)
		url = 'http://'+auth_ip+':9696/v2.0/networks'
		payload = {"network": {"name": net_name,"admin_state_up": "true", "port_security_enabled" : "false", "tenant_id" : proj_id }}
		headers = {'X-Auth-Token': curr_token , 'Content-Type': 'application/json' }
		try:
			r=requests.post(url, data=json.dumps(payload), headers=headers)
			url = 'http://'+auth_ip+':9696/v2.0/subnets'
                	payload = {"subnet": {"network_id":r.json()["network"]["id"],"ip_version": 4,"cidr": net_cidr,"name":net_name}}
                	headers = {'X-Auth-Token': curr_token , 'Content-Type': 'application/json' }
			r=requests.post(url, data=json.dumps(payload), headers=headers)	
		except:
			return(1)




