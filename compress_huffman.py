# Auteur : Romain MELLAZA
# Compression de chaînes de caractères via la méthode de Huffman.

import networkx as nx
import matplotlib.pyplot as plt
import os
import tkinter

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
    for i in range(len(liste)):
        liste[i] = list(liste[i]) # Liste de tuples convertie en liste de listes.
        liste[i].append([liste[i][0], None, None]) # On ajoute le noeud courant.
    while len(liste) > 1:
        noeud = liste[0][1]+liste[1][1]
        arbreH = [str(noeud), liste[0][2], liste[1][2]]
        arbreN = [str(noeud),noeud, arbreH]
        del liste[0]
        del liste[0]
        liste.append(arbreN)
        liste = sorted(liste,key=lambda a: a[1])
    return arbreH

def huffman2(liste):
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
        liste[i] = list(liste[i]) #liste de tuples en liste de listes
        lchar.append(liste[i][0]) #liste des valeurs de chaque noeud
        liste[i].append([liste[i][0], None, None]) #on ajoute le noeud
    while len(liste) > 1:
        noeud = liste[0][1]+liste[1][1]
        valNoeud = str(noeud)
        if valNoeud in lchar: #aucune valeur identique
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

# Calcul de la hauteur de l'arbre :
def hauteur(arbre_check_hauteur):
    if arbre_check_hauteur == None :
        return -1
    else :
        h1 = 1 + hauteur(arbre_check_hauteur[1])
        h2 = 1 + hauteur(arbre_check_hauteur[2])
        return max(h1,h2)

def repr_graph(arbre, size=(8,8), null_node=False):
    """
    size : tuple de 2 entiers. Si size est int -> (size, size)
    null_node : si True, trace les liaisons vers les sous-arbres vides
    """
    def parkour(arbre, noeuds, branches, labels, positions, profondeur, pos_courante, pos_parent, null_node):
        if arbre != None :
            noeuds[0].append(pos_courante)
            positions[pos_courante] = (pos_courante, profondeur)
            profondeur -= 1
            labels[pos_courante] = str(arbre[0])
            branches[0].append((pos_courante, pos_parent))
            pos_gauche = pos_courante - 2**profondeur
            parkour(arbre[1], noeuds, branches, labels, positions, profondeur, pos_gauche, pos_courante, null_node)
            pos_droit = pos_courante + 2**profondeur
            parkour(arbre[2], noeuds, branches, labels, positions, profondeur, pos_droit, pos_courante, null_node)
        elif null_node:
            noeuds[1].append(pos_courante)
            positions[pos_courante] = (pos_courante, profondeur)
            branches[1].append((pos_courante, pos_parent))
    
    
    if arbre == None:
        return
    
    branches = [[]]
    profondeur = hauteur(arbre)
    pos_courante = 2**profondeur
    noeuds = [[pos_courante]]
    positions = {pos_courante: (pos_courante, profondeur)} 
    labels = {pos_courante: str(arbre[0])}
    
    if null_node:
        branches.append([])
        noeuds.append([])
        
    profondeur -= 1
    parkour(arbre[1], noeuds, branches, labels, positions, profondeur, pos_courante - 2**profondeur, pos_courante, null_node)
    parkour(arbre[2], noeuds, branches, labels, positions, profondeur, pos_courante + 2**profondeur, pos_courante, null_node) 

    mon_arbre = nx.Graph()
    
    if type(size) == int:
        size = (size, size)    
    plt.figure(figsize=size)
    
    nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[0], node_color="white", node_size=550, edgecolors="blue")
    nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[0], edge_color="black", width=2)
    nx.draw_networkx_labels(mon_arbre, positions, labels)

    if null_node:
        nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[1], node_color="white", node_size=50, edgecolors="grey")
        nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[1], edge_color="grey", width=1)

    ax = plt.gca()
    ax.margins(0.1)
    plt.axis("off")
    plt.show()
    plt.close()


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

filename = "data.txt"

with open (filename, "r") as file_no_compress:
    phrase = file_no_compress.read()

filename_compressed = os.path.splitext(filename)[0] + "_compressed.txt"

tabl_occur = ordonne(occurrencesLettre(phrase))
print("\n---------- Occurences des lettres ----------\n",tabl_occur)

abr_bin_huffman = huffman2(tabl_occur)
print("\n---------- Arbre binaire correspondant ----------\n",abr_bin_huffman)

encodage_huff = encode(abr_bin_huffman, code="", dicoC={}, dicoHuf={})

phraseComp = compresse(phrase, encodage_huff)
print("\n---------- Phrase compressée ----------\n",phraseComp)

compression_package = phraseComp + "\n" + str(encodage_huff)
print(compression_package)

with open(filename_compressed, 'w') as file_compress:
   file_compress.write(compression_package)

taux = (1 - len(phraseComp)/(len(phrase)*8))*100
print("\nTexte ASCII compressé à {:.2f} %".format(taux))
