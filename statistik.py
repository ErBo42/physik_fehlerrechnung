import math
import tkinter as tk



def to_list():
    a = list(map(int, input("Enter the numbers : ").strip().split()))

    return a


def mittelwert(mess_list):
    num_mess = len(mess_list)
    add_mess = 0
    for i in mess_list:
        add_mess = add_mess + i
    mittel = add_mess/num_mess
    return mittel


def standardabweichung_einz(mess_list, anz_mess, mittel):
    add_mess = 0
    for i in mess_list:
        add_mess = add_mess + (i-mittel)**2
    result = math.sqrt(add_mess/(anz_mess-1))
    return result


def standardabweichung_mittel(anz_mess, stan_abw_einz):
    stan_abw_mittel = stan_abw_einz/(math.sqrt(anz_mess))
    return stan_abw_mittel

def statistik():
    mess_list = to_list()
    anz_mess = len(mess_list)
    mittel = mittelwert(mess_list)
    stan_abw_einz = standardabweichung_einz(mess_list, anz_mess, mittel)
    stan_abw_mittel = standardabweichung_mittel(anz_mess, stan_abw_einz)
    print("Messwerte:", mess_list)
    print("Mittelwert:", mittel)
    print("Standardabweichung der Einzelmessung:", stan_abw_einz)
    print("Standardabweichung des Mittelwertes:", stan_abw_mittel)


statistik()