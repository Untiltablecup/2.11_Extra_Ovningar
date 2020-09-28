import math # importerar modulen math

r = float(input("Vad är sfärens radie?: ")) # Frågar om radien, man får sedan skriva in vad radien är

v = 4 * math.pi * r ** 3 / 3 # Räknar ut volymen på sfären med hjälp av radien

a = 4 * math.pi * r ** 2  # Räknar ut arean på sfären med hjälp av radien

print ("Sfärens area är:", a, "Sfärens volym är:", v) # Skriv ut arean och volymen