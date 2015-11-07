def compareOperators(op1, op2):
	operator1 = operatorToNumber(op1)
	operator2 = operatorToNumber(op2)

	if (operator1 == 3) and (operator2 == 3):
		return 1
	elif operator1 > operator2:
		return 1
	elif operator1 <= operator2:
		return -1		

def operatorToNumber(operator):
	if operator == ")":
		return 0
	elif operator == "(":
		return 0
	elif operator == "-":
		return 1
	elif operator == "+":
		return 1
	elif operator == "//":
		return 2
	elif operator == "%":
		return 2
	elif operator == "/":
		return 2
	elif operator == "*":
		return 2
	elif operator == "^":
		return 3

def operatorMath(operand1, operator, operand2):
	if operand1 == None:
		operand1 = 0
	if operand2 == None:
		operand2 = 0

	if operator == "-":
		return (num(operand1) - num(operand2))
	elif operator == "+":
		return (num(operand1) + num(operand2))
	elif operator == "//":
		return (num(operand1) // num(operand2))
	elif operator == "%":
		return (num(operand1) % num(operand2))
	elif operator == "/":
		return (num(operand1) / num(operand2))
	elif operator == "*":
		return (num(operand1) * num(operand2))
	elif operator == "^":
		return (num(operand1) ** num(operand2))	

def convertToString(list):
	if len(list) == 1:
		result = list[0]
	else:
		result = list[0]
		for i in range(1,len(list)):
			result = result + ", " + list[i]
	return result

def num(s):
    return float(s)
	#try:
        #return int(s)
    #except ValueError:
        #return float(s)