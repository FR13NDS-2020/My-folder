import random 

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int( input( 'Кол-во кодов ---> ' ) )
lenght = 16

for x in range( number ):
	password = ''

	for i in range( lenght ):
		password += random.choice( chars )

	print( password )

	file = open( 'password.txt', 'a' )
	file.write( 'https://ptb.discordapp.com/api/v6/entitlements/gift-codes/' + password + '\n')
	file.close()
# + 'https://discord.com/gifts/'
# Закрытие программы при нажатии клавиши для консоли	
import os
os.system( 'pause' )
