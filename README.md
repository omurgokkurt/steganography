## steganography
https://github.com/omurgokkurt/steganography  
Storing 6 bits of data in each pixel of an image. Capable of encoding a large text file into a .png and decoding it.

## how it works:
We normalize each RGB channel value to value % 4 = 0, thus each channel gives us 2 bits to store data in it. Manipulating a channel value in a such  insignificant range (1 to 3) practically creates no visual difference to the human eye. Number of pseudo-bits allocated could be increased, in exchange of "deep frying" the image


## usage:
Pillow is required to run the code:
``` 
python -m pip install --upgrade pip
python -m pip install --upgrade Pillow
```
 
to encode 
``` 
python steg.py encode image.png text.txt
```
to decode 
``` 
python steg.py decode image.png
```

## example output:  
The painting *Still-Life with a Skull* by Philippe De Champaigne, containing the 232,051 characters long *Meditations* by Marcus Aurelius (Shout out to my homie Marcus and also https://www.gutenberg.org):  

![*Still-Life with a Skull* by Philippe De Champaigne](https://raw.githubusercontent.com/omurgokkurt/steganography/main/memento_mori_encoded.png)

The original image, for comparison:  
![*Still-Life with a Skull* by Philippe De Champaigne](https://raw.githubusercontent.com/omurgokkurt/steganography/main/memento_mori.png)
