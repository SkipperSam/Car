import tkinter as tk
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

# Funktion zum Abrufen der Mitarbeiter-Namen aus der Datenbank
def get_mitarbeiter_names():
    # Verbindung zur Datenbank herstellen
    mitarbeiter_connect = sqlite3.connect("database.db")
    mitarbeiter_cursor = cursor = mitarbeiter_connect.cursor()
    # Abfrage: Alle Namen aus der Tabelle "Kategorien" abrufen
    mitarbeiter_cursor.execute("SELECT Name FROM Mitarbeiter")
    mitarbeiter_names = [row[0] for row in cursor.fetchall()]  # Extrahiere die Namen aus den Ergebnissen
    # Verbindung schließen
    mitarbeiter_connect.close()
    return mitarbeiter_names

# Funktion zum Abrufen der Kategorien-Namen aus der Datenbank
def get_kategorie_names():
    # Verbindung zur Datenbank herstellen
    kategorie_connect = sqlite3.connect("database.db")
    kategorie_cursor = cursor = kategorie_connect.cursor()
    # Abfrage: Alle Namen aus der Tabelle "Mitarbeiter" abrufen
    kategorie_cursor.execute("SELECT Name FROM Kategorien")
    kategorie_names = [row[0] for row in cursor.fetchall()]  # Extrahiere die Namen aus den Ergebnissen
    # Verbindung schließen
    kategorie_connect.close()
    return kategorie_names

# Funktion zum Abrufen der Typ-Namen aus der Datenbank
def get_typ_names():
    # Verbindung zur Datenbank herstellen
    typ_connect = sqlite3.connect("database.db")
    typ_cursor = cursor = typ_connect.cursor()
    # Abfrage: Alle Namen aus der Tabelle "Mitarbeiter" abrufen
    typ_cursor.execute("SELECT Name FROM Typ")
    typ_names = [row[0] for row in cursor.fetchall()]  # Extrahiere die Namen aus den Ergebnissen
    # Verbindung schließen
    typ_connect.close()
    return typ_names



