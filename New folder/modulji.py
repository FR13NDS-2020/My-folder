#import module_name

import random
#from random import randint #importirovalji funkcijiu randint iz modulja random
#print(randint(1, 10)) #i vot tak ona vizivajetca bez kljuchegogo slova modulja
print(random.randint(1, 100)) #random eto modulj {objekt} a randint eto funkcija v njom

#for i in range(10):
#	print(random.randint(1, 100))
#generiruje randomnije chisla 10 raz

from random import * # importirovalji iz modulja random vso
#dlja togo shtob njepesat { random.randint() } a pesat tok { randint() }


from math import sqrt, pi #importiruju njeskoljka funkciji

from math import sqrt as my_sqrt # sami nazivajem funkciju po svojemu dlja izbezhanija konfliktov

