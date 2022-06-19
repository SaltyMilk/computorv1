#!/Users/531-m31c/bin/python
import sys

class Term:
	def __init__(self, value, degree, sign, side): #ex 4 * 7x = 3 we're focusing on the left term here
		self.value = value       # 4*7 = 28
		self.degree = degree     # degree = 1 coz x = x^1 
		self.sign = sign		 # 1 or -1
		self.side = side		 # 'l'
		
def check_equation_format(equation):
	authorized_char = [ '0','1', '2', '3', '4', '5', '6', '7', '8', '9', '^', '+', '-', '*' , 'x', 'X', ' ', '=', '.']
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
 
	clean_eq = equation #remove spaces
	clean_eq_len = len(clean_eq)
	i = 0
	operands = ['*', '+', '-', '=', '.']

	while i < clean_eq_len:
		if (i == 0 and (clean_eq[i] == '+' or clean_eq[i] == '-')):
			i += 1
			continue
		if clean_eq[i] in operands and (i == 0 or i == clean_eq_len - 1):
			print("Bad use of operator '" + clean_eq[i] + "'")
			return
		if clean_eq[i] in operands and not (clean_eq[i - 1].isdigit() or (clean_eq[i - 1] == 'x' and clean_eq[i] != '.')):
			print("Invalid chars before operand '" + clean_eq[i] + "'")
			return
		if clean_eq[i] in operands and not (clean_eq[i + 1].isdigit() or (clean_eq[i + 1] == 'x' and clean_eq[i] != '.')):
			print("Invalid chars after operand '" + clean_eq[i] + "'")
			return
		
		i += 1

def parse_terms_strings(side):
	terms = []
	tmp_s = ""

	i = 0	
	for c in side: #parse left side, we're basically splitting on '+' or '-' and keeping the signs
		if (i == 0):
			i += 1
			tmp_s += c
			continue
		elif c == '+' or c == '-':
			terms.append(tmp_s)
			tmp_s = ""
		tmp_s += c

	terms.append(tmp_s)
	return terms

def strs_to_term(strs, side):
	sp = strs.split("*")
	len_sp = len(sp)
	if len_sp > 2:													# ... + 4 * 2x * 4x + ...
		sys.exit("Excessive multiplication, not polynomial form.")
	if len_sp == 2 and ('x' not in sp[0] and 'x' not in sp[1]):		# ... + 7 * 4 + ...
		sys.exit("Excessive multiplication, not polynomial form.")

	term = Term(0, 0, 0, side)

	if len_sp == 2:
		i = 0
		for c in sp['x' in sp[1]]:
			if c == 'x' and sp['x' in sp[1]][i + 1] != '^':
				term.degree = 1
				break
			elif c == '^':
				term.degree = int(sp['x' in sp[1]][i + 1])
				break
			i += 1
		term.value = float(sp[not 'x' in sp[1]])
		term.sign = 1
		if term.value < 0:
			term.sign = -1
			term.value *= -1
	else:
		if 'x' in sp[0]:
			i = 0
			for c in sp[0]:
				if c == 'x' and sp[0][i + 1] != '^':
					term.degree = 1
					break
				elif c == '^':
					term.degree = int(sp[0][i + 1])
					break
				i += 1
			term.value = 1
			term.sign = 1
			if sp[0][0] == '-':
				term.sign = -1
		else:
			term.value = float(sp[0])
			term.sign = 1
			if term.value < 0:
				term.sign = -1
				term.value *= -1
	return term

# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
def parse_eq(eq):
	sides = eq.split('=')
	
	left_s = parse_terms_strings(sides[0])
	right_s = parse_terms_strings(sides[1])
	print(left_s + right_s)
	

	termlst = []
	for t in left_s:
		termlst.append(strs_to_term(t, 'l'))
	for t in right_s:
		termlst.append(strs_to_term(t, 'r'))

	for x in termlst:
		print(vars(x))


if len(sys.argv) != 2:
	sys.exit("Incorrect number of argument")

eqx = sys.argv[1].lower()
eqx = eqx.replace(" ", "")
print(eqx)
check_equation_format(eqx)
parse_eq(eqx)
