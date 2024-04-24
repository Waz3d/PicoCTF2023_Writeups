# PicoCTF2023_Writeups
Writeups of (hopefully all) the challenges of the PicoCTF2023 competition

The writeups will be divided by category and will be ordered by points assigned.

The flags will be slightly obscured so that the reader may try the challenge by himself.

# Crypto

## HideToSee (100pts)
How about some hide and seek heh?

![atbash](https://github.com/Waz3d/PicoCTF2023_Writeups/assets/96386635/cdee59df-a398-40cc-9604-d7401cca46f0)

Before starting the challenge, a quick google search for "atbash" showed that it is a simple character substitution cryptographical algorithm.

First things first i checked the contents of the image:
```bash
$ strings atbash.jpg
```
but nothing seemed to be encrypted using said algorithm.
I then checked if there was any hidden file using:
```bash
$ binwalk atbash.jpg
```
with no luck.
I also analyzed the image using stegsolve but nothing was found.
Finally, after using steghide, a ".txt" file was found within the image.

![github_img](https://github.com/Waz3d/PicoCTF2023_Writeups/assets/96386635/b58735d8-9805-4d22-8774-0d7532698d17)

The file contained a string encrypted with the atbash encoding, that once decoded gave the flag

### picoCTF{atbash_crack_XXXXXX}

## ReadMyCert (100pts)

