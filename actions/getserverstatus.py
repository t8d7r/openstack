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
		net_count = 0
		client = Client()
		keys = client.keys.get_all()
		curr_token = client.keys.get_by_name(name='curr_token')
		print curr_token
		proj_id = client.keys.get_by_name(name='curr_project_id')
		url = 'http://'+auth_ip+':8774/v2.1/'+proj_id.value+'/servers/'+serv_id
		headers = {'X-Auth-Token': curr_token.value }
		try:
			r = requests.get(url, headers=headers)
			print r
			token=r.json()
			print token['server']['name']+":id:"+token['server']['id']+":status:"+token['server']['status']+":tenant:"+token['server']['tenant_id']
			for address in token['server']['addresses']:
				print "net:"+token['server']['addresses'].keys()[net_count]+":ip:"+token['server']['addresses'][address][0]['addr']+":mac:"+token['server']['addresses'][address][0]['OS-EXT-IPS-MAC:mac_addr']
				net_count = net_count + 1
		except:
			return(1)




