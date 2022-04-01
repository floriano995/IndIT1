#Aufgabe: Wörterbuch DE -> EN
#Eingabe Deutscher Begriff und ausgabe des englischen wortes,
#wenn wort nicht in Wörterbuch --> entsprechende ausgabe

woerterbuch = {"apfel":"apple","birne":"pear","kirsche":"cherry","melone":"melon","marille":"apricot","pfirsich":"peach"}   #erstellung Wörterbuch als dict


eingabe = input("Eingabe des deutschen Wortes:  ")  #Eingabeaufforderung
eingabe = eingabe.lower()    #umwandlung in kleinbuchstaben


if eingabe not in woerterbuch:  #check ob in wörterbuch enthalten
    print("Wort nicht gefunden") #ausgabe
    
else:
    print("Übersetzung Englisch:   ", woerterbuch[eingabe])  #ansonsten ausgabe der übersetzung
   
'''
    neu = input("Möchten Sie dieses Wort zum Wörterbuch hinzufügen? [Y/N]  ")
    check = neu.upper()
    if check == "Y":
        neueswort_de = eingabe
        neueswort_en = input("Englische Übersetzung: ")
        
        
    else:
        print("Ok, dann vielleicht beim nächsten mal")  
        
'''    










    
    
        
        
    
    
    
    
    
        
        
