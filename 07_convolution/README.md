<h2> Convolution </h2>

General purpose image filtering.

<br><br><br><br>

<b> Usage: </b>
<br><br>
<b> General: </b> ```python3 main.py --path lena.jpg --kernel sharpen --stride 1 1 --padding 1 1 --dilation 1 1```
![alt text](https://github.com/rohan1198/Image-Processing-Projects/blob/main/07_convolution/assets/general.png)
<br><br>

<b> Specific Filtering Operations: </b>
<br><br>
<b> Identity: </b> ```python3 main.py --path lena.jpg --kernel identity```
![alt text](https://github.com/rohan1198/Image-Processing-Projects/blob/main/07_convolution/assets/identity.png)
<br><br>

<br><br>
<b> 3x3 Gaussian Blurring: </b> ```python3 main.py --path lena.jpg --kernel blur3```
![alt text](https://github.com/rohan1198/Image-Processing-Projects/blob/main/07_convolution/assets/blur3x3.png)
<br><br>

<br><br>
<b> 5x5 Gaussian Blurring: </b> ```python3 main.py --path lena.jpg --kernel blur5```
![alt text](https://github.com/rohan1198/Image-Processing-Projects/blob/main/07_convolution/assets/blur5x5.png)
<br><br>

<br><br>
<b> Sharpen: </b> ```python3 main.py --path lena.jpg --kernel sharpen```
![alt text](https://github.com/rohan1198/Image-Processing-Projects/blob/main/07_convolution/assets/sharpen.png)
<br><br>

<br><br>
<b> Outline: </b> ```python3 main.py --path lena.jpg --kernel outline```
![alt text](https://github.com/rohan1198/Image-Processing-Projects/blob/main/07_convolution/assets/outline.png)
<br><br>

<br><br>
<b> Unsharp: </b> ```python3 main.py --path lena.jpg --kernel unsharp```
![alt text](https://github.com/rohan1198/Image-Processing-Projects/blob/main/07_convolution/assets/unsharp.png)
<br><br>

<br><br>
<b> Changing stride: </b> ```python3 main.py --path lena.jpg --kernel blur3 --stride 1 2```
![alt text](https://github.com/rohan1198/Image-Processing-Projects/blob/main/07_convolution/assets/stride.png)
<br><br>
