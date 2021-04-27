test = None
#pustaja peremennaja

txt = {
	"kljuch1" : "znachenije1",#v kachestve kljuchej mozhet vistupat (123, 1.2, ilje stroki)
	123 : "znachenije2"#tut mozhet bit shto ugodno
}

if 123 in txt:
	print('jesc')
else:
	print('njetu')

contacts = {
	"andrej" : "+2304782374",
	"aleg" : "+32462762387",
	"losha" : "+7321490749"
}

print(contacts.get("aleg", "nomer njenajden"))