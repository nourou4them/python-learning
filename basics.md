#### installer pip en téléchargeant le fichier tar.gz ici => https://pypi.org/  

    Extraire le contenu du fichier
    Copier le contenu et le coller dans le répertoire où se trouve python
    Se logguer dans le répertoire et  lancer la commande **python .\setup.py install**
    Installer xlrd en téléchargeant le fichier tar.gz ici => https://pypi.org/
    Utiliser la commande pip install chemin_du_fichier.tar.gz

#### Importer le package qui permet de lire un fichier excel

    import xlrd
    Ouvrir le fichier excel
    example =>  wb = xlrd.open_workbook('C:\\Users\\username\\Desktop\\testpython.xlsx')

#### Regarder le nombre de feuilles et leurs noms

    print ("Nombre de feuilles : "+str(wb.nsheets))
    print ("Nom des feuilles : "+str(wb.sheet_names()))

#### Création d'un objet 'feuille_1'

    feuille_1 = wb.sheet_by_index(0)
    feuille_1 = wb.sheet_by_name("Feuil1")

#### Lire le contenu de la feuille 1

    for rownum in range(feuille_1.nrows):
        print(feuille_1.row_values(rownum))

    colonne1 = feuille_1.col_values(0)
    print(colonne1)

    colonne2 = feuille_1.col_values(1)
    print (colonne2)



##########################################################################################################################################################

    def save_html(html, path)
        with open(path, 'wb') as f:
                f.write(html)
    save_html(r.content,'seneweb.com')





######################################################################################################################################################

#### Basiques
##### Calculer une vitesse, en sachant que vitesse = distance/temps

    temps = 6.892
    distance = 19.7
    vitesse = distance / temps
    vitesse
    2.8583865351131745
    #arrondir à 1 chiffre après la virgule
    round (vitesse, 1)

############################################################################
#### Condition + module (reste d'une division)
    if a % 2 == 0:
        print ("a est pair")
        print ("parce que le reste de sa division par 2 est nul")
    else:
        print ("a est impair")
    Result = a est impair


###########################################################################


    password = 1234
    password1 = password
    if password1 != password:
        print ("Mot de passe invalide")
    elif password1 == password:
        print ("Bienvenue")



    a = 5
    b = 8
    if a > 0:
        # On incrémente la valeur de b
        b += 1
        # On affiche les valeurs des variables
        print("a =",a,"et b =",b)




#### Vérifier si une année est bissextile

    annee = input("Saisissez l'année en question : ")
    annee = int(annee)
    if annee % 4 != 0:
        print("L'année", annee, "n'est pas bissextile")
    elif annee % 4 == 0 and annee % 100 = 0 and annee % 400 = 0:
        print("L'année", annee, "est bissextile")
    else:
        print("L'année", annee, "n'est pas bissextile")

        #####Other solution
    annee = input("Saisissez l'annee en question : ")
    annee = int(annee)
    bissextile = False
    if bissextile % 400 == 0:
        bissextile = True
    elif bissextile % 100 == 0:
        bissextile = True
    elif bissextile % 4 == 0:
        bissextile = True
    else:
        bissextile = False

    if bissextile:
        print("L'année saisie est bissextile")
    else:
        print("L'année saisie n'est pas bissextile")


############# Another solution

    annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
    annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")




###### Plus j'avance en âge et mieux je suis noté

    km = 1000
    litres = 70
    while litres < 60:
        print("Il me reste", km, "km à faire et je n'ai plus que", mark, "litres d'essence")
        km -= 100
        litres -= 10


##### Plus je roule, et moins j'ai de l'essence

    km = 900
    litres = 100
    while km < 1000 and km > 99:
        print("Il me reste", km, "km à faire et je n'ai plus que", litres, "litres d'essence")
        km -= 100
        litres -= 10



#######for...in

    chaine = "Bonjour les ZER0S"
    for lettre in chaine:
        if lettre in "AEIOUYaeiouy": # lettre est une voyelle
            print(lettre)
        else: # lettre est une consonne... ou plus exactement, lettre n'est pas une voyelle
            print("*")





########### Mot clé "break"

    while 1: # 1 est toujours vrai -> boucle infinie
        lettre = input("Tapez 'Q' pour quitter : ")
        if lettre == "Q":
            print("Fin de la boucle")
            break