def open_buchen():
     # Neues Fenster für das Hauptmenü erstellen
    root = tk.Tk()
    root.title("Buchungsjournal")
    root.geometry("400x570")  # Größe des Hauptmenüs
    root.iconbitmap("logo.ico")
    root.configure(bg="#f6ebd9")



    def close_window():
        root.destroy()


        # Daten aus der Datenbank abrufen und zuordnen
    mitarbeiter_options = get_mitarbeiter_names()
    kategorie_options   = get_kategorie_names()
    typ_options         = get_typ_names()

    # Überschrift
    title_label = tk.Label(root, text="Buchungsjournal", font=("Arial", 20),bg="#f6ebd9",fg="black")
    title_label.pack(pady=5,)

    # Eingabefeld für den Betrag
    betrag_label = tk.Label(root, text="Betrag (€):", font=("Arial",12), fg="black" )
    betrag_label.pack()
    betrag_entry = tk.Entry(root)
    betrag_entry.pack()

    luft1_label = tk.Label(root, text="Platzhalter", font=("Arial",8), fg="#f6ebd9", bg="#f6ebd9",)
    luft1_label.pack()

    # Auswahl der Mitarbeiter
    def set_name_sam():
        mitarbeiter_var.set("Sam")
        sam_button.configure(bg="lightgreen")
        simon_button.configure(bg="lightgrey")
        shawn_button.configure(bg="lightgrey")
        luke_button.configure(bg="lightgrey")
        Moritz_button.configure(bg="lightgrey")
    def set_name_simon():
        mitarbeiter_var.set("Simon")
        sam_button.configure(bg="lightgrey")
        simon_button.configure(bg="lightgreen")
        shawn_button.configure(bg="lightgrey")
        luke_button.configure(bg="lightgrey")
        Moritz_button.configure(bg="lightgrey")
    def set_name_shawn():
        mitarbeiter_var.set("Shawn")
        sam_button.configure(bg="lightgrey")
        simon_button.configure(bg="lightgrey")
        shawn_button.configure(bg="lightgreen")
        luke_button.configure(bg="lightgrey")
        Moritz_button.configure(bg="lightgrey")
    def set_name_luke():
        mitarbeiter_var.set("Luke")
        sam_button.configure(bg="lightgrey")
        simon_button.configure(bg="lightgrey")
        shawn_button.configure(bg="lightgrey")
        luke_button.configure(bg="lightgreen")
        Moritz_button.configure(bg="lightgrey")
    def set_name_moritz():
        mitarbeiter_var.set("Moritz")
        sam_button.configure(bg="lightgrey")
        simon_button.configure(bg="lightgrey")
        shawn_button.configure(bg="lightgrey")
        luke_button.configure(bg="lightgrey")
        Moritz_button.configure(bg="lightgreen")


    tk.Label(root, text="Mitarbeiter auswählen", font=("Arial",12), fg="black").pack()
    mitarbeiter_var = tk.StringVar()
    button_frame = tk.Frame(root)
    button_frame.pack()
    sam_button = tk.Button(button_frame, text="Sam", command=set_name_sam, bg="lightgrey")
    sam_button.grid(row=0, column=0, padx=2)
    simon_button = tk.Button(button_frame, text="Simon", command=set_name_simon, bg="lightgrey")
    simon_button.grid(row=0, column=1, padx=2)
    shawn_button = tk.Button(button_frame, text="Shawn", command=set_name_shawn, bg="lightgrey")
    shawn_button.grid(row=0, column=2, padx=2)
    luke_button = tk.Button(button_frame, text="Luke", command=set_name_luke, bg="lightgrey")
    luke_button.grid(row=0, column=3, padx=2)
    Moritz_button = tk.Button(button_frame, text="Moritz", command=set_name_moritz, bg="lightgrey")
    Moritz_button.grid(row=0, column=4, padx=2)
    
    luft2_label = tk.Label(root, text="Platzhalter", font=("Arial",8), fg="#f6ebd9", bg="#f6ebd9",)
    luft2_label.pack()

    # Auswahl des Types
    def set_typ_Ausgabe():
        typ_var.set("Ausgabe")
        ausgabe_button.configure(bg="lightgreen")
        einnahme_button.configure(bg="lightgrey")
    def set_typ_einnahme():
        typ_var.set("Einnahme")
        ausgabe_button.configure(bg="lightgrey")
        einnahme_button.configure(bg="lightgreen")
    
    tk.Label(root, text="Typ auswählen", font=("Arial",12), fg="black").pack()
    typ_var = tk.StringVar()
    button_frame2 = tk.Frame(root)
    button_frame2.pack()
    ausgabe_button = tk.Button(button_frame2, text="Ausgabe", command=set_typ_Ausgabe, bg="lightgrey")
    ausgabe_button.grid(row=0, column=0, padx=2)
    einnahme_button = tk.Button(button_frame2, text="Einnahme", command=set_typ_einnahme, bg="lightgrey")
    einnahme_button.grid(row=0, column=1, padx=2)

    
    luft3_label = tk.Label(root, text="Platzhalter", font=("Arial",8), fg="#f6ebd9", bg="#f6ebd9",)
    luft3_label.pack()





    # Daten werden in Kassenbuch geschrieben
    def save_in_kassenbuch():
        Betrag = betrag_entry.get()
        Mitarbeiter = mitarbeiter_var.get()
        Typ = typ_var.get()

        print(f"Betrag: {Betrag}, Mitarbeiter: {Mitarbeiter}, Typ: {Typ}")

        if not Betrag or Mitarbeiter == "Mitarbeiter auswählen" or Typ == "Typ auswählen":
            messagebox.showerror("Fehler!", "Bitte fülle alle Felder aus!")
            return
        try:
            betrag = float(Betrag)
            if betrag < 1:
                messagebox.showerror("Fehler!", "Bitte einen Betrag größer als 0 eingeben!")
                return
        except ValueError:
            messagebox.showerror("Fehler!", "Bitte einen gültigen Betrag eingeben!")
            return
    
        Datum = datetime.now().strftime("%d-%m-%Y %H:%M")

        print("Daten, die eingefügt werden sollen:")
        print(f"Datum: {Datum}, Betrag: {betrag}, Mitarbeiter: {Mitarbeiter}, Typ: {Typ}")

        kassenbuch_connect = sqlite3.connect("database.db")
        kassenbuch_cursor  = kassenbuch_connect.cursor()
        kassenbuch_cursor.execute('''INSERT INTO Kassenbuch (Datum, Betrag, Mitarbeiter, Typ) VALUES (?, ?, ?, ?)''', (Datum, betrag, Mitarbeiter, Typ))
        kassenbuch_connect.commit()
        kassenbuch_connect.close()
        messagebox.showinfo("Information", "Buchung erfolgreich durchgeführt")
        close_window()
 
    # Button um Buchung zu speichern
    buchen_button = tk.Button(root, text="Buchen", command=save_in_kassenbuch)
    buchen_button.pack()

    luft5_label = tk.Label(root, text="Platzhalter", font=("Arial",15), fg="#f6ebd9", bg="#f6ebd9",)
    luft5_label.pack()
    
    # Button zum Schließen des Buchungsjournal
    end_button = tk.Button(root, text="Schließen", command=close_window)
    end_button.pack()


    root.mainloop()

