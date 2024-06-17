import math


def mittelwert():
    anz_var = int(input("Anzahl Messwerte: "))
    zaehler = 0
    nenner = 0
    for i in range(anz_var):
        fehler = float(input("Fehler: "))
        wert = float(input("Wert: "))
        nenner = nenner + (1 / (fehler ** 2))
        zaehler = zaehler + ((1 / (fehler ** 2)) * wert)
    result = zaehler/nenner
    result_fehler = 1 / (math.sqrt(nenner))
    print(result, "\u00B1", result_fehler)


