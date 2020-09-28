i = float(input("Mätarställning i dag?:")) # Läser in mätarställning idag
v = float(input("Mätarställning för ett år sedan?:")) # Läser in mätarställning för ett år sedan
b = float(input("Hur mång liter bensin har förbrukats?:")) # Läster in bensin förbruk på ett år

m = i - v # Räknar ut hur många mil som man åkt på ett år
f = b / m # Räknar ut bensin förbruk per mil

print ("Mätarställning i dag:", i) # Mätarställning i dag
print ("Mätarställning ett år sedan:", v) # Mätarställning ett år sedan
print ("Antal mil:", m) # Antal mil kört på ett år
print ("Antal liter bensin:", b) # Bensin förbrukning på ett år
print ("Förbrukning per mil:", f) # Skriver ut bensin förbrukning per mil
