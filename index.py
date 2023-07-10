import tkinter as tk

def on_text_change(event):
    char = event.char
    texte = textbox.get()
    ttexte = ""
    for char in texte:
        if char == "1" or char == "0":
            ttexte += char
    texte = ttexte
    while len(texte) >= 9:
        texte = texte[:8]
    textbox.delete(0, tk.END)
    textbox.insert(0, texte)
    if texte != "":
        text_respond.config(text=text_respond_texte+str(int(texte, 2)))

fenetre = tk.Tk()
fenetre.title("Bin2Dec")

text = tk.Label(fenetre, text="Entre ici le nombre binaire (8 caractères max) :", font="bold")
text.grid(row=0, column=0, sticky="w")

text_respond_texte = "Nombre décimal : "

text_respond = tk.Label(fenetre, text=text_respond_texte, font="bold")
text_respond.grid(row=1, column=0, sticky="w")

textbox = tk.Entry(fenetre, font=("Arial", 12))
textbox.config(width=8)
textbox.grid(row=0, column=1, sticky="w")

textbox.bind("<KeyRelease>", on_text_change)

fenetre.mainloop()