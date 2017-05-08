import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, port_id, auth_ip):
		i = 0
		client = Client()
		keys = client.keys.get_all()
		curr_token = client.keys.get_by_name(name='curr_token')
		url = 'http://'+auth_ip+':9696/v2.0/ports'
		headers = {'X-Auth-Token': curr_token.value }
		try:
			r = requests.get(url, headers=headers)
			print r
			token=r.json()
			length = len(token['ports'])
			if port_id == "default" :
				while i < length :
					print "id:"+token['ports'][i]['id']+":mac:"+token['ports'][i]['mac_address']+":ip:"+token['ports'][i]['fixed_ips'][0]['ip_address']+":net_id:"+token['ports'][i]['fixed_ips'][0]['subnet_id']
					i = i + 1
			else :
				while i < length :
					if token['ports'][i]['id'] == port_id :
						print "id:"+token['ports'][i]['id']+":mac:"+token['ports'][i]['mac_address']+":ip:"+token['ports'][i]['fixed_ips'][0]['ip_address']+":net_id:"+token['ports'][i]['fixed_ips'][0]['subnet_id']
                			i = i + 1	
		except:
			return(1)




