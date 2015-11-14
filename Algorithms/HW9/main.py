from dataobject import DataObject
from outputjson import OutputJSON
from outputxml import OutputXML
from inputjson import InputJSON

if __name__ == "__main__":
	text = '{ "fname": "Jasmine", "lname": "Islam", "address": [  { "street": "63 S Terrace Place", "city": "Valley Stream" },  { "street": "731 Lexington Ave", "city": "New York" } ], "phone_numbers": { "home": "(516) 837-0641", "mobile": "(347) 423-7387" }}'

	processed = InputJSON(text)
	text = OutputJSON(processed)
	print(text.json)
	
	output = OutputXML(processed.processedInput)
	print(output.xml)
