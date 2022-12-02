# Auteur : Romain MELLAZA

import os

def decompresse(phrase_comp, dicoHuf):
    pile_letter = []
    txt_decomp = ""
    for value in phrase_comp :
        pile_letter.append(value)
        temp = str(''.join(pile_letter))
        if temp in dicoHuf.values() :
            letter = [i for i in dicoHuf if dicoHuf[i]==temp]
            letter = str(letter[0])
            txt_decomp += letter
            pile_letter.clear()
    return txt_decomp

