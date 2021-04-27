def function():
	print('spam')
	print('spam')
	print('spam')
	print('spam')

function()#vizvalji svoju funkciju nazvanije mozhna vibrat ljuboje

#sozdalji svoju funkciju izpoljzuja def i nazvalji jejo function

def multiplay(number):#number et peremennaja tam mozhet bit ljuboj tekst
	print(number * 2)

multiplay(5)

def max(x, y):
	if x > y:
		return x #konstrukcija return ostanavlevajet izpolnenije funkciji
	else:
		return y
x = float(input('Chislo 1:'))
y = float(input('Chislo 2:'))
print(max(x, y))