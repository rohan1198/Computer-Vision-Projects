<h2> Image Morphological Operations </h2>

1. Erosion
2. Dilation
3. Opening
4. Closing
5. Gradient

<br><br>
- Morphological Operations are image processing operations applied to grayscale or binary images.

<br><br><br>
<b> Usage: </b><br><br>

<b> General: </b>: ```python3 morph.py --op erosion --path ../lena.jpg --iter 3 --kernel 7``` <br><br>
<b> Operation Specific: </b><br>
Erosion: ```python3 morph.py --op erosion --path ../lena.jpg --iter 3``` <br>
![alt text](https://github.com/rohan1198/Computer-Vision-Projects/blob/main/03_morphological_operations/assets/eroded.png)

<br><br>
Dilation: ```python3 morph.py --op dilation --path ../lena.jpg --iter 3``` <br>
![alt text](https://github.com/rohan1198/Computer-Vision-Projects/blob/main/03_morphological_operations/assets/dilated.png)

<br><br>
Opening: ```python3 morph.py --op opening --path ../lena.jpg --kernel 7``` <br>
![alt text](https://github.com/rohan1198/Computer-Vision-Projects/blob/main/03_morphological_operations/assets/opened.png)

<br><br>
Closing: ```python3 morph.py --op closing --path ../lena.jpg --kernel 7``` <br>
![alt text](https://github.com/rohan1198/Computer-Vision-Projects/blob/main/03_morphological_operations/assets/closed.png)

<br><br>
Gradient: ```python3 morph.py --op gradient --path ../lena.jpg --kernel 7``` <br>
![alt text](https://github.com/rohan1198/Computer-Vision-Projects/blob/main/03_morphological_operations/assets/gradient.png)
