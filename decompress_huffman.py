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

filename = "data_compressed.txt"

with open (filename, "r") as file_compressed:
    txt_file_work = file_compressed.read()

    compressed_texte = txt_file_work.partition('\n')[0]
    encodage_huff = txt_file_work.partition('\n')[-1]
    encodage_huff = eval(encodage_huff)
    print(encodage_huff)


phraseDecomp = decompresse(compressed_texte, encodage_huff)
print("\n---------- Phrase décompressée ----------\n",phraseDecomp)

filename_decompressed = os.path.splitext(filename)[0] + "_decompressed.txt"

with open(filename_decompressed, 'w') as file_decompress:
   file_decompress.write(phraseDecomp)