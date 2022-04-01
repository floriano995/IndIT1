#Aufgabe Wetterabfrage


richtigeEingabe = True      #Bedingung für while Schleife
while richtigeEingabe:      #Schleife
    
    eingabe= input("Wie ist das Wetter heute? [Sonne/Regen]  ")    #Eingabeaufforderung
    var = eingabe.upper()    #Variable für Großbuchstaben
    
    if var == "SONNE":    #wenn variable 0 Sonne?
        print("Heute gibts eine Gartenparty!!")   #dann schreib das
        richtigeEingabe = False   #und beende while schleife
        
    elif var == "REGEN":  #wenn variable 0 Regen?
        print("Leider müssen wir im Keller feiern")  #dann schreib das
        richtigeEingabe = False #und beende while schleife
    else:
        print("Falsche Eingabe, nur 'Sonne' oder 'Regen' möglich")   #wenn weder noch, schreib das
        richtigeEingabe = True   #und beginne schleife von vorne
