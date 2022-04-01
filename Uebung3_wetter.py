#Aufgabe Wetterabfrage


richtigeEingabe = True
while richtigeEingabe:
    
    eingabe= input("Wie ist das Wetter heute? [Sonne/Regen]  ")
    var = eingabe.upper()
    
    if var == "SONNE":
        print("Heute gibts eine Gartenparty!!")
        richtigeEingabe = False
        
    elif var == "REGEN":
        print("Leider müssen wir im Keller feiern")
        richtigeEingabe = False
    else:
        print("Falsche Eingabe, nur 'Sonne' oder 'Regen' möglich")
        richtigeEingabe = True