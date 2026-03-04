vram=[0]*256
fenetre_ref=None
ecran_ref=None

def kernel(id):
    from cpu import registres
    parametre=registres["GPU_PARA"]
    operation=registres["GPU_OP"]
    valeurA=vram[id]
    valeurB=vram[id+registres["GPU_OFFSET_B"]]
    valeurC=vram[id+registres["GPU_OFFSET_C"]]
    match(operation):
        case(1):
            vram[id]=valeurA+parametre
        case(2):
            vram[id]=valeurA-parametre
        case(3):
            vram[id]=valeurA*parametre
        case(4):
            if parametre!=0:
                vram[id]=valeurA//parametre
        case(5):
            vram[id+registres["GPU_OFFSET_C"]]=valeurA+valeurB
        case(6):
            vram[id+registres["GPU_OFFSET_C"]]=valeurA-valeurB
        case(7):
            vram[id+registres["GPU_OFFSET_C"]]=valeurA*valeurB
        case(8):
            if valeurB!=0:
                vram[id+registres["GPU_OFFSET_C"]]=valeurA//valeurB
        case(9):
            vram[id]=1

def dessine_ecran():
    if ecran_ref is None: return
    ecran_ref.delete("all")
    for i in range(len(vram)):
        x=i % 16
        y=i // 16
        taille=20
        x1=x*taille
        y1=y*taille
        x2=x1+taille
        y2=y1+taille
        couleur="white" if vram[i]!=0 else "black"
        ecran_ref.create_rectangle(x1, y1, x2, y2, fill=couleur,outline=couleur)


def dispatcher():
    from cpu import registres
    if registres["GPU_STATE"]==1:
        nb_boucle=registres["GPU_LIMIT"]
        start=registres.get("GPU_START", 0)
        for i in range(start, start + nb_boucle):
            if i < 256:
                kernel(i)
        dessine_ecran()
        registres["GPU_STATE"]=0
        if fenetre_ref:
            fenetre_ref.update_idletasks()
            fenetre_ref.update()
