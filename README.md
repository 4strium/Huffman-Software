# Introduction
[Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding), proposed by [David Huffman](https://en.wikipedia.org/wiki/David_A._Huffman) (1925 – 1999) in 1952, is a **lossless data compression method** used for text, images (JPEG files) or sounds (MP3 files).

In long texts, the letters do not appear with the same frequency. These frequencies vary according to the language used.

Huffman coding consists in **assigning a binary word of variable length to the different symbols of the document to be compressed.** The most frequent symbols are encoded with short words, while the rarest symbols are encoded with longer words (thus recalling the principle of the Morse alphabet).

The constructed code has the particularity of not having **any word prefixed with another word.**

# Representation
*An example of a Huffman tree, generated with the phrase “this is an example of a huffman tree”.*
<html>
    <p align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Huffman_tree_2.svg" alt="Huffman tree generated from the exact frequencies of the text 'this is an example of a huffman tree'. The frequencies and codes of each character are below. Encoding the sentence with this code requires 135 (or 147) bits, as opposed to 288 (or 180) bits if 36 characters of 8 (or 5) bits were used. (This assumes that the code tree structure is known to the decoder and thus does not need to be counted as part of the transmitted information."/>
    </p>
</html>

We first look for the **number of occurrences of each character.** In the example above, the sentence contains 2 times the character h and 7 spaces. Each character constitutes one of the leaves of the tree to which we associate a **weight equal to its number of occurrences.**

The tree is created in the following way: the two nodes with the lowest weights are associated each time, to give a new node whose weight is equivalent to the sum of the weights of its children. This process is repeated until there is only one node left: the root.

**Then, for example, the code 0 is associated with each branch going to the left and the code 1 to the right.**

To obtain the binary code of each character, we go up the tree from the root to the leaves, each time adding a 0 or a 1 to the code depending on the branch followed. The sentence “this is an example of a huffman tree” is then encoded on **135 bits instead of 288 bits** (if the initial encoding of the characters is on 8 bits).

# Project
We will see together how to create a completely autonomous application (with graphical interface) to compress and decompress text files using Huffman coding.

To accomplish this, we will use exclusively the Python programming language, and in particular the [Tkinter module](https://docs.python.org/3/library/tkinter.html) which will be extremely useful for us to create a superb graphical interface!

# Compression/decompression procedure
When you compress a file with Huffman encoding, then to decompress it, you must have in your possession what is called "**the encoding dictionary**" with a binary value corresponding to each character of the uncompressed file.

The problem is that if a user A compresses a text file on his machine, sends it for example by email to a user B, but without the encoding dictionary, it is then strictly impossible for user B to decode the file compress…

So I came up with the idea to write the encoding dictionary on the last line of the compressed text file. I called the grouping of the two elements "**compression_package**".

For the decompression step, my software just has to split the text file in two, with the binary values on one side, and the encoding dictionary on the other!

# Packaging as an executable
Now that we have a fully functional compression/decompression application, a problem arises: the user **does not necessarily have a Python interpreter on his machine, and even less external modules…**

The solution to this problem is to package all lines of code and external modules in a single executable file (.exe)!

To achieve this, we will use an external module named “[PyInstaller](https://pyinstaller.org/en/stable/)”.

Then just open a command prompt in the directory where our Python files are, and enter the following command:
`Pyinstaller --icon=icon\icon_huffman_mellaza.ico --noconsole --onefile --add-data "img/Background_IMAGE.png;img" --add-data "icon\icon_huffman_mellaza.ico;icon" main.py`