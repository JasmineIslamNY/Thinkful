def compareOperators(op1, op2):
	operator1 = operatorToNumber(op1)
	operator2 = operatorToNumber(op2)

	if operator1 > operator2:
		return 1
	elif operator1 <= operator2:
		return -1		

def operatorToNumber(operator):
	if operator == "-":
		return 1
	elif operator == "+":
		return 2
	elif operator == "//":
		return 3
	elif operator == "%":
		return 4
	elif operator == "/":
		return 5
	elif operator == "*":
		return 6
	elif operator == "^":
		return 7

def operatorMath(operand1, operator, operand2):
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


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)