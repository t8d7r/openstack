import sys
import os
import json
import requests

from st2client.client import Client
from st2actions.runners.pythonrunner import Action
from st2client.models import KeyValuePair

class InternalDelIntf(Action):
	def run(self, image_id, auth_ip):
		i = 0
		client = Client()
		keys = client.keys.get_all()
		curr_token = client.keys.get_by_name(name='curr_token')
		url = 'http://'+auth_ip+':9292/v2/images'
		headers = {'X-Auth-Token': curr_token.value }
		try:
			r = requests.get(url, headers=headers)
			print r
			token=r.json()
			length = len(token['images'])
			print length
			if image_id == "default" :
				while i < length :
					print token['images'][i]['name']+":"+token['images'][i]['id']
					i = i + 1
			else :
				while i < length :
					if token['images'][i]['name'] == image_id :              
 						print token['images'][i]['name']+":"+token['images'][i]['id']
                			i = i + 1	
		except:
			return(1)




