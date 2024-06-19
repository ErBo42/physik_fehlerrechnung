import statistik
from fehlerfortpflanzung import fehler
from gewichteterMittelwert import mittelwert
import tkinter as tk


def open_statistik_window():
    statistik_window = tk.Toplevel(root)
    statistik_window.title("Statistik Rechner")

    entry_label = tk.Label(statistik_window, text="Enter the numbers (separated by spaces):")
    entry_label.pack()
    entry = tk.Entry(statistik_window, width=50)
    entry.pack()

    result_text = tk.StringVar()
    result_label = tk.Label(statistik_window, textvariable=result_text, justify="left")
    result_label.pack()

    calculate_button = tk.Button(statistik_window, text="Calculate", command=lambda: statistik.statistik(entry, result_text))
    calculate_button.pack()

# Main application window
root = tk.Tk()
root.title("Main Application")

open_button = tk.Button(root, text="Open Statistik Rechner", command=open_statistik_window)
open_button.pack()

root.mainloop()


# fehler()

# mittelwert()
