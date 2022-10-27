def choix_piece(liste_pieces):
    numeros_piece = input("choix pièce joueur 1")  # choix dans la liste des pièces
    for i in liste_pieces:
        if(liste_pieces[i] == numeros_piece):
            piece = liste_pieces[i]
    return piece

def orientation():
    orientation = int(input("choix orientation (1 , 2 , 3 ou 4)"))
    while(orientation < 1 or orientation > 4):
        print("orientation impossible")
        orientation = int(input("choix orientation (1 , 2 , 3 ou 4)"))