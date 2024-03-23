from compress_huffman import *      # On importe les fonctions de compression
from decompress_huffman import *    # On importe les fonctions de décompression
from get_path import *
import tkinter                      # Module pour créer une interface graphique, et ses dépendances.
from tkinter import *               
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import ttk          
import os                   # Module pour manipuler les différntes fichiers sur le système de l'user.

# On génère la fenêtre :
root = tkinter.Tk()

# Je défini des paramètres à cette fenêtre :
root.title("Compresseur/décompresseur de fichiers via la méthode Huffman")  # Un titre
root.geometry("1080x720")                                # Une résolution d'affichage, ici HD
root.minsize(1080, 720)                                  # Je bloque cette résolution, pour éviter que l'utilisateur ne redimensionne n'importe comment.
root.maxsize(1080, 720)
root.iconbitmap(default= resource_path('icon\icon_huffman_mellaza.ico')) # Je défini un icon pour la fenêtre

# J'importe et j'affiche une image de fond pour mon accueil :
bg = PhotoImage(file = resource_path("img\Background_IMAGE.png"))
canvas_accueil = Canvas( root, width = 1080, height = 720)
canvas_accueil.pack(fill = "both", expand = True)
canvas_accueil.create_image( 0, 0, image = bg, anchor = "nw")

# J'affiche un titre sur ma page d'accueil :
i=canvas_accueil.create_text(540.45, 137, text=" Choisissez l'action qui vous convient : ", font=("Helvetica", 42), fill="white", justify = CENTER)
r=canvas_accueil.create_rectangle(canvas_accueil.bbox(i),fill="#feb58a", width = 1)                                                            
canvas_accueil.tag_lower(r,i)


def compression():
    """
    Procédure appelée quand l'user. appuie sur le bouton "Compresser un fichier"
    """
    global l,m,i,r,o,p,taux_bar     # Les différents éléments graphiques, je les mets en "global" afin
                                    # qu'ils puissent être supprimés/modifiés par la fonction de décompression.

    # L'utilisateur ne pourra sélectionner que les fichiers textes :
    filetypes = [
        ('Fichiers textes', '*.txt')
    ]
    
    # Un pop-up apparaît sur l'écran pour séléctionner le fichier à compresser.
    filename = fd.askopenfilename(
        title='Selectionnez le fichier à compresser...',
        initialdir='/',
        filetypes=filetypes
    )

    # Ouverture et lecture du fichier :
    with open (filename, "r") as file_no_compress:
        phrase = file_no_compress.read()

    # Génération du nom du fichier compressé :
    filename_compressed = os.path.splitext(filename)[0] + "_compressed.txt"

    # Appel des différentes fonctions du fichier .py de compression :
    tabl_occur = ordonne(occurrencesLettre(phrase))
    abr_bin_huffman = huffman(tabl_occur)
    encodage_huff = encode(abr_bin_huffman, code="", dicoC={}, dicoHuf={})
    phraseComp = compresse(phrase, encodage_huff)

    # Création d'un package qui va être écrit dans le fichier compressé :
    compression_package = phraseComp + "\n" + str(encodage_huff)

    # Écriture du fichier compressé :
    with open(filename_compressed, 'w') as file_compress:
        file_compress.write(compression_package)

    # Calcul du taux de compression :
    taux = round((1 - len(phraseComp)/(len(phrase)*8))*100,2)

    # Suppression des éléments graphiques précédemment affichés :
    canvas_accueil.delete(i)
    canvas_accueil.delete(r)
    try :
        canvas_accueil.delete(g)
        canvas_accueil.delete(h)
    except :
        pass
    try :
        canvas_accueil.delete(o)
        canvas_accueil.delete(p)
        canvas_accueil.delete(l)
        canvas_accueil.delete(m)
        taux_bar.destroy()
    except:
        pass

    # Affichage de "Compression effectuée avec succès !" sur l'écran :
    o=canvas_accueil.create_text(540.45, 137, text=" Compression effectuée avec succès ! ", font=("Helvetica", 42), fill="white", justify = CENTER)
    p=canvas_accueil.create_rectangle(canvas_accueil.bbox(o),fill="#feb58a", width = 1)                                                            
    canvas_accueil.tag_lower(p,o)

    # Affichage du taux de compression sur l'écran :
    l=canvas_accueil.create_text(540.45, 275, text=" Taux de compression ➔ " + str(taux) + " %", font=("Helvetica", 20), fill="white", justify = CENTER)
    m=canvas_accueil.create_rectangle(canvas_accueil.bbox(l),fill="#feb58a", width = 1)                                                            
    canvas_accueil.tag_lower(m,l)

    # Affichage d'une bar de progression avec le taux de compression correspondant :
    taux_bar = ttk.Progressbar(canvas_accueil, orient=HORIZONTAL, length=500, mode='determinate')
    taux_bar.pack(pady=300)

    taux_bar['value'] = taux


