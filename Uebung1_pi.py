from math import pi  #Nur für Kontrolle


print("Berechnung von Pi mit der Leibnitz Reihe:")

while True:           #Schleife für Eingabe Kontrolle
    eingabe = input("Wie oft soll die Reihe Wiederholt werden? [Eingabe Natürlicher Zahl]:    ")   #eingabaufforderung
    try:              #Eingabecheck
        x = int(eingabe)     #Umwandeln in Integer, wenn möglich
        if x <= 0:           #Überprüfen ob Integer positiv
            raise ValueError #Wenn negativ, springe zu Fehler
        break;               #Ende der Schleife, wenn Natürliche Zahl
    except ValueError:       #Fehler ausgabe
        try:                 #Prüfe ob Float
            float(eingabe)            
            print("Bitte nur Natürliche Zahlen ", eingabe)
        except ValueError:   #Prüfe ob String
            print("Falsche Eingabe, bitte eine Zahl eingeben")


summe = 0  #Variable für Reihen Summe
a = 0    #Variable für Berechnung
n = 0    #Variable für Laufvariable

while True: #While Schleife
    a=float(((-1)**n)/(2*n+1))   #Berechnung
    summe += a          #"Summenzeichen" wird erste am ende ausgegeben
    n += 1              #Laufvariable erhöhen
   
    if n==x:            #While Stopper für Eingabe
        break

ergebnis = summe * 4    # Ausgabe von Leibnitz ist Pi/4 

print('Berechnetes Pi:',ergebnis) #Ausgabe Ergebnis
print('Vergleich mit Import:', pi) #Ausgabe Vergleich
