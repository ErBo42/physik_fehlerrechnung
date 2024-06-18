from statistik import statistik
from fehlerfortpflanzung import fehler
from gewichteterMittelwert import mittelwert
import tkinter as tk


def button_sta_clicked():
    statistik()


def button_feh_clicked():
    fehler()


def button_mittel_clicked():
    mittelwert()


root = tk.Tk()

# Creating a button with specified options
button_sta = tk.Button(root,
                   text="Statistik",
                   command=button_sta_clicked,
                   activebackground="blue",
                   activeforeground="red",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button_feh = tk.Button(root,
                   text="Fehlerfortpflanzung",
                   command=button_feh_clicked,
                   activebackground="blue",
                   activeforeground="red",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button_mittel = tk.Button(root,
                   text="Gewichteter Mittelwert",
                   command=button_mittel_clicked,
                   activebackground="blue",
                   activeforeground="red",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)


button_sta.pack(padx=20, pady=20)
button_feh.pack(padx=20, pady=20)
button_mittel.pack(padx=20, pady=20)

root.mainloop()


# statistik()

# fehler()

# mittelwert()
