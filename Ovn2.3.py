f = float(input("Hur många farenheit?:")) # Läser in farenheit och ger det till variabeln f
c=(f-32)*5/9 # Räknar ut hur många celsius det är
print (c ,"grader celsius") # Skriver ut celsius

if c >= 20:
    print ("Mans not hot")
elif c < 20:
    print ("I no go brrrrr")
else:
    print ("Temprature go brrrrr")