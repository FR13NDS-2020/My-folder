# %
#.format()
name = 'Dima'
age = 21
print( 'Privet, %s!\nTebe uzhe %d god!' % (name, age) )

# %s --- placeholder stroki
# %d --- placeholder chisla
# %f --- placeholder drobi [3.4] 
print()
print('Privet, {}! \nTebe uzhe{} god!' .format( name, age ))
#tozhesamoje v figurnah skobkah mozhna vpesat indeks
print()
human = {
	'name' : 'Jesy',
	'age' : '21'
}

print('imja: {person[name]}\nvozrast: {person[age]}'.format(person = human) )



