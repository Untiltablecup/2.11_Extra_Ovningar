import math

i = float(input("Mätarställning i dag?:"))
v = float(input("Mätarställning för ett år sedan?:"))
b = float(input("Hur mång liter bensin har förbrukats?:"))

m = i - v
f = b / m

print ("")
print ("Mätarställning i dag:", i)
print ("Mätarställning ett år sedan:", v)
print ("Antal mil:", m)
print ("Antal liter bensin:", b)
print ("Förbrukning per mil:", f)
