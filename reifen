import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime


def open_reifen():
    # Neues Fenster für die Reifenverwaltung
    root = tk.Tk()
    root.title("Reifenverwaltung")
    root.geometry("700x500")
    root.configure(bg="#f6ebd9")

    # Verbindung zur Datenbank und Abrufen der Daten
    def fetch_reifen_data():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT ID, Lagerplatz, Name, Kennzeichen, Fahrzeug, Profiltiefe, Art, Datum FROM Lagerung")
        rows = cursor.fetchall()
        conn.close()
        return rows

    # Daten in der Treeview darstellen
    def populate_treeview():
        for row in tree.get_children():
            tree.delete(row)  # Vorhandene Einträge löschen
        for index, row in enumerate(fetch_reifen_data()):
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            tree.insert("", tk.END, values=row, tags=(tag,))

    # Reifen hinzufügen
    def add_reifen():
        def submit_reifen():
            try:
                lagerplatz = lagerplatz_entry.get()
                name = name_entry.get()
                kennzeichen = kennzeichen_entry.get()
                fahrzeug = fahrzeug_entry.get()
                profiltiefe = float(profiltiefe_entry.get())
                art = art_entry.get()
                datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if not all([lagerplatz, name, kennzeichen, fahrzeug, profiltiefe, art]):
                    messagebox.showerror("Fehler", "Bitte alle Felder ausfüllen!")
                    return

                conn = sqlite3.connect("database.db")
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO Lagerung (Lagerplatz, Name, Kennzeichen, Fahrzeug, Profiltiefe, Art, Datum) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (lagerplatz, name, kennzeichen, fahrzeug, profiltiefe, art, datum),
                )
                conn.commit()
                conn.close()

                messagebox.showinfo("Erfolg", "Reifen wurde erfolgreich hinzugefügt!")
                add_window.destroy()
                populate_treeview()
            except ValueError:
                messagebox.showerror("Fehler", "Bitte eine gültige Profiltiefe eingeben!")

        add_window = tk.Toplevel(root)
        add_window.title("Reifen hinzufügen")
        add_window.geometry("400x400")
        add_window.configure(bg="#f6ebd9")

        tk.Label(add_window, text="Lagerplatz:", bg="#f6ebd9").grid(row=0, column=0, padx=10, pady=10)
        lagerplatz_entry = tk.Entry(add_window)
        lagerplatz_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Name:", bg="#f6ebd9").grid(row=1, column=0, padx=10, pady=10)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Kennzeichen:", bg="#f6ebd9").grid(row=2, column=0, padx=10, pady=10)
        kennzeichen_entry = tk.Entry(add_window)
        kennzeichen_entry.grid(row=2, column=1)

        tk.Label(add_window, text="Fahrzeug:", bg="#f6ebd9").grid(row=3, column=0, padx=10, pady=10)
        fahrzeug_entry = tk.Entry(add_window)
        fahrzeug_entry.grid(row=3, column=1)

        tk.Label(add_window, text="Profiltiefe (mm):", bg="#f6ebd9").grid(row=4, column=0, padx=10, pady=10)
        profiltiefe_entry = tk.Entry(add_window)
        profiltiefe_entry.grid(row=4, column=1)

        tk.Label(add_window, text="Art:", bg="#f6ebd9").grid(row=5, column=0, padx=10, pady=10)
        art_entry = tk.Entry(add_window)
        art_entry.grid(row=5, column=1)

        tk.Button(add_window, text="Hinzufügen", command=submit_reifen, bg="lightblue").grid(row=6, column=0, columnspan=2, pady=20)

    # Reifen bearbeiten
    def edit_reifen():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Fehler", "Bitte wähle einen Eintrag aus!")
            return

        item = tree.item(selected_item)
        values = item["values"]

        def save_changes():
            try:
                lagerplatz = lagerplatz_entry.get()
                name = name_entry.get()
                kennzeichen = kennzeichen_entry.get()
                fahrzeug = fahrzeug_entry.get()
                profiltiefe = float(profiltiefe_entry.get())
                art = art_entry.get()
                datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                conn = sqlite3.connect("database.db")
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE Lagerung SET Lagerplatz = ?, Name = ?, Kennzeichen = ?, Fahrzeug = ?, Profiltiefe = ?, Art = ?, Datum = ? WHERE ID = ?",
                    (lagerplatz, name, kennzeichen, fahrzeug, profiltiefe, art, datum, values[0]),
                )
                conn.commit()
                conn.close()

                messagebox.showinfo("Erfolg", "Eintrag wurde aktualisiert!")
                edit_window.destroy()
                populate_treeview()
            except ValueError:
                messagebox.showerror("Fehler", "Bitte eine gültige Profiltiefe eingeben!")

        edit_window = tk.Toplevel(root)
        edit_window.title("Reifen bearbeiten")
        edit_window.geometry("400x400")
        edit_window.configure(bg="#f6ebd9")

        tk.Label(edit_window, text="Lagerplatz:", bg="#f6ebd9").grid(row=0, column=0, padx=10, pady=10)
        lagerplatz_entry = tk.Entry(edit_window)
        lagerplatz_entry.grid(row=0, column=1)
        lagerplatz_entry.insert(0, values[1])

        tk.Label(edit_window, text="Name:", bg="#f6ebd9").grid(row=1, column=0, padx=10, pady=10)
        name_entry = tk.Entry(edit_window)
        name_entry.grid(row=1, column=1)
        name_entry.insert(0, values[2])

        tk.Label(edit_window, text="Kennzeichen:", bg="#f6ebd9").grid(row=2, column=0, padx=10, pady=10)
        kennzeichen_entry = tk.Entry(edit_window)
        kennzeichen_entry.grid(row=2, column=1)
        kennzeichen_entry.insert(0, values[3])

        tk.Label(edit_window, text="Fahrzeug:", bg="#f6ebd9").grid(row=3, column=0, padx=10, pady=10)
        fahrzeug_entry = tk.Entry(edit_window)
        fahrzeug_entry.grid(row=3, column=1)
        fahrzeug_entry.insert(0, values[4])

        tk.Label(edit_window, text="Profiltiefe (mm):", bg="#f6ebd9").grid(row=4, column=0, padx=10, pady=10)
        profiltiefe_entry = tk.Entry(edit_window)
        profiltiefe_entry.grid(row=4, column=1)
        profiltiefe_entry.insert(0, values[5])

        tk.Label(edit_window, text="Art:", bg="#f6ebd9").grid(row=5, column=0, padx=10, pady=10)
        art_entry = tk.Entry(edit_window)
        art_entry.grid(row=5, column=1)
        art_entry.insert(0, values[6])

        tk.Button(edit_window, text="Speichern", command=save_changes, bg="lightblue").grid(row=6, column=0, columnspan=2, pady=20)

    # Reifen löschen
    def delete_reifen():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Fehler", "Bitte wähle einen Eintrag aus!")
            return

        item = tree.item(selected_item)
        values = item["values"]

        if messagebox.askyesno("Bestätigung", f"Möchten Sie den Eintrag '{values[2]}' wirklich löschen?"):
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Lagerung WHERE ID = ?", (values[0],))
            conn.commit()
            conn.close()
            populate_treeview()

    # Treeview für die Reifenliste
    columns = ("ID", "Lagerplatz", "Name", "Kennzeichen", "Fahrzeug", "Profiltiefe", "Art", "Datum")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, anchor="center")

    tree.tag_configure("evenrow", background="lightgray")
    tree.tag_configure("oddrow", background="white")
    tree.pack(fill=tk.BOTH, expand=True)

    # Buttons
    button_frame = tk.Frame(root, bg="#f6ebd9")
    button_frame.pack(side="bottom", pady=10)

    tk.Button(button_frame, text="Hinzufügen", command=add_reifen, bg="lightblue").pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Bearbeiten", command=edit_reifen, bg="lightblue").pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Löschen", command=delete_reifen, bg="lightblue").pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Schließen", command=root.destroy, bg="lightblue").pack(side=tk.RIGHT, padx=10)

    # Daten anzeigen
    populate_treeview()

    root.mainloop()


# Starte die Anwendung
if __name__ == "__main__":
    open_reifen()
