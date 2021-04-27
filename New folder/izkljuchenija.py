#ImportError
#IndexError
#NameError
#SyntaxError
#TypeError njesovmestimije tipi dannih
#ValueError nje to znachenije
#ZeroDivisionError
try:
	print(7 / 0) #lovit vse oshibki
except ZeroDivisionError:
	print('ZeroDivisionError')
except ImportError:
	print('ImportError')
except IndexError:
	print('IndexError')
except NameError:
	print('NameError')
except TypeError:
	print('TypeError')
except ValueError:
	print('ValueError')
finally:
	print('konjec')#eto vivedetca v ljubom sluchaje

#uznajom kokaja oshibka vivedetca pri izpolnenijji

#etimi komanda mi proverajem na SyntaxError
try:
	eval("print('21')z") #suda vpisivajem komandu dlja proverki na oshibku Syntax error
except SyntaxError:
	print('SyntaxError')




#sozdajom svoju oshibku
try:
	pogoda = 'Плохая'
	if pogoda == 'Плохая':
		raise TypeError

except TypeError:
	print('Поймано исключение TypeError')


#sozdajom svoj tip izkljuchenij

class oshibka_nahuj(Exception):
	pass

raise oshibka_nahuj('pizda vsemu kodu delaj zanivo')

print()
print('programma zavershina . . .')