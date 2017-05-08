import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, auth_ip, serv_name, secgrp_id, flav_id, image_id, nets):
		i = 0
		paytemp = "["
		client = Client()
		keys = client.keys.get_all()
		proj_id = client.keys.get_by_name(name='curr_project_id').value
		curr_token = client.keys.get_by_name(name='curr_token').value
		print (curr_token)
		url = 'http://'+auth_ip+':8774/v2.1/'+proj_id+'/servers'
		payload = {"server": {"name": serv_name,"imageRef": image_id,"flavorRef": flav_id,"security_groups": [{"name": secgrp_id}], }}
		payload ['server']['networks'] = [dict(uuid=netid) for netid in nets]
		headers = {'X-Auth-Token': curr_token , 'Content-Type': 'application/json' }
		try:
			r=requests.post(url, data=json.dumps(payload), headers=headers)
			print r
		except:
			return(1)




