import math


def summe():
    anz_var = int(input("Anzahl der Variablen:" ))
    add_fehler = 0
    for i in range(anz_var):
        fehler = float(input("Fehler: "))
        add_fehler = add_fehler + (fehler ** 2)
    result = math.sqrt(add_fehler)
    return result


def produkt():
    anz_var = int(input("Anzahl der Variablen:"))
    mul_fehler = 0
    for i in range(anz_var):
        power = float(input("Potenz: "))
        fehler = float(input("Fehler: "))
        wert = float(input("Wert: "))
        mul_fehler = mul_fehler + (power * (fehler/wert)) ** 2
    rel_fehler = math.sqrt(mul_fehler)
    return rel_fehler


