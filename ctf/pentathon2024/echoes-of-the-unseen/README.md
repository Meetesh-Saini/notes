# Echoes of the Unseen

## Description 
Within the digital void, a silent challenge beckons. No maps, no signs only intuition guides. Will you decode the whispers of light and shadow, or succumb to obscurity? Journey forth, unveil the unseen.

## Steps
- Extract the file. It contains a corrupted PNG.
- Open the file in hexedit.
- The first byte is corrupted, it must be `89` but it is `98`.
![alt text](image.png)
- Save and Run pngcheck with verbose mode.
![alt text](image-1.png)
- Change `IFAT` to `IDAT` at offset `0x00025` (IDAT is a valid chuck in the PNG specification)
![alt text](image-2.png)
![alt text](image-3.png)

- Save and check again
![alt text](image-4.png)
- Change `ICAT` to `IDAT` at offset `0x10031`
![alt text](image-5.png)
![alt text](image-6.png)

- Save and check again
![alt text](image-7.png)

- Remove the trailing data 
![alt text](image-8.png)
- No errors are detected
![alt text](image-9.png)

- The image says `I LOVE ALPHA`.
![alt text](image-10.png)

- This hints to something related to alpha channel and the image looks noisy so I ran `zsteg` and got the flag.
![alt text](image-11.png)