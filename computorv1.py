#!/usr/bin/python
import sys

class Term:
	def __init__(self, value, degree, sign, side): #ex 4 * 7x = 3 we're focusing on the left term here
		self.value = value       # 4*7 = 28
		self.degree = degree     # degree = 1 coz x = x^1 
		self.sign = sign		 # '+'
		self.side = side		 # 'l'
		
def check_equation_format(equation):
	authorized_char = [ '0','1', '2', '3', '4', '5', '6', '7', '8', '9', '^', '+', '-', '*' , 'x', 'X', ' ', '=']
	equation = equation.lower()
	for c in equation:
		if c not in authorized_char:
			print("Equation contained illegal characters.")
			return
	if '=' not in equation:
		print("This is not an equation.")
		return
	eq_len = len(equation)
	i = 0
	while i < eq_len:
		if equation[i] == '^' and ( i == 0 or i == eq_len -1): #exponent bad format for sure |^ or ^|
			print("Bad use of exponent operator '^'.")
			return
		if equation[i] == '^' and not (equation[i - 1] == 'x'):
			print("Missing 'x' before '^'.")
			return
		if equation[i] == '^' and not equation[i + 1].isdigit():
			print("Invalid char after '^'.")
			return
		if equation[i] == '^' and equation[i + 1] > '2':
			print("The polynomial degree is strictly greater than 2, I can't solve.")
			return
		i += 1
	
	clean_eq = equation.replace(' ', '') #remove spaces
	clean_eq_len = len(clean_eq)
	i = 0
	operands = ['*', '+', '-', '=']

	while i < clean_eq_len:
		if clean_eq[i] in operands and (i == 0 or i == clean_eq_len - 1):
			print("Bad use of operator '" + clean_eq[i] + "'")
			return
		if clean_eq[i] in operands and not (clean_eq[i - 1].isdigit() or clean_eq[i - 1] == 'x'):
			print("Invalid chars before operand '" + clean_eq[i] + "'")
			return
		if clean_eq[i] in operands and not (clean_eq[i + 1].isdigit() or clean_eq[i + 1] == 'x'):
			print("Invalid chars after operand '" + clean_eq[i] + "'")
			return
		i += 1
	


if len(sys.argv) != 2:
	sys.exit("Incorrect number of argument")
check_equation_format(sys.argv[1])


