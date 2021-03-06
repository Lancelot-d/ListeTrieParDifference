import random
from traceback import print_exc

'''
	 * Cette méthode permet de récuperer la liste initial 
	 * @return Une liste de INT de taille variable
	 
'''
def recuperListe():
    tailleListe=1
    #Tant que impair demande le nombre de d'elements souhaités
    while tailleListe%2 !=0 and tailleListe <=4:
        print("Entrer le nombres d'elements que vous souhaitez ?(nombre pair et supérieur a 4) : ")
        tailleListe = int(input())

    listeNombre = []
    while len(listeNombre) < tailleListe:
        print("Entrer le nombre n{} :".format(len(listeNombre)+1))
        nombre = int(input())
        if nombre not in listeNombre:
            listeNombre.append(nombre)
        else:
            print("\n!!! veuillez entrer un nombre différent de ceux utilisés précédemment !!!\n")

    return listeNombre
'''
	 * Cette méthode de calculer le factorielle d'un nombre 
	 *@param nombre a factoriser
	 * @return résulat de la factorisation

'''
def fact(n):
    x=1
    for i in range(2,n+1):
        x*=i
    return x
'''
	 * Cette méthode permet trouver toutes les combinaison d'une liste
	 *@param liste de INT de taille variable
	 * @return Une liste contenant une liste par combinaison possible 

'''
def trouverCombinaisonListe(listeNombre):
    combinaisonPossible = []
    combinaisonPossible.append(listeNombre)

    #TANT QUE toutes les combinaisons n'ont pas était trouvé
    while len(combinaisonPossible) < fact(len(listeNombre)):
        listeTemporaire = []

        #Permet de ne pas mettre l'objet dans la nouvelle liste mais bien son contenu
        for i in range(len(listeNombre)):
            listeTemporaire.append(listeNombre[i])

        random.shuffle(listeTemporaire) #Mélange la liste
        compteurListeDifferente = 0

        #utile pour debug la fonction
        #print(len(combinaisonPossible), " liste actuel :", listeTemporaire, "combinaison possible: ",combinaisonPossible )

        #Test la nouvelle combinaison avec toute les anciennes
        for i in range(len(combinaisonPossible)):
            compteurNombreIdentique = 0
            for y in range(len(listeNombre)):
                if listeTemporaire[y] == combinaisonPossible[i][y]:
                    compteurNombreIdentique+=1
            if compteurNombreIdentique < 4:
                compteurListeDifferente+=1
        if compteurListeDifferente == len(combinaisonPossible): #un compteur egale au nombre d'éléments de la liste de combinaison signifie qu'aucune liste n'est identique à la listeTemporaire
            combinaisonPossible.append(listeTemporaire) # ajoute la combinaison a liste des differentes combinaisons

    #utile pour debug
    #print("Liste de toutes les combinaisons: ",combinaisonPossible)
    return combinaisonPossible

'''
	 * Cette méthode permet trouver toutes les combinaisons qui agissent comme la suite x,y et z tel que (x-y) > (y-z)
	 *@param Une liste contenant une liste par combinaison possible ( Liste de liste de int )
	 * @return Une liste contenant toutes les combinaisons prouvant la regles : x,y et z tel que (x-y) > (y-z)
'''
def trouversuiteordonancer(listenombre):
    leslistesvalides = []
    tailleliste = len(listenombre[0])

    for i in range(len(listenombre)):  # Pour nombre de combinaison ( pour 4 = 4^2 = 16 )
        compteur = 0
        for y in range(int(tailleliste/2)):  # le nombre de fois a éxécuté correspond au nombre d'éléments de la liste - 1
            # Tres utile pour visualiser le fonctionement
            #print(abs(listenombre[i][y] - listenombre[i][y + 1]), ">=",abs(listenombre[i][y + 1] - listenombre[i][y + 2]))
            if abs(listenombre[i][y] - listenombre[i][y + 1]) >= abs(listenombre[i][y + 1] - listenombre[i][y + 2]):
                compteur += 1
        if compteur == int(tailleliste/2):
            # si le compteur correspond au nombre d'éléments de la liste - 1 cela signifie que le résultat est valide
            leslistesvalides.append(listenombre[i])
    #print("Nombre de combinaisons: ", len(listenombre))
    print("Les listes valides sont les suivantes: {}".format(leslistesvalides))
    return leslistesvalides

def main():
    try:
        listeNombre = recuperListe()
        trouversuiteordonancer(trouverCombinaisonListe(listeNombre))
    except:
        print_exc()

if __name__ == '__main__':
    quit(main())