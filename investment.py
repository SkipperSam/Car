import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def open_investment():
    # Neues Fenster für Investments
    root = tk.Toplevel()
    root.title("Investments")
    root.geometry("515x350")
    root.configure(bg="#f6ebd9")

    # Verbindung zur Datenbank und Abrufen der Mitarbeiter und Investments
    def fetch_investment_data():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Mitarbeiter und ihre Gesamtinvestitionen abrufen
        cursor.execute("SELECT Name FROM Mitarbeiter")
        mitarbeiter = cursor.fetchall()

        # Berechnung der jeweiligen Investments
        investments = []
        for (name,) in mitarbeiter:
            cursor.execute(
                "SELECT SUM(Betrag) FROM Investments WHERE Mitarbeiter = ?",
                (name,),
            )
            total_investment = cursor.fetchone()[0] or 0
            investments.append((name, total_investment))

        conn.close()
        return investments


    # Funktion zum Hinzufügen eines Investments
    def add_investment(name, amount, reason):
       
        if amount <= 0:
            messagebox.showwarning(
                "Warnung", "Der Betrag muss größer als 0 sein."
            )
            return
        if not reason or not amount:
            messagebox.showwarning("Warnng", "Bitte alle Felder ausfüllen.")
            return
        
        if messagebox.askyesno(
            "Bestätigung",
            f"Soll ein Investment von {amount:.2f} € für {name} mit dem Grund '{reason}' hinzugefügt werden?",
        ):
            try:
                conn = sqlite3.connect("database.db")
                cursor = conn.cursor()

                # Eintrag in Kassenbuch hinzufügen
                cursor.execute(
                    "INSERT INTO Kassenbuch (Datum, Betrag, Mitarbeiter, Typ) VALUES (DATE('now'), ?, ?, 'Investment')",
                    (amount, name),
                )

                # Eintrag in Investments hinzufügen
                cursor.execute(
                    "INSERT INTO Investments (Datum, Betrag, Mitarbeiter, Grund) VALUES (DATE('now'), ?, ?, ?)",
                    (amount, name, reason),
                )

                conn.commit()

                # Erfolgsmeldung
                messagebox.showinfo(
                    "Erfolg", f"Ein Investment von {amount:.2f} € wurde für {name} mit dem Grund '{reason}' hinzugefügt!"
                )

                populate_table()  # Tabelle aktualisieren
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Hinzufügen des Investments: {e}")
            finally:
                conn.close()

    # Tabelle mit den Investments
    def populate_table():
        for widget in frame.winfo_children():
            widget.destroy()

        investments = fetch_investment_data()

        # Header
        tk.Label(frame, text="Name", bg="#f6ebd9", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(frame, text="Investment (€)", bg="#f6ebd9", font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame, text="Aktion", bg="#f6ebd9", font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=5)

        # Daten
        for index, (name, investment) in enumerate(investments):
            tk.Label(frame, text=name, bg="#f6ebd9", font=("Arial", 10)).grid(row=index + 1, column=0, padx=10, pady=5)
            tk.Label(
                frame,
                text=f"{investment:.2f} €",
                bg="white",
                font=("Arial", 10),
                relief="solid",
                width=15,
            ).grid(row=index + 1, column=1, padx=10, pady=5)

            # Investment-Button
            tk.Button(
                frame,
                text="Investieren",
                bg="green",
                fg="white",
                font=("Arial", 10),
                command=lambda n=name: ask_investment(n),
            ).grid(row=index + 1, column=2, padx=10, pady=5)

    # Eingabedialog für Investment
    def ask_investment(name):
        def submit_investment():
            try:
                amount = float(amount_entry.get())
                reason = reason_entry.get()
                add_investment(name, amount, reason)
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Fehler", "Bitte geben Sie eine gültige Zahl ein.")

        dialog = tk.Toplevel(root)
        dialog.title("Investment hinzufügen")
        dialog.geometry("300x200")
        dialog.configure(bg="#f6ebd9")

        tk.Label(dialog, text=f"Investment für {name}:", bg="#f6ebd9", font=("Arial", 12)).pack(pady=10)
        amount_entry = tk.Entry(dialog, font=("Arial", 12))
        amount_entry.pack(pady=5)

        tk.Label(dialog, text="Grund:", bg="#f6ebd9", font=("Arial", 12)).pack(pady=10)
        reason_entry = tk.Entry(dialog, font=("Arial", 12))
        reason_entry.pack(pady=5)

        tk.Button(dialog, text="Bestätigen", bg="lightblue", font=("Arial", 12), command=submit_investment).pack(pady=5)

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

    # Buttons für Aktualisieren und Schließen
    button_frame = tk.Frame(root, bg="#f6ebd9")
    button_frame.pack(side="bottom", pady=10)

    tk.Button(
        button_frame,
        text="Aktualisieren",
        bg="lightblue",
        font=("Arial", 12),
        command=populate_table,
    ).pack(padx=5)

    tk.Button(
        button_frame,
        text="Schließen",
        bg="lightblue",
        font=("Arial", 12),
        command=root.destroy,
    ).pack(padx=5)

    root.mainloop()