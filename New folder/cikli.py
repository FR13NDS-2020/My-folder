i = 1

while i <= 5:
	print(i)
	i = i +1
#poka i menjshe ilje ravno 5 delaj
#vivod 1 , 2 , 3 , 4 ,5

i = 1

while 1 == 1:
	print("privet, " + str(i))
	i += 1

	if i ==1000:
		break
print('gotova')

#################################

number = 0

while number <=1000:
	number +=1 #teperj number = 1 
	if (number % 2) !=0: #pri usloviji jesle number deljetca na 2 i njejevljajetca 0
		continue #vivodim cifru a jesle njet povtarjajem {continue}
	print(number)