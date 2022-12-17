# Auteur : Romain MELLAZA
# Compression de chaînes de caractères via la méthode de Huffman.

def occurrencesLettre(phrase):
    """
    Donne le nombre d'occurences de chaque caractères de phrase
    
    ---- Parameters ----
    "phrase" --> str
    
    ---- Returns ----
    "dicoF" --> dict

    """
    dicoF = {}
    for occur in phrase:
        if occur not in dicoF:
            dicoF[occur] = 1
        else:
            dicoF[occur] += 1
    return dicoF

def ordonne(dico):
    """
    Convertie le dictionnaire en une liste de tuple
    triée par valeurs croissantes.
    
    ---- Parameters ----
    "dico" --> dict
    
    ---- Returns ----
    "listeF" --> list
    
    """
    listeF = sorted(dico.items(),key=lambda a: a[1])
    return listeF


def huffman(liste):
    """
    Création de l'abre binaire correspondant à
    la liste des occurences.
    
    ---- Parameters ----
    "liste" --> list
    
    ---- Returns ----
    "arbreH" --> list (Binary Tree)

    """
    charAscii = 97
    lchar = []
    for i in range(len(liste)):
        liste[i] = list(liste[i]) # Liste de tuples en liste de listes
        lchar.append(liste[i][0]) # Liste des valeurs de chaque noeud
        liste[i].append([liste[i][0], None, None]) # On ajoute le noeud
    while len(liste) > 1:
        noeud = liste[0][1]+liste[1][1]
        valNoeud = str(noeud)
        if valNoeud in lchar: # Aucune valeur identique
            valNoeud += chr(charAscii)
            charAscii += 1
        lchar.append(valNoeud)
        arbreH = [valNoeud, liste[0][2], liste[1][2]]
        arbreN = [valNoeud, noeud, arbreH]
        del liste[0]
        del liste[0]
        liste.append(arbreN)
        liste = sorted(liste,key=lambda a: a[1])
    return arbreH

def encode(abr,code="",dicoC={},dicoHuf={}):
    """
    Donne le code préfixe de toutes les feuilles de l'arbre.
    
    ---- Parameters ----
    "abr" --> list (Binary Tree)
    code --> str (Binary Code)
    dicoC --> dict (All the node with their corresponding code)
    
    ---- Returns ----
    "dicoHuf" --> dict (Leaves + Code)

    """
    if dicoC == {}:
        dicoC[abr[0]] = code
    if abr is None:
        return []
    elif abr[1] != None and abr[2] != None:
        dicoC[abr[1][0]] = dicoC[abr[0]]+"0"
        dicoC[abr[2][0]] = dicoC[abr[0]]+"1"
        code=dicoC[abr[1][0]]
    else:
        code=code[:-1]
        dicoHuf[abr[0]] = dicoC[abr[0]]
        return
    encode(abr[1], code, dicoC, dicoHuf)
    encode(abr[2], code, dicoC, dicoHuf)
    return dicoHuf

def compresse(phrase, dicoHuf):
    """
    Réalise la traduction de la phrase en code de Huffman avec le dictionnaire dicoHuf
    
    ---- Parameters ----
    phrase --> string
    "dicoHuf" --> dict (Leaves + Code)
    
    ---- Returns ----
    phrase_comp --> str
    """
    phraseComp = ""
    for c in phrase:
        phraseComp += dicoHuf[c]
    return phraseComp