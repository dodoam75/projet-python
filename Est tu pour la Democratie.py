import tkinter as tk
import random



def bouton1_click():
    label.config(text="\n\n\n\nPOUR\n LA\n DEMOCRATIE\n", font=("Arial", 30), justify='center')
    bouton1.destroy()
    bouton2.destroy()

clics_bouton2 = 0
def bouton2_click():
    label.config(text="Est tu pour la democratie ?")
    x = random.randint(0, fenetre.winfo_width() - bouton2.winfo_width())
    y = random.randint(0, fenetre.winfo_height() - bouton2.winfo_height())
    bouton2.place(x=x, y=y)
    global clics_bouton2
    clics_bouton2 += 1
    if clics_bouton2 > 10:
        label.config(text="Cette determination blesse le democratie :(", font=("Arial", 12))
    elif clics_bouton2 >= 3:
        label.config(text="Tu vas refuser encore lontemps !!!", font=("Arial", 12))


fenetre = tk.Tk()
fenetre.title("Est tu pour la democratie ?")


fenetre.geometry("400x600")

label = tk.Label(fenetre, text="Est tu pour la democratie ?", font=("Arial", 12))
label.pack()

bouton1 = tk.Button(fenetre, text="OUI", command=bouton1_click)
bouton1.pack()

bouton2 = tk.Button(fenetre, text="NON", command=bouton2_click)
bouton2.pack()

fenetre.mainloop()
