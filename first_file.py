#Handlungsvorschrift 1:

a = int(input("Gib eine Zahl a element von N ein: "))
b = int(input("Gib eine Zahl b element von N ein: "))
if a < 0 or b < 0:
    print("Stopp, eine negative Zahl.")
    #break -> Error: outside loop
    #return -> Error: outside function
else:
    print("Weitergehen.")
    while b != 0:
        h = a % b
        a = b ; b = h
    
    print("Das Ergebnis ist" , a,".")
    print("Test: Ich verändere gerade in develop Branch")
'''        
Testfälle
1. a = -3 und b = 4 -> Stopp, eine negative Zahl. -> Programm beweist das es keine natürliche Zahl ist und wird beendet.
2. a = 5 und b = 1.3 -> ValueError: invalid literal for int() with base 10: '1.3' -> zeigt dass die Zahl eine natürliche Zahl sein muss 
3. a = 20 und b = 0 -> weitergehen. Das Ergebnis ist 20. -> Programm rechnet das Ergebnis aus.
4. a = -33 und b = -11 -> Stopp, eine negative Zahl. -> Programm beweist das es keine natürliche Zahl ist und wird beendet.
5. a = 9/7 -> ValueError: invalid literal for int() with base 10: '9/7' -> Programm bricht ab, weil eine ungültige Zahl gegeben wurde. 
'''



