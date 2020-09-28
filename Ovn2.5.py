import math # Importerar modulen math

x1 = float(input("Kordinat för X1?:")) # Läser in kordinaterna för x1
x2 = float(input("Kordinat för X2?:")) # Läser in kordinaterna för x2
y1 = float(input("Kordinat för Y1?:")) # Läser in kordinaterna för y1
y2 = float(input("Kordinat för Y2?:")) # Läser in kordinaterna för y2

s = (x1-x2)**2 + (y1-y2)**2 # Räknar ut talet innan roten ur
o = math.sqrt(s) # Räknar roten ur s

print (o, "cm") # Skriver ut avståndet i cm