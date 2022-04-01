#Programm, das in 10° Schritten zwischen 0 und 180° den jew. Cosinus-Wert berechnet und ausgibt:

import math #import der math lib

a = 0     #Bennenung Laufvariable

while (True): #Beginn schleife für Berechnung

    winkel = a*(math.pi/180)  #umrechnung Grad in Radiant
    
    cosinus =  round(math.cos(winkel),3)  #berechnung des Cosinus und runden auf 3 Nachkommastellen
    
    print("cos(" , a , "°) = " , cosinus)  #ausgabe 
    

    a += 10 #ändern der Laufvariable

    if a == 190:
        break  #Ende der Berechnungsschleife bei a=190 weil letzte Berechnung mit a=180