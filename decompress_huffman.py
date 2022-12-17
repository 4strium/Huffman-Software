# Auteur : Romain MELLAZA
# Décompression de chaînes de caractères via la méthode de Huffman.

def decompresse(phrase_comp, dicoHuf):
    """
    Réalise la traduction du code de Huffman en phrase avec le dictionnaire dicoHuf
    
    ---- Parameters ----
    phrase_comp --> string
    "dicoHuf" --> dict (Leaves + Code)
    
    ---- Returns ----
    txt_decomp --> str
    """
    pile_letter = []            # On génère une pile vide.
    txt_decomp = ""             # String qui va accueillir le texte décompressé.
    for value in phrase_comp :              # On parcourt le texte compressé.
        pile_letter.append(value)           # On ajoute chaque bit dans la pile.
        temp = str(''.join(pile_letter))    # On convertis la pile actuelle en string.
        if temp in dicoHuf.values() :       # Si les bits correspondent à une lettre dans le dico.
            letter = [i for i in dicoHuf if dicoHuf[i]==temp]   # On recupère la clé (ici le caractère) correspondant à la valeur.
            letter = str(letter[0])         # On convertis le caractère en string
            txt_decomp += letter            # On ajoute le caractère au texte décompressé.
            pile_letter.clear()             # On vide complètement la pile.
    return txt_decomp           # On retourne le texte décodé !