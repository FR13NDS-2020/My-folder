test = [1, 2, 3, 4, 5]

print( test[2] )
#3
test = [1,2,3]
print (test * 2)

test = 'help'

print( test[2] )
#l

test = ['alex', 'oleg', 'igotj']

if 'alex' in test: #operator in 
	print('alex is in list')

if 'ale' not in test:
	print('ale not in list')

spisok = ['aleg', 'aljosha', 'kostik']

spisok.append('aljosha') #append dobavljajet cnachenije v konjec spiska

print(spisok)

chislo = [8, 2, 3, 5, 9]
chislo.remove (2)#remove udaljajet element
chislo.insert (0, 4)#nolj eto index a 4 eto to chto mi hotim dobavit
print(chislo)
print ('v massive test u nas nahoditca ' + str(len(chislo)) + ' eljementov.' )

test1 = [1, 2, 3,1 2, 4, 1, 6, 1, 4,1, 1]

print(max(test1) )#vivodit maksimaljnoje chislo tagzhe jesc min

print(test1.count(1))#uznajom koljivhestvo elementov v spiske

test1.reverse()#eta strochka perevarachevajet spisok jevo nado tak vivodit a nje izpoljzuja print()



#len eto funkcija, len vozvrashajet chislo kaljichestvo v spiske, jego muzhna kankatenjirovat dlja vivoda
