import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def open_kassenbuch():
    # Neues Fenster für die Buchungsliste erstellen
    root = tk.Tk()
    root.title("Kassenbuch")
    root.geometry("500x500")
    root.configure(bg="#f6ebd9")

    # Verbindung zur Datenbank und Abrufen der Daten
    def fetch_data():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT ID, Datum, Betrag, Mitarbeiter, Typ FROM Kassenbuch")
        rows = cursor.fetchall()
        conn.close()
        return rows

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

    # Daten in der Treeview darstellen
    def populate_treeview():
        for row in tree.get_children():
            tree.delete(row)  # Vorhandene Einträge löschen
        for index, row in enumerate(fetch_data()):
            typ = row[4].lower()  # Typ (Einnahme, Ausgabe, etc.) aus der Zeile
            tag = None

            # Tag je nach Typ setzen
            if typ == "einnahme":
                tag = "einnahme"
            elif typ == "ausgabe":
                tag = "ausgabe"
            elif typ == "investment":
                tag = "investment"
            elif typ == "provision":
                tag = "provision"

            # Zeile einfügen und Tag anwenden
            tree.insert("", tk.END, values=row, tags=(tag,))

        # Kassenstand aktualisieren
        balance = calculate_balance()
        balance_label.config(text=f"Aktueller Kassenstand: {balance:.2f} €")

    # Eintrag bearbeiten
    def edit_entry():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Fehler", "Bitte wähle einen Eintrag aus!")
            return

        # Werte des ausgewählten Eintrags holen
        item = tree.item(selected_item)
        values = item["values"]

        # Neues Fenster für die Bearbeitung
        edit_window = tk.Toplevel(root)
        edit_window.title("Eintrag bearbeiten")
        edit_window.geometry("400x300")
        edit_window.configure(bg="#f6ebd9")

        tk.Label(edit_window, text="Datum:", bg="#f6ebd9").grid(row=0, column=0, padx=10, pady=10)
        datum_entry = tk.Entry(edit_window)
        datum_entry.grid(row=0, column=1)
        datum_entry.insert(0, values[1])

        tk.Label(edit_window, text="Betrag:", bg="#f6ebd9").grid(row=1, column=0, padx=10, pady=10)
        betrag_entry = tk.Entry(edit_window)
        betrag_entry.grid(row=1, column=1)
        betrag_entry.insert(0, values[2])

        tk.Label(edit_window, text="Mitarbeiter:", bg="#f6ebd9").grid(row=2, column=0, padx=10, pady=10)
        mitarbeiter_entry = tk.Entry(edit_window)
        mitarbeiter_entry.grid(row=2, column=1)
        mitarbeiter_entry.insert(0, values[3])

        tk.Label(edit_window, text="Typ:", bg="#f6ebd9").grid(row=3, column=0, padx=10, pady=10)
        typ_entry = tk.Entry(edit_window)
        typ_entry.grid(row=3, column=1)
        typ_entry.insert(0, values[4])

        def save_changes():
            try:
                conn = sqlite3.connect("database.db")
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE Kassenbuch SET Datum = ?, Betrag = ?, Mitarbeiter = ?, Typ = ? WHERE ID = ?",
                    (
                        datum_entry.get(),
                        float(betrag_entry.get()),
                        mitarbeiter_entry.get(),
                        typ_entry.get(),
                        values[0],  # rowid des Eintrags
                    ),
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Erfolg", "Eintrag wurde aktualisiert!")
                edit_window.destroy()
                populate_treeview()  # Aktualisiere die Treeview
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Speichern: {e}")

        # Speichern-Button
        save_button = tk.Button(edit_window, text="Speichern", command=save_changes)
        save_button.grid(row=4, column=0, columnspan=2, pady=20)

    # Treeview für die Buchungsliste
    columns = ("ID", "Datum", "Betrag", "Mitarbeiter", "Typ")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
    tree.heading("ID", text="ID")
    tree.heading("Datum", text="Datum")
    tree.heading("Betrag", text="Betrag")
    tree.heading("Mitarbeiter", text="Mitarbeiter")
    tree.heading("Typ", text="Typ")
    tree.pack(fill=tk.BOTH, expand=True)

    # Farben je nach Typ definieren
    tree.tag_configure("einnahme", background="lightgreen")
    tree.tag_configure("ausgabe", background="lightcoral")
    tree.tag_configure("investment", background="lightblue")
    tree.tag_configure("provision", background="lightsalmon")

    # Aktueller Kassenstand
    balance_label = tk.Label(root, text="Aktueller Kassenstand: 0.00 €", font=("Arial", 12), bg="#f6ebd9")
    balance_label.pack(pady=10)

    # Buttons
    tk.Button(root, text="Bearbeiten", command=edit_entry, bg="lightblue").pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(root, text="Aktualisieren", command=populate_treeview, bg="lightblue").pack(side=tk.LEFT, padx=10, pady=10)  # Neuer Button
    tk.Button(root, text="Schließen", command=root.destroy, bg="lightblue").pack(side=tk.RIGHT, padx=10, pady=10)

    # Daten anzeigen
    populate_treeview()

    root.mainloop()