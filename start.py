import tkinter as tk
from main_menu import open_main_menu

# Funktion für den Login-Button
def login_action():
    root.destroy()
    open_main_menu()

# Hauptfenster erstellen


root = tk.Tk()
root.title("CarosTrupp Startprogramm")
root.iconbitmap("logo.ico")
root.geometry("300x300")  # Breite x Höhe
root.configure(bg="#f6ebd9")

# Begrüßungstext in der Mitte4
welcome_label = tk.Label(
    root, 
    text="Herzlich Willkommen\nbeim CarosTrupp", 
    font=("Arial", 18, "bold"), 
    bg="#f6ebd9", 
    fg="black"
)
welcome_label.pack(pady=50)  # Abstand nach oben

# Login-Button
login_button = tk.Button(
    root, 
    text="Login", 
    font=("Arial", 14), 
    command=login_action, 
    bg="white", 
    fg="black"
)
login_button.pack()

# Hauptschleife starten
root.mainloop()