pogoda = 'kapajet'
time = 'temno'

if pogoda == 'kapajet' and (time 'temno' or time == 'vecher') :#mozhem vso jeto v kruglije skobki dlja udobstva
	print("sidi doma") # {and} i jevljajetca uslovnim operatorim tagzhe jesc {or} ilje
#eto Множественные условия 

#tagzhe jesc {not} 
if not pogoda == 'kapajet' :
	print('chtoto')

### приоритетность операторов

() #dlja ckobok samij visoki preoritet 
** #potom jeto
* / #daljshe jeto
+ - #potom et 
# i takdaleje
