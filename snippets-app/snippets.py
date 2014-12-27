import logging
import csv
import argparse
import sys

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name, snippet, filename):
	""" Store a snippet with an associated name in the CSV file """
	logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
	logging.debug("Opening file")
	with open(filename, "a") as f:
		writer = csv.writer(f)
		logging.debug("Writing snippet to file")
		writer.writerow([name, snippet])
	logging.debug("Write successful")
	return name, snippet

def get(name, filename):
	""" Get a snippet from a file when the snippet name is listed """
	logging.info("Retrieving {!r} from {!r}".format(name, filename))
	logging.debug("Reading the file")
	count = 0
	with open(filename, "r") as file:
		reader = csv.reader(file)
		for row in reader:
			if row[0] == name:
				print "The snippet for {!r} is {!r}".format(row[0], row[1])
				count += 1
	if count == 1:
		instance = "one instance"
	else:
		instance = str(count) + " instances"
	return name, filename, instance

def find(snippet, filename):
	""" Get a snippet and name from a file when the snippet is listed """
	logging.info("Looking for {!r} from {!r}".format(snippet, filename))
	logging.debug("Reading the file")
	count = 0
	with open(filename, "r") as file:
		reader = csv.reader(file)
		for row in reader:
			if row[1].count(snippet) > 0:
				print "Found {!r} in {!r}: the full snippet is {!r}".format(snippet, row[0], row[1])
				count += 1
	if count == 1:
		instance = "one snippet"
	else:
		instance = str(count) + " snippets"
	return filename, instance
		
def make_parser():
	""" Construct the command line parser """
	logging.info("Constructing parser")
	description = "Store and retrieve snippets of text"
	parser = argparse.ArgumentParser(description = description)
	
	subparsers = parser.add_subparsers(dest = "command", help = "Available commands")
	
	# Subparser for the put command
	logging.debug("Constructing put subparser")
	put_parser = subparsers.add_parser("put", help = "Store a snippet")
	put_parser.add_argument("name", help = "The name of the snippet")
	put_parser.add_argument("snippet", help = "The snippet text")
	put_parser.add_argument("filename", default= "snippets.csv", nargs = "?", help = "The snippet filename")
	
	# Subparser for the get command
	logging.debug("Constructing get subparser")
	get_parser = subparsers.add_parser("get", help = "Retrieve a snippet")
	get_parser.add_argument("name", help = "The name of the snippet")
	get_parser.add_argument("filename", default= "snippets.csv", nargs = "?", help = "The snippet filename")
	
	
	# Subparser for the find command
	logging.debug("Constructing find subparser")
	find_parser = subparsers.add_parser("find", help = "Retrieve a snippet")
	find_parser.add_argument("snippet", help = "A segment of the snippet")
	find_parser.add_argument("filename", default= "snippets.csv", nargs = "?", help = "The snippet filename")
	
	return parser
	
def main():
	""" Main function """
	logging.info("Starting snippets")
	parser = make_parser()
	arguments = parser.parse_args(sys.argv[1:])
	# Convert parsed arguments from Namespace to dictionary
	arguments = vars(arguments)
	command = arguments.pop("command")
	
	if command == "put":
		name, snippet = put(**arguments)
		print "Stored {!r} as {!r}".format(snippet, name)
		
	if command == "get":
		name, filename, instance = get(**arguments)
		print "Retrieved {} of {!r} from {!r}".format(instance, name, filename)
	
	if command == "find":
		filename, instance = find(**arguments)
		print "Retrieved {} from {!r}".format(instance, filename)
	
if __name__ == "__main__":
	main()
	