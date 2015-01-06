import authorization
import requests
import json
from urls import *

def main():
	""" Main Function """
	auth = authorization.authorize()
	response = requests.get(TIMELINE_URL, auth=auth)
	print json.dumps(response.json(), indent=4)

if __name__ == "__main__":
	main()