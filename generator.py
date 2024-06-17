from tkinter import *
import random
import string
from tkinter import messagebox

password_history = []
history_window = None  # Fenêtre de l'historique
history_text = None  # Widget de texte pour afficher l'historique




root = Tk()

def toggle_password():
    if passwordEntry.cget('show') == '':
        passwordEntry.config(show='*')
    else:
        passwordEntry.config(show='')

def generate():

  all_chars = ""

  if uppercase_var.get():
    all_chars += string.ascii_uppercase
  if lowercase_var.get():
    all_chars += string.ascii_lowercase
  if digits_var.get():
    all_chars += string.digits
  if punctuation_var.get():
    all_chars += string.punctuation

  while True:
    password_length = int(scale.get())
    password = "".join(random.choice(all_chars) for _ in range(password_length))

    if password not in reversed(password_history):
      password_history.insert(0, password)  # Insère le nouveau mot de passe au début de l'historique
      break


  passwordEntry.delete(0, END)
  passwordEntry.insert(0, password)

  update_history_text()

def update_history_text():
    if history_text:
        history_text.config(state=NORMAL)  # Permet de modifier le contenu du widget de texte
        history_text.delete(1.0, END)  # Efface le contenu actuel

        # Ajoute les mots de passe à l'historique dans le widget de texte
        for password in password_history:
            history_text.insert(END, password + "\n")

        history_text.config(state=DISABLED)

def history():
  global history_window, history_text

    # Crée ou actualise la fenêtre de l'historique
  if history_window is None:
    history_window = Toplevel(root)
    history_window.title("History")
    history_text = Text(history_window, height=10, width=40, font=("Arial", 14), bg='#009AFF', fg='white')
    history_text.pack()

    history_window.protocol("WM_DELETE_WINDOW", on_history_close)  # Appel on_history_close() lorsque l'utilisateur ferme la fenêtre de l'historique

    # Actualise le contenu du widget de texte
  update_history_text()


def on_history_close():
    global history_window
    if history_window:
        # Vérifie si history_window est différent de None avant d'appeler destroy()
        history_window.destroy()
        history_window = None

def copy():
  root.clipboard_clear()
  root.clipboard_append(passwordEntry.get())

def check_password_length():
  password = passwordEntry.get()
  length = len(password)
  if length < 12:
    messagebox.showwarning("Attention", "Votre mot de passe est trop court.")
  elif length > 23:
    messagebox.showwarning("Attention", "Votre mot de passe est trop long.")
  else:
    messagebox.showinfo("Succès", "La longueur de votre mot de passe est appropriée.")

frameTitle = Frame(root, bg='#009AFF')
frameTitle.pack(side=TOP, expand=YES)

frameButton = Frame(root, bg='#009AFF')
frameButton.pack(side=BOTTOM, expand=YES)

root.title("Password Generator")
root.geometry("700x700")
root.minsize(700,700)
root.config(background='#009AFF')

labelTitle = Label(frameTitle, text="Bienvenue sur Password Generator", font=("Arial", 40), bg='#009AFF', fg='white')
labelTitle.pack(side=TOP, expand=YES)

labelSubtitle = Label(frameTitle, text="Générez un mot de passe sécurisé à l'aide de notre générateur !", font=("Arial", 20), bg='#009AFF', fg='white')
labelSubtitle.pack(side=TOP, expand=YES)

passwordEntry = Entry(frameButton, font=("Arial", 15), bg='#009AFF', fg='white')
passwordEntry.grid(row=0, column=0, pady=10, padx=10, sticky=W)

scale = Scale(frameButton, from_=8, to=24, orient=HORIZONTAL, label="Chars Number", font=("Arial", 14), bg='#009AFF', fg='white')
scale.set(8) 
scale.grid(row=1, column=0, padx=10, pady= 20, sticky=W)

uppercase_var = IntVar()
uppercase_check = Checkbutton(frameButton, text="Majuscules", variable=uppercase_var, font=("Arial", 14), bg='#009AFF', fg='white')
uppercase_check.grid(row=2, column=0, sticky=W)

lowercase_var = IntVar()
lowercase_check = Checkbutton(frameButton, text="Minuscules", variable=lowercase_var, font=("Arial", 14), bg='#009AFF', fg='white')
lowercase_check.grid(row=2, column=1, sticky=W)

digits_var = IntVar()
digits_check = Checkbutton(frameButton, text="Chiffres", variable=digits_var, font=("Arial", 14), bg='#009AFF', fg='white')
digits_check.grid(row=4, column=0, sticky=W)

punctuation_var = IntVar()
punctuation_check = Checkbutton(frameButton, text="Caractères spéciaux", variable=punctuation_var, font=("Arial", 14), bg='#009AFF', fg='white')
punctuation_check.grid(row=4, column=1, sticky=W)

startButton = Button(frameButton, text="Generate", font=("Arial", 20), bg='#009AFF', fg='blue', command=generate)
startButton.grid(row=6, column=0, pady=50, padx=10, sticky=W)

historyButton = Button(frameButton, text="Historique", font=("Arial", 20), bg='#009AFF', fg='blue', command=history)
historyButton.grid(row=6, column=1, pady=50, padx=10, sticky=W)


copyButton = Button(frameButton, text="Copier", font=("Arial", 20), bg='#009AFF', fg='blue', command=copy)
copyButton.grid(row=0, column=1, pady=10, padx=10, sticky=W)

toggleButton = Button(frameButton, text="Afficher/Masquer", bg='#009AFF', fg='blue', command=toggle_password)
toggleButton.grid(row=0, column=3, pady=10, padx=10, sticky=W)

frameTitle.pack(expand=YES)
frameButton.pack(expand=YES)

checkButton = Button(frameButton, text="Vérifier la longueur", command=check_password_length)
checkButton.grid(row=7, column=0, pady=10, padx=10, sticky=W)

root.mainloop()