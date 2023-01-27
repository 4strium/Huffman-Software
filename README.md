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