questions = {     
	"strong": "Do ye like yer drinks strong?",     
	"salty": "Do ye like it with a salty tang?",     
	"bitter": "Are ye a lubber who likes it bitter?",     
	"sweet": "Would ye like a bit of sweetness with yer poison?",     
	"fruity": "Are ye one for a fruity finish?" 
	}  

ingredients = {     
	"strong": ["glug of rum", "slug of whisky", "splash of gin"],     
	"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],     
	"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],     
	"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],     
	"fruity": ["slice of orange", "dash of cassis", "cherry on top"] 
	}

responses = {}

def drink_style():
	for question in questions:
		print questions[question]
		answer = raw_input("Please enter Yes or No: ")
		if (answer.upper() == 'YES') or (answer.upper() == 'Y'):
			responses[question] = True
		else:
			responses[question] = False
	print responses
	return responses

def make_drink(selections):
	import random 
	drink = []
	for selection in selections:
		if selections[selection] == True:
			drink.append(random.choice(ingredients[selection]))
                
	your_drink = "Your drink is made from " + str(drink[0])                                                                   
	for i in range(1,len(drink)):
		your_drink = your_drink + ", " + str(drink[i]) 
		
	return your_drink

if __name__ == '__main__':
	drink_style()
	print make_drink(responses)
