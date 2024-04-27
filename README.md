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
How about we take you on an adventure on exploring certificate signing requests

The challenge provides a certificate. The name of the challenge suggests to actually read into in.
The content of the certificate is the following: 

-----BEGIN CERTIFICATE REQUEST-----

MIICpzCCAY8CAQAwPDEmMCQGA1UEAwwdcGljb0NURntyZWFkX215Y2VydF82OTNm
N2MwM30xEjAQBgNVBCkMCWN0ZlBsYXllcjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBAPp+XuDB3ZkmrkvAsgtjP+mjIcYDWfptuZsJieu6eRl39wl4Sg38
+/OfY24LV9sNmgKyTGvpmCaUoZMYkvkulYSoFzE0xqPBo6kruLEyIvqqpAFqRH2b
mierLT6RcKgJHYr/Vt6SwP8NCCawCrvhQ4NZcuB49Hr/2AiGHzmf86/lG/c+lhmH
gyqPb1kDghsVxi/GNs9i7AgniZikqT8OTp0INmmCgZtJn1Jo615Iu/tFiC8Sfhhg
QHmTDLjgx1oP1kvZV2PE5UUN/oC05Zup8f31LksXZwpazZKwYC/LbN96HdqgVQ9K
S8e/4I7MJQmPmLIsLp3sdL2FiDGML3smAi0CAwEAAaAmMCQGCSqGSIb3DQEJDjEX
MBUwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAOxSR8Fs
Tdjfu9e0vRNqKWd09ISmYDQc3qnSbLRlYZyMK4pguALq310h/1nNgURWESbNJPOp
FkBWG0XWhWyWP7rTqxo/pk9AKx0TNbHDrS6KiBnKPq0mxjPZsH1L7wNYDc5OANDl
btvn3zT7lMms6z1qM7xUWXR76n2xL/81cdF725nBZ00mWmPW0S1pSmA4EEHCEgNW
0vWQqsIDki3gYc4NCm8OHjx79kcwE+ksyc6vHgMOwsYoOFJnyayhl15oN/3x7hW3
G1xovPupABpfOSNOcTwbgfrfjUDOLx/wirvj9L1N5EGDh4FOLaRZDs+tMrimGBBS
zGU13BnykmQ5jOQ=

-----END CERTIFICATE REQUEST-----

Simply by copying and pasting it in an online certificate reader, it is possible to visualize informations like the subject and a summary.
Moreover, inside the "Common Name" field, there will be our flag.

### picoCTF{read_mycert_XXXXXXXX}

## Rotation (100pts)
You will find the flag after decrypting this file

The challenge provides a ".txt" file, containing the following cyphertext:

xqkwKBN{z0bib1wv_l3kzgxb3l_949in1i1}

The name suggests a rotation encryption, such as Caesar's encryption.
Testing the different 26 possible rotations once can get the flag.
The key for the rotation is found out to be 8 to the right or 18 to the left.

### picoCTF{r0tat1on_d3crypt3d_XXXXXXXX}

## PowerAnalysis: Warmup (200pts)
This encryption algorithm leaks a "bit" of data every time it does a computation. Use this to figure out the encryption key.
The flag will be of the format picoCTF{<encryption key>} where <encryption key> is 32 lowercase hex characters comprising the 16-byte encryption key being used by the program.

To solve the challenge we are given a python script.

Within the python script one can clearly see that only the least significant bit of the cyphertext is leaked. Moreover, the output is only the number of odd results after the encryption, byte per byte, using the secret key and
a Sbox. The idea to obtain the key is to exploit the fact that we know the Sbox and the fact that we can easily see if the result of Sbox[ our_byte ^ key_byte ] is even or odd.

If one tries to connect to the server and send the string 

00000000000000000000000000000000

will obtain as output the number of odd results after the Sbox, which in our case will be 6.

Sending instead:

ff000000000000000000000000000000

will give give yet again as a result the number 6, but, giving 

11000000000000000000000000000000

will instead output 7.

This means that Sbox[ 0x00 ^ key_byte ] give an even result, same goes for Sbox[ 0xff ^ key_byte ] but Sbox[ 0x11 ^ key_byte ] give instead an odd result.

Following this idea, it is possible using a python script and pwntools, to quickly test each byte of the 16 bytes of the key, obtain a map that associates
input_byte to a 0 if the result is even, 1 if it's odd. Given the map, we can test 256 possible values for the key_byte and find the one and only that will
respect the map obtained from the server.

This can be done for each byte of the key, thus obtaining the flag.
The python script used will be provided in the reporitory and it can be found in 
#### Crypto -> PowerAnalysis: Warmup

### picoCTF{6f040f33f3521c634878c02fXXXXXXXX}

## PowerAnalysis: Part 1 (400pts)
This embedded system allows you to measure the power consumption of the CPU while it is running an AES encryption algorithm. Use this information to leak the key via dynamic power analysis.

Upon connecting to the remote server, after providing a 16 byte plaintext in hex format, you will be given a trace of 2666 CPU power consumption values.
Online research suggests that AES Dynamic Power Analysis attacks can leak informations about the key given the correlation with the Hamming distance.

If one tries to send the same plaintext twice to the remote server, he will be getting traces with different values. This is because there is some noise
introduced in the power consumption metric, thus making the attack slightly harder.

After a lot of online reasearch i found a very handy python library called SCAred, which can be easily installe with 

'''bash
pip install scared
'''

The latter contains a set of functions for the implementation of side-channel analysis, such as in fact the dynamic power consumption attacks.

The method that should be used to implement the attack is CPAAttack, as it can be seen in the attack.py file at the following path:
#### Crypto -> PowerAnalysis: Part 1

The idea behind the attack is to exploit the fact that we can obtain an infinite amount of combinations of plaintexts - traces, thus allowing us to eventually get the
amount of informations required to find the plaintext that correlates the most with the key, looking at the power consumption traces.

This can be done by the CPAAttack method provided by "scared".

The attack can be implemented in a simple way:
Create a set of randomly generated plaintexts, making sure that for each byte index there will be every possible byte at least once (simply create a plaintext list of at least 300 entries to be sure).
Collect the traces for each of the generated plaintext.
Start the CPAAttack.
Find the bytes that, for each index in the plaintext, obtained the highest score for the correlation.

### picoCTF{af55be9bb08d78491b0aa416XXXXXXXX}
