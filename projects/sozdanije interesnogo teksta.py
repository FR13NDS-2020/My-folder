filename = input('Nazavite imja dokumenta? ')
platums = int(input('Vvedi sherinu? '))
input_str2 = int(input('Skolka strok sozdat? '))
fill = input('chem zapolnit? ')
lenght = platums

file = open(filename, 'a')

while 1 <= input_str2:
	input_str = input('Pechatoj: ')
	input_str2 -= 1
	file.write(('{0:'+str(fill)+'^'+str(lenght)+'}').format(input_str))
	file.write("\n")
	'''if(len (input_str) % 2):
		lenght += 1
	else:
		lenght -= 1
	moshna obratno prinjat shtob bilo po rivnu s kazhdoj storoni
	'''
	if input_str2 == 0:
		file.close()
		break


'''
Jessy*****   <
*****Jessy   >
**Jessy***   ^
'''