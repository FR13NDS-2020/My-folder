#debiljnij kaljkuljator
from colorama import Fore, Back, Style
from colorama import init
init()
print(Fore.BLACK)
print(Back.GREEN)

what = input("chto delajem? (+, -):" )
print(Back.CYAN)
a = float(input("vvedi pervoje chislo: "))
b = float(input("vvedi vtoroje chislo: "))
print(Back.RED)
if what == "+":
    c = a + b
    print("Rezuljtat: " + str(c))
elif what == "-":
    c = a - b
    print("Rezuljatat: " + str(c))
else:
    print("vibrana njevernaja operacija!")
input()