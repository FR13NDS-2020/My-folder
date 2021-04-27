#def fub(text):
#	assert text != ''	
#	print(str(text) + '?')

#fub('darova')

#def test(number):
#	assert number > 0, "number should be bigger than 0"
#	print(str(number))

#test(-10)

#vijevljajem oshibki
################################################

#cho kasajetca failov?
filename = input('Ukazhite fail?: ')

file = open('text.txt', 'r')

print( 'v dannom faile ' + str(len(file.read())) + ' simvol' )
file.close()

#################################################
#r - chtenije faila
file = open('text.txt', 'r')
print(file.read())
file.close()
#w - dlja perezapisi faila
file = open('text.txt', 'w')
file.write('darou')
file.close()
#a - dlja dobovlenija v fail
file = open('text.txt', 'a')
file.write( 'darou' )
file.close()
#b - binary mode



#progeamma dlja kopirovanija failov
filename1 = input('kokoj fail zabekapitc?:')
filename = 'backup ' + filename1

file1 = open(filename1, 'rb')
file2 = open(filename2, 'wb')

file2.write(file1.read())

file1.close()
file2.close()

print('bekup zavershon!')

#############################
#chtenije postrochna
file = open('text.txt', 'r' )

strings = file.readlines()

for string in strings:
	print(string)

file.close()

#eto komanda pozvoljajet nje zakrivat fail samomu
with open('text.txt', 'r' ) as f:
	print(f.read(5))
