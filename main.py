from tkinter import*
from assembler import*
from cpu import*
from gpu import*

def simulation():
    affichage.delete("1.0","end")
    code_texte=txt.get("1.0", "end-1c")
    code_machine=decouper(code_texte)
    charger_programme(code_machine)
    executer(affichage)

if __name__ == "__main__":
    fenetre=Tk()
    import gpu
    gpu.fenetre_ref=fenetre
    fenetre.title("ASSEMBLEUR")
    fenetre.geometry("1000x650")
    panneau_principal=Frame(fenetre)
    panneau_principal.pack(expand=True, fill=BOTH)
    cadre_gauche=Frame(panneau_principal)
    cadre_gauche.pack(side=LEFT, expand=True, fill=BOTH, padx=10)
    txt=Text(cadre_gauche, bg="white", height=15)
    txt.pack(expand=True, fill=BOTH, pady=5)
    bouton=Button(cadre_gauche, text="COMPILER", command=simulation)
    bouton.pack(pady=5)
    affichage=Text(cadre_gauche, bg="black", fg="green", height=10)
    affichage.pack(expand=True, fill=BOTH, pady=5)
    cadre_droite=Frame(panneau_principal)
    cadre_droite.pack(side=RIGHT, padx=10)
    ecran = Canvas(cadre_droite, width=320, height=320, bg="black", highlightthickness=1, highlightbackground="gray")
    ecran.pack(pady=5)
    gpu.fenetre_ref=fenetre
    gpu.ecran_ref=ecran
    fenetre.mainloop()
