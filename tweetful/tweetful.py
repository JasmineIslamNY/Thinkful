import authorization
import requests
import json
import urlparse
from urls import *

def read_tweets():
	""" This will read the last 10 tweets tweeted"""
	print "Read off a tweet"
	limit = '10'
	auth = authorization.authorize()
	url = USERTIMELINE_URL + "&count=" + limit
	response = requests.get(url, auth=auth)
	tweets = json.dumps(response.json(), indent=4)
	#tweets = json.load(response)
	#tweets = urlparse.parse_qs(response.content)
	#first_tweet = tweets.get("text")
	tweet = json.load(tweets)
	print tweet
	#print first_tweet
	#print json.dumps(response.json(), indent=4)
	main()
	
def write_tweets():
	""" This will send a tweet"""
	print "This will write a tweet"
	main()
	
def get_option():
	""" This will get the selected option from the user - tweet or read tweet """
	print "What would you like to do?"
	print "Option 1: You can write a tweet"
	print "Option 2: You can read your last 10 tweets"
	print "Q to quit the app"
	option = ''
	while not(option == '1' or option == '2' or option == 'Q' or option == 'q'):
		option = raw_input("Please select your option (1 or 2): ")
	if (option == 'Q' or option == 'q'):
		import sys
		sys.exit(0)
	option = int(option)
	return option
	
def main():
	""" Main Function """
	# auth = authorization.authorize()
	# response = requests.get(TIMELINE_URL, auth=auth)
	# print json.dumps(response.json(), indent=4)
	option = get_option()
	if option == 1:
		write_tweets()
	else:
		read_tweets()
	
if __name__ == "__main__":
	main()
	
	
	
	
	