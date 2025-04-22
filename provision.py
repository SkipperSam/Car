import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def open_provision():
    # Neues Fenster für Provisionen
    root = tk.Toplevel()
    root.title("Provisionen")
    root.geometry("515x250")
    root.configure(bg="#f6ebd9")

    # Verbindung zur Datenbank und Abrufen der Mitarbeiter und Provisionen
    def fetch_provision_data():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Mitarbeiter und ihren Provisionssatz abrufen
        cursor.execute("SELECT Name, Provisionssatz FROM Mitarbeiter")
        mitarbeiter = cursor.fetchall()

        # Berechnung der jeweiligen Provisionen
        provisionen = []
        for name, satz in mitarbeiter:
            cursor.execute(
                "SELECT SUM(Betrag) FROM Kassenbuch WHERE Mitarbeiter = ? AND Typ = 'Einnahme'",
                (name,),
            )
            summe_einnahmen = cursor.fetchone()[0] or 0
            provision = summe_einnahmen * (satz / 100)
            provisionen.append((name, provision))

        conn.close()
        return provisionen

     # Kassenstand berechnen
    def calculate_balance():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Betrag, Typ FROM Kassenbuch")
        rows = cursor.fetchall()
        conn.close()

        balance = 0
        for betrag, typ in rows:
            if typ.lower() == "einnahme":
                balance += betrag  # Positive Beträge
            elif typ.lower() == "ausgabe":
                balance -= betrag  # Negative Beträge
            elif typ.lower() == "investment":
                balance += betrag  # Investment als positiv
            elif typ.lower() == "provision":
                balance -= betrag  # Provision als negativ
        return balance

    # Funktion zum Auszahlen der Provision
    def auszahlen(name, provision):
        current_balance = calculate_balance  # Aktuellen Kassenstand abrufen
        if provision == 0:
            messagebox.showwarning(
                "Warnung", f"Die Provision für {name} beträgt 0.00 €. Auszahlung nicht möglich."
            )
            return

        if messagebox.askyesno(
            "Bestätigung",
            f"Soll die Provision von {provision:.2f} € für {name} ausgezahlt werden?",
        ):
            try:
                conn = sqlite3.connect("database.db")
                cursor = conn.cursor()

                # Eintrag in Kassenbuch hinzufügen
                cursor.execute(
                    "INSERT INTO Kassenbuch (Datum, Betrag, Mitarbeiter, Typ) VALUES (DATE('now'), ?, ?, 'Provision')",
                    (provision, name),
                )

                # Eintrag in Provision hinzufügen
                cursor.execute(
                    "INSERT INTO Provisionen (Datum, Betrag, Mitarbeiter) VALUES (DATE('now'), ?, ?)",
                    (provision, name),
                )

                conn.commit()

                # Erfolgsmeldung
                messagebox.showinfo(
                    "Erfolg", f"Die Provision von {provision:.2f} € wurde an {name} ausgezahlt!"
                )

                # Provision auf 0 setzen
                provision = provision - provision

                populate_table()  # Tabelle aktualisieren
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Auszahlen der Provision: {e}")
            finally:
                conn.close()

    # Tabelle mit den Provisionen
    def populate_table():
        for widget in frame.winfo_children():
            widget.destroy()

        provisionen = fetch_provision_data()

        # Kassenstand aktualisieren
        calculate_balance()

        # Header
        tk.Label(frame, text="Name", bg="#f6ebd9", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(frame, text="Provision (€)", bg="#f6ebd9", font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame, text="Aktion", bg="#f6ebd9", font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=5)

        # Daten
        for index, (name, provision) in enumerate(provisionen):
            tk.Label(frame, text=name, bg="#f6ebd9", font=("Arial", 10)).grid(row=index + 1, column=0, padx=10, pady=5)
            tk.Label(
                frame,
                text=f"{provision:.2f} €",
                bg="white",
                font=("Arial", 10),
                relief="solid",
                width=15,
            ).grid(row=index + 1, column=1, padx=10, pady=5)

            # Auszahlen-Button
            tk.Button(
                frame,
                text="Auszahlen",
                bg="red",
                fg="white",
                font=("Arial", 10),
                command=lambda n=name, p=provision: auszahlen(n, p),
            ).grid(row=index + 1, column=2, padx=10, pady=5)

    # Scrollbarer Frame
    canvas = tk.Canvas(root, bg="#f6ebd9")
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f6ebd9")

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    frame = scrollable_frame

    # Tabelle initialisieren
    populate_table()

    # Buttons für Aktualisieren und Schließen links unterhalb positionieren
    button_frame = tk.Frame(root, bg="#f6ebd9")
    button_frame.pack(side="bottom", pady=10)

    tk.Button(
        button_frame,
        text="Aktualisieren",
        bg="lightblue",
        font=("Arial", 12),
        command=populate_table,  # Aktualisiert die Tabelle
    ).pack(padx=5)

    tk.Button(
        button_frame,
        text="Schließen",
        bg="lightblue",
        font=("Arial", 12),
        command=root.destroy,  # Schließt das Fenster
    ).pack(padx=5)

    root.mainloop()