########## Mot clé "continue"

    i = 1
    while i < 20: # Tant que i est inférieure à 20
        if i % 3 == 0:
            i += 4 # On ajoute 4 à i
            print("On incrémente i de 4. i est maintenant égale à", i)
            continue # On retourne au while sans exécuter les autres lignes
        print("La variable i =", i)
        i += 1 # Dans le cas classique on ajoute juste 1 à i





##############################################################################
######### Les fonctions

    def nom_de_la_fonction(parametre1, parametre2, parametre3, parametreN):
        # Bloc d'instructions

    def table (nb, max):
        i = 0
        while i < max:
                 print(i + 1, "*", nb, "=", (i + 1)*nb)
                 i+=1
    #Pour lancer la fonction
    table (7, 30)



######### mot clé "return"

    def carre(valeur):
        return valeur * valeur
    #Pour lancer
    carre (25)



######### lambda

    f = lambda x: x * x
     f(5)
    25


#####################  fibonacci  ###################

    def fibonacci(n): 
        if n == 0: 
            return 0 
        elif n == 1: 
            return 1 
        else:
            return fibonacci(n - 1) + fibonacci(n - 2) 
        n = int(n) 
        print(fibonacci(n))


###### Other solution

    def fib(n):
        if n == 0: 
            return 0 
        elif n == 1: 
            return 1
        n = int(n)
        n1 = fib(n - 1)
        n2 = fib(n - 2)
        fib2 = n1 + n2
        while n > 1:
            return fib2
        print (fib(n))
    


    ################# Classe
#### La classe est une forme de type de donnée, 
#### sauf qu'elle permet de définir des fonctions 
#### et variables propres au type.

#### L'idée est que tu crées un objet dabord.
#### Ce dernier appartient forcément à une classe (int, str, float).
#### Dès lors, tu peux faire appel à toutes les méthodes de la classe.

#### Les classes sont donc :
###### int
###### str
###### float
###### boolean



# 19/08/2019

#### formatage d'une adresse

    adresse = """
    {no_rue}, {nom_rue}
     {code_postal} {nom_ville} ({pays})
    """.format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
    print(adresse)


#### Gestion d'une liste
##### Ajout d'un élément à la fin de la liste
##### On utilise la méthode # append # pour ajouter un élément à la fin d'une liste.

    ma_liste = [1, 2, 3]
    ma_liste.append(56) # On ajoute 56 à la fin de la liste
    ma_liste
    [1, 2, 3, 56]


#### Concanténation de listes

    ma_liste1 = [3, 4, 5]
    ma_liste2 = [8, 9, 10]
    ma_liste1.extend(ma_liste2) # On insère ma_liste2 à la fin de ma_liste1
    print(ma_liste1)
    [3, 4, 5, 8, 9, 10]
    ma_liste1 = [3, 4, 5]
    ma_liste1 + ma_liste2 # Identique à extend
    [3, 4, 5, 8, 9, 10]
    ma_liste1 += ma_liste2 # Identique à extend
    print(ma_liste1)
    [3, 4, 5, 8, 9, 10]


#### Parcourir une liste

    ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    i = 0 # Notre indice pour la boucle while
    while i < len(ma_liste):
    ...     print(ma_liste[i])
    ...     i += 1 # On incrémente i, ne pas oublier !
    ... 
    a
    b
    c
    d
    e
    f
    g
    h
    
#### Cette méthode est cependant préférable

    ... for elt in ma_liste: # elt va prendre les valeurs successives des éléments de ma_liste
    ...     print(elt)
    ... 
    a
    b
    c
    d
    e
    f
    g
    h

#### Cette méthode est meilleure pour parcourir une liste

    for i, elt in enumerate(mon_nom):
         print("Indice {} = {}.".format(i, elt))


#### Atteindre un item spécifique de la liste 
#### Define a list

    z = [3, 7, 4, 2]
    # Access the first item of a list at index 0
    print(z[0])


#### fonction qui renvoie deux résulats

    def decomposer(entier, divise_par):
        """Cette fonction retourne la partie entière et le reste de
        entier / divise_par"""

    p_e = entier // divise_par
    reste = entier % divise_par
    return p_e, reste


#### Renvoyer un message d'erreur en fonction du type d'erreur

    def resultat(chiffre):
        if type(chiffre) != float:
            raise TypeError("D onnez moi un chiffre quand même")
        chiffre = str(chiffre)
        p_entiere, p_flottante = chiffre.split(".")
        return ",".join([p_entiere, p_flottante[:3]])





