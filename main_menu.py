import tkinter as tk
from buchen import open_buchen
from kassenbuch import open_kassenbuch
from provision import open_provision
from investment import open_investment


def open_main_menu():
    # Neues Fenster für das Hauptmenü erstellen
    root = tk.Tk()
    root.title("Hauptmenü")
    root.geometry("500x570")  # Größe des Hauptmenüs
    root.iconbitmap("logo.ico")
    root.configure(bg="#f6ebd9")

    def dummy_function():
        print("Button wurde geklickt!")

     # Begrüßungstext
    welcome_label = tk.Label(root, text="Willkommen im Hauptmenü", font=("Arial", 20),bg="#f6ebd9",fg="black")
    welcome_label.pack(pady=5)
                               
    # Buttons für Module
    buchen_button = tk.Button(root, text="Buchungsjournal", command=open_buchen, width=20, height=5)
    buchen_button.place(x=175, y=70)

    kassenbuch_button = tk.Button(root, text="Kassenbuch", command=open_kassenbuch, width=20, height=5)
    kassenbuch_button.place(x=100, y=170)
        
    provisionen_button = tk.Button(root, text="Provisionen", command=open_provision, width=20, height=5)
    provisionen_button.place(x=250, y=170)

    investment_button = tk.Button(root, text="Investment", command=open_investment, width=20, height=5)
    investment_button.place(x=100, y=270)
       
    statistik_button = tk.Button(root, text="Statistik", command=dummy_function, width=20, height=5)
    statistik_button.place(x=250, y=270)
        
        
    # Exit-Button
    exit_button = tk.Button(root, text="Beenden", command=root.quit, width=20, height=5)
    exit_button.place(x=175, y=470)

    # Hauptfenster starten
    root.mainloop()
    










