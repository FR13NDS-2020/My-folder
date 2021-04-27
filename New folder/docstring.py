def tekst(name):
	''' opisanije funkciji idjot obizateljno pervoj'''
	print('zdraste ' + name())

#print(tekst.__doc__)#vivelji opisanije funkciji

#tekst1 = tekst
#tekst1()
#vot tak mi mozhem sdelat shob vizvat svoju funkciju pod drugim nazvanijem

def imja():
	return input('vvedite vashe imja: ')

tekst(imja)

#delajesh funkciju argumentom drugoj funkciji