### Faire une fonction semblable à Print

    def afficher(*parametres, sep=' ', fin='\n'):
        """Fonction chargée de reproduire le comportement de print.
    
    Elle doit finir par faire appel à print pour afficher le résultat.
    Mais les paramètres devront déjà avoir été formatés. 
    On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :

    print(chaine, end='')"""
    
    # Les paramètres sont sous la forme d'un tuple
    # Or on a besoin de les convertir
    # Mais on ne peut pas modifier un tuple
    # On a plusieurs possibilités, ici je choisis de convertir le tuple en liste
    parametres = list(parametres)
    # On va commencer par convertir toutes les valeurs en chaîne
    # Sinon on va avoir quelques problèmes lors du join
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    # La liste des paramètres ne contient plus que des chaînes de caractères
    # À présent on va constituer la chaîne finale
    chaine = sep.join(parametres)
    # On ajoute le paramètre fin à la fin de la chaîne
    chaine += fin
    # On affiche l'ensemble
    print(chaine, end='')




####### Exercice - Trier une liste avec une clé de fonction

    def triliste(chf)
        return chf[1]


         inventaire = [
    ...     ("pommes", 22),
    ...     ("melons", 4),
    ...     ("poires", 18),
    ...     ("fraises", 76),
    ...     ("prunes", 51),
    ... ]

    listetrie = sorted(inventaire, reverse=True, key=triliste)

    print ("List triée : ", listetrie)
    ### cette solution ci dessus ne fonctionne pas. Elle ne renvoie que le 2nd élément, aulieu de filtrer sur la base de la quantité

### Bonne solution ci dessous :
#### On change le sens de l'inventaire, la quantité avant le nom

    inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]
    # On n'a plus qu'à trier dans l'ordre décroissant l'inventaire inversé
    # On reconstitue l'inventaire trié
    inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in sorted(inventaire_inverse, \
        reverse=True)]



####################################################
## Tuples => (_)
## Liste => [ ]
## Dictionnaire => {_}

#### Le dictionnaire est un objet conteneur c'est à dire qu'il contient d'autres objet


# 09/04/2020
##### Pour supprimer un item dans un dict, il faut :

    del nom_dict["item_a_supprimer"]

##### On peut aussi utiliser 'pop'
    >>> placard = {"chemise":3, "pantalon":6, "tee shirt":7}
    >>> placard.pop("chemise")
    3
    >>>

#### La méthodekeys(« clés » en anglais) renvoie la liste des clés contenues dans le dictionnaire.

    >>> fruits = {"pommes":21, "melons":3, "poires":31}
    >>> for cle in fruits.keys():
    ...     print(cle)
    ... 
    melons
    poires
    pommes
    >>>

#### On peut aussi parcourir les valeurs contenues dans un dictionnaire. 
#### Pour ce faire, on utilise la méthodevalues(« valeurs » en anglais).
    >>> fruits = {"pommes":21, "melons":3, "poires":31}
    >>> for valeur in fruits.values():
    ...     print(valeur)
    ... 
    3
    31
    21
    >>>

# 29/04/2020
#### Lorsqu'on est sur python et qu'on veut changer de répertoire courant

    >>> import os
    >>> os.chdir("C:/tests python")
    >>>

#### On peut ouvrir un fichier directement dans python, en créant d'avoir une variable
#### 'r' = ouverture en mode écriture
#### 'w' = ouverture en mode lecture
#### 'a' = ouverture en mode ajout (append)

    >>> mon_fichier = open("fichier.txt", "r")
    >>> mon_fichier
    <_io.TextIOWrapper name='fichier.txt' encoding='cp1252'>
    >>> type(mon_fichier)
    <class '_io.TextIOWrapper'>
    >>> contenu = mon_fichier.read()
    >>> print(contenu)
    >>> Ceci est le contenu du fichier
    >>> mon_fichier.close()
    >>>
    
#### Autre technique, avec le mot clé "with"

        >>> with open('fichier.txt', 'r') as mon_fichier:
        ...     texte = mon_fichier.read()
        ... 
        >>>



#### Pour enregistre un objet dans un fichier, on utilise le module pickle, avec deux classes : Pickler et Unpickler

    >>> with open('donnees', 'wb') as fichier:
    ...     mon_pickler = pickle.Pickler(fichier)
    ...     # enregistrement ...
    ... 
    >>>

