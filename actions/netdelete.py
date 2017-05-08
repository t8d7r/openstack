import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, auth_ip, net_id, sub_id):
		i = 0
		paytemp = "["
		client = Client()
		keys = client.keys.get_all()
		curr_token = client.keys.get_by_name(name='curr_token').value
		url = 'http://'+auth_ip+':9696/v2.0/subnets/'+sub_id
		headers = {'X-Auth-Token': curr_token , 'Content-Type': 'application/json' }
		try:
			r=requests.delete(url, headers=headers)
			url = 'http://'+auth_ip+':9696/v2.0/networks/'+net_id
			r=requests.delete(url, headers=headers)	
		except:
			return(1)




