
import requests
import json
from tokens import getCreds
import datetime

def makeApiCall(url, endpointParams, debug = 'no'):
	data = requests.get(url, endpointParams)

	response = dict()

	response['url'] = url
	response['endpoint_params'] = endpointParams
	response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)
	response['json_data'] = json.loads(data.content)
	response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)

	if ('yes' == debug):
		displayApiCallData(response)

	return response

def displayApiCallData(response):
	print("\nURL: ")
	print(response['url'])
	print("\nEnpoint Params: ")
	print(response['endpoint_params_pretty'])
	print("Response: ")
	print(response['json_data_pretty'])


def debugAccessToken(params):
	endpointParams = dict()
	endpointParams['input_token'] = params['access_token']
	endpointParams['access_token'] = params['access_token']

	url = params['graph_domain'] + '/debug_token'

	return makeApiCall(url, endpointParams, params['debug'])

def getLongLivedAccessToken(params):
	endpointParams = dict()
	endpointParams['grant_type'] = 'fb_exchange_token'
	endpointParams['client_id'] = params['client_id']
	endpointParams['client_secret'] = params['client_secret']
	endpointParams['fb_exchange_token'] = params['access_token']

	url = params['endpoint_base'] + 'oauth/access_token'

	return makeApiCall(url, endpointParams, params['debug'])
#params = getCreds()
#params['debug'] = 'yes'
#response = debugAccessToken(params)

#print('Data Acces Expires: ')
#print(datetime.datetime.fromtimestamp(response['json_data']['data']['data_access_expires_at']))

#print('Token Expires: ')
#print(datetime.datetime.fromtimestamp(response['json_data']['data']['expires_at']))


