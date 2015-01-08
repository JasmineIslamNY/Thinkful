import authorization
import requests
import argparse
import logging
import json
import sys
import urlparse
from urls import *

def read_tweets(limit):
	""" This will read the last 10 tweets tweeted"""
	try:
		int(limit)
		if (limit >= 1 or limit <= 3200):
			limit = str(limit)
		else:
			limit = '10'
	except TypeError: 
		limit = '10'
	
	print "Printing the last {} tweets".format(limit)
	auth = authorization.authorize()
	url = USERTIMELINE_URL + "&count=" + limit
	response = requests.get(url, auth=auth)
	#tweets = json.loads(response)
	#for tweet in tweets:
	#	print tweet["text"]
	#tweets = urlparse.parse_qs(response.content)
	#first_tweet = tweets.get("text")
	#tweet = json.load(tweets)
	#print tweet
	#print first_tweet
	print json.dumps(response.json(), indent=4)
	print " "

def write_tweets(tweet):
	""" This will send a tweet"""
	while True:
		if (tweet == 'C' or tweet == 'c' or tweet == ' '):
			print " "
			return 1
		elif (tweet == 'Q' or tweet == 'q'):
			print " "
			sys.exit(0)
		elif (len(tweet) >= 1 and len(tweet) <= 140):
			payload = {'status': tweet}
			break
		else:
			tweet = raw_input("Enter your Tweet (C to Cancel or Q to Quit):")
	
	auth = authorization.authorize()
	response = requests.post(TWEET_URL, auth=auth, data=payload)
	if response.status_code == 200:
		print " "
		print "Tweet Successful. Code: {}".format(response)
		print " "
	else:
		print " "
		print "Something went wrong. Code: {}".format(response)
		print " "
		
def get_option():
	""" This will get the selected option from the user - tweet or read tweet """
	print "What would you like to do?"
	print "    Option 1: You can write a tweet"
	print "    Option 2: You can read your tweets"
	print "    Q to quit the app"
	option = ''
	while not(option == '1' or option == '2' or option == 'Q' or option == 'q'):
		option = raw_input("Please select your option (1 or 2): ")
	if (option == 'Q' or option == 'q'):
		sys.exit(0)
	option = int(option)
	return option
		
def make_parser():
	""" Construct the command line parser """
	logging.info("Constructing parser")
	description = "This app allows you to send and retrieve tweets"
	parser = argparse.ArgumentParser(description = description)

	subparsers = parser.add_subparsers(dest = "command", help = "Available commands")

	# Subparser for the write command
	logging.debug("Constructing write subparser")
	write_parser = subparsers.add_parser("write", help = "Send a Tweet")
	write_parser.add_argument("tweet", default= 'c', nargs = "?", help = "What do you want to tweet? Surround with quotes.")

	# Subparser for the read command
	logging.debug("Constructing read subparser")
	read_parser = subparsers.add_parser("read", help = "Retrieve your tweets")
	read_parser.add_argument("limit", default= "10", nargs = "?", help = "Set a limit, default is 10 last tweets")

	return parser

def main():
	""" Main function """
	parser = make_parser()
	arguments = parser.parse_args(sys.argv[1:])
	# Convert parsed arguments from Namespace to dictionary
	arguments = vars(arguments)
	command = arguments.pop("command")

	if command == "write":
		write_tweets(**arguments)

	if command == "read":
		read_tweets(**arguments)

	while True:
		option = get_option()
		if option == 1:
			write_tweets(raw_input("Enter your Tweet (C to Cancel or Q to Quit):"))			
		else:
			read_tweets(raw_input("Set a limit, default is 10 last tweets: ")) 
	
if __name__ == "__main__":
	main()
	
	
	
	
	