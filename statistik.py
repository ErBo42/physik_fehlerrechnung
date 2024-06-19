import tkinter as tk
from tkinter import messagebox
import math

def to_list(entry):
    try:
        # Convert input string to a list of integers
        a = list(map(float, entry.strip().split()))
        return a
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid list of integers separated by spaces.")
        return []

def mittelwert(mess_list):
    num_mess = len(mess_list)
    add_mess = sum(mess_list)
    mittel = add_mess / num_mess
    return mittel

def standardabweichung_einz(mess_list, anz_mess, mittel):
    add_mess = sum((i - mittel) ** 2 for i in mess_list)
    result = math.sqrt(add_mess / (anz_mess - 1))
    return result

def standardabweichung_mittel(anz_mess, stan_abw_einz):
    stan_abw_mittel = stan_abw_einz / math.sqrt(anz_mess)
    return stan_abw_mittel

def statistik(entry, result_text):
    mess_list = to_list(entry.get())
    if mess_list:
        anz_mess = len(mess_list)
        mittel = mittelwert(mess_list)
        stan_abw_einz = standardabweichung_einz(mess_list, anz_mess, mittel)
        stan_abw_mittel = standardabweichung_mittel(anz_mess, stan_abw_einz)

        result_text.set(
            f"Messwerte: {mess_list}\n"
            f"Mittelwert: {mittel}\n"
            f"Standardabweichung der Einzelmessung: {stan_abw_einz}\n"
            f"Standardabweichung des Mittelwertes: {stan_abw_mittel}"
        )
