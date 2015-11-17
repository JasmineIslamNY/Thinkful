from dataobject import DataObject
from outputjson import OutputJSON
from outputxml import OutputXML
from inputjson import InputJSON
from inputxml import InputXML

if __name__ == "__main__":
	
	
	textjson = '{"fname": "Jasmine", "lname": "Islam", "address": [  { "street": "63 S Terrace Place", "city": "Valley Stream" },  { "street": "731 Lexington Ave", "city": "New York" } ], "phone_numbers": { "home": "(516) 837-0641", "mobile": "(347) 423-7387" }}'

	textxml = '<person><firstName>John</firstName><lastName>Smith</lastName><age>25</age><address><streetAddress>21 2nd Street</streetAddress><city>New York</city><state>NY</state><postalCode>10021</postalCode></address><phoneNumbers><phoneNumber><type>home</type><number>212 555-1234</number></phoneNumber><phoneNumber><type>fax</type><number>646 555-4567</number></phoneNumber></phoneNumbers><gender><type>male</type></gender></person>'


	print("Original JSON")
	print("-------------")
	print("             ")
	print(textjson)
	print("             ")

	print("Processed JSON")
	print("-------------")
	print("             ")
	processed = InputJSON(textjson)
	temp = OutputJSON(processed.processedInput)
	print(temp.json)
	print("             ")

	print("Processed XML")
	print("-------------")
	print("             ")
	processed = InputJSON(textjson)
	temp = OutputXML(processed.processedInput)
	print(temp.xml)
	print("             ")

	print("*************")

	print("Original XML")
	print("-------------")
	print("             ")
	print(textxml)
	print("             ")

	print("Processed XML")
	print("-------------")
	print("             ")
	processed = InputXML(textxml)
	temp = OutputJSON(processed.processedInput)
	print(temp.json)
	print("             ")

	print("Processed XML")
	print("-------------")
	print("             ")
	processed = InputXML(textxml)
	temp = OutputXML(processed.processedInput)
	print(temp.xml)
	print("             ")
