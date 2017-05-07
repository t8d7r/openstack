import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, auth_user, auth_password, auth_project, auth_ip):
		client = Client()
		url = 'http://'+auth_ip+':5000/v3/auth/tokens'
		payload = { 'auth': {'identity': {'methods': ['password'],'password': {'user': {'name': auth_user,'domain': { 'id': 'default' },'password': auth_password}}},'scope': {'project': {'name': auth_project,'domain': { 'id': 'default' }}}}}
		try:
			r=requests.post(url, data=json.dumps(payload))
			token=r.headers['X-Subject-Token']
			client.keys.update(KeyValuePair(name='curr_token', value=token))
			client.keys.update(KeyValuePair(name='curr_user', value=auth_user))
			client.keys.update(KeyValuePair(name='curr_project', value=auth_project))
			keys = client.keys.get_all()
			print(client.keys.get_by_name(name='curr_token'))
			print(client.keys.get_by_name(name='curr_user'))
			print(client.keys.get_by_name(name='curr_project'))
			
		except:
			return(1)




