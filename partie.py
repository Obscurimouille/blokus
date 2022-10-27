from action_joueur import choix_piece,couleur,position

def jeu():
    while(True):
        for J in range(1,5):
            piece = [[1, 0, 1], [1, 1, 1], [0, 1, 0]]
            #piece = choix_piece(tableau_piece)
            #choix_piece = input("choix forme joueur 1",piece)    #choix dans tableau pièces
            piece = couleur(J,piece)
            position(piece)
            J += 1