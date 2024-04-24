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

