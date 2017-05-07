import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, user, password, project, ip):
		client = Client(base_url='http://localhost')
		url = 'http://'+ip+'/v3/auth/tokens'
		payload = { "auth": {'identity': {'methods': ['password'],'password': {'user': {'name': user,'domain': { 'id': 'default' },'password': password}}},'scope': {'project': {'name': project,'domain': { 'id': 'default' }}}}}
		try:
			r=requests.post(url, data=json.dumps(payload))
			token=r.headers['X-Subject-Token']
			client.keys.update(KeyValuePair(name='token', value=token))
			client.keys.update(KeyValuePair(name='user', value=user))
			client.keys.update(KeyValuePair(name='project', value=project))
			
		except:
			return(1)




