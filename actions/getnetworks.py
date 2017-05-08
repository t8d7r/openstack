import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, net_id, auth_ip):
		i = 0
		client = Client()
		keys = client.keys.get_all()
		curr_token = client.keys.get_by_name(name='curr_token')
		url = 'http://'+auth_ip+':9696/v2.0/networks'
		headers = {'X-Auth-Token': curr_token.value }
		try:
			r = requests.get(url, headers=headers)
			print r
			token=r.json()
			length = len(token['networks'])
			if serv_id == "default" :
				while i < length :
					print token['networks'][i]['name']+":id:"+token['networks'][i]['id']+":sub_id:"+token['networks'][i]['subnets'][0]
					i = i + 1
			else :
				while i < length :
					if token['networks'][i]['name'] == net_id :
						print token['networks'][i]['name']+":id:"+token['networks'][i]['id']+":sub_id:"+token['networks'][i]['subnets'][0]              
                			i = i + 1	
		except:
			return(1)




