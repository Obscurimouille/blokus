def choix_piece(liste_pieces):
    numeros_piece = input("choix pièce joueur 1")  # choix dans la liste des pièces
    for i in liste_pieces:
        if(liste_pieces[i] == numeros_piece):
            piece = liste_pieces[i]
    return piece

def couleur(J,paterne):
    print(paterne)
    a = 0
    for c in paterne:
        b = 0
        for d in c:
            paterne[a][b] = d * J
            b += 1
        a += 1
    print(paterne)
    return paterne

def position(paterne):
    x = int(input("choix colone plateau"))
    while (x < 0 or x > 20):
        print("La colonne n'est pas sur le plateau")
        x = int(input("choix colone plateau"))

    y = int(input("choix ligne plateau"))
    while (y < 0 or y > 20):
        print("La ligne n'est pas sur le plateau")
        y = int(input("choix ligne plateau"))
    orientation()
    plateau[x][y] = paterne

def orientation():
    orientation = int(input("choix orientation (1 , 2 , 3 ou 4)"))
    while(orientation < 1 or orientation > 4):
        print("orientation impossible")
        orientation = int(input("choix orientation (1 , 2 , 3 ou 4)"))