<h2> Image Morphological Operations </h2>

1. Erosion
2. Dilation
3. Opening
4. Closing

<br><br>
- Morphological Operations are image processing operations applied to grayscale or binary images.

<br><br><br>
<b> Usage: </b><br><br>
Erosion: python3 morph.py --op erosion --path ../lena.jpg --iter 3 --kernel 7

<br><br>
Dilation: python3 morph.py --op dilation --path ../lena.jpg --iter 3 --kernel 7

<br><br>
Opening: python3 morph.py --op opening --path ../lena.jpg --iter 3 --kernel 7

<br><br>
Closing: python3 morph.py --op closing --path ../lena.jpg --iter 3 --kernel 7