def decompression():
    """
    Procédure appelée quand l'user. appuie sur le bouton "Compresser un fichier"
    """
    global g,h          # Les différents éléments graphiques, je les mets en "global" afin
                        # qu'ils puissent être supprimés/modifiés par la fonction de compression.

    # L'utilisateur ne pourra sélectionner que les fichiers textes :
    filetypes = [
        ('Fichiers textes', '*.txt')
    ]

    # Un pop-up apparaît sur l'écran pour sélectionner le fichier à compresser.
    filename = fd.askopenfilename(
        title='Selectionnez le fichier à décompresser...',
        initialdir='/',
        filetypes=filetypes
    )

    # Suppression des éléments graphiques précédemment affichés :
    try :
        canvas_accueil.delete(i)
        canvas_accueil.delete(r)
    except :
        pass
    try :
        canvas_accueil.delete(o)
        canvas_accueil.delete(p)
        canvas_accueil.delete(l)
        canvas_accueil.delete(m)
        taux_bar.destroy()
    except:
        pass

    # Lecture du fichier compressé :
    with open (filename, "r") as file_compressed:
        txt_file_work = file_compressed.read()

        # Séparation du texte compressé et du dico Huffman écris dans le fichier compressé :
        compressed_texte = txt_file_work.partition('\n')[0]
        encodage_huff = txt_file_work.partition('\n')[-1]
        encodage_huff = eval(encodage_huff)

    # Appel de la fonction de décompression du fichier .py
    phraseDecomp = decompresse(compressed_texte, encodage_huff)

    # Affichage de "Déompression effectuée avec succès !" sur l'écran :
    g=canvas_accueil.create_text(540.45, 137, text=" Décompression effectuée avec succès ! ", font=("Helvetica", 42), fill="white", justify = CENTER)
    h=canvas_accueil.create_rectangle(canvas_accueil.bbox(g),fill="#feb58a", width = 1)                                                            
    canvas_accueil.tag_lower(h,g)

    # Génération du nom du fichier décompressé :
    filename_decompressed = os.path.splitext(filename)[0] + "_decompressed.txt"

    # Écriture du fichier décompressé :
    with open(filename_decompressed, 'w') as file_decompress:
        file_decompress.write(phraseDecomp)

    

# Définition du bouton pour sélectionner le mode de compression :
button_compression = Button(root, text="Compresser un fichier .txt", command=compression, font=("Helvetica", 26), fg='white', bg="#feb58a", height = 2, width = 24)
button_compression_window = canvas_accueil.create_window(30, 425, anchor='nw', window=button_compression)

# Définition du bouton pour sélectionner le mode de décompression :
button_decompression = Button(root, text="Décompresser un fichier .txt", command=decompression, font=("Helvetica", 26), fg='white', bg="#feb58a", height = 2, width = 24)
button_decompression_window = canvas_accueil.create_window(560, 425, anchor='nw', window=button_decompression)



def msg_remerciement():
    '''
    Cette procédure affiche un message de remerciement lorsque l'utilisateur ferme la fenêtre principale.
    Puis elle met fin au fonctionnement de celle-ci.
    '''
    messagebox.showinfo('Dev : Romain MELLAZA',"Merci d'avoir utilisé mon logiciel ! :)")
    root.destroy()

# Ces lignes de codes permettent au programme d'actionner la fonction de remerciement si il reçoit l'information que l'utilisateur essaie de fermer le logiciel :
try:
    root.protocol('WM_DELETE_WINDOW', msg_remerciement)
except:
    pass


# Je rafraîchis continuellement mon application via cette commande :
root.mainloop()