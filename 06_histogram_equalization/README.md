<h2> Histogram Equalization </h2>

Adjust the global contrast of a grayscale image by changing the pixel intensity distribution.

1. Simple Histogram Equalization
2. Adaptive Histogram Equalization

<br><br><br><br>

<b> Usage: </b>
<br><br>
<b> General: </b> ```python3 equalize.py --path ../lena.jpg```


<b> Specific Method </b>
- Simple Histogram Equalization: ```python3 equalize.py --path ../lena.jpg --method simple```
![alt text](https://github.com/rohan1198/Computer-Vision-Projects/blob/main/06_histogram_equalization/assets/simple_eq.png)

<br><br>
- Adaptive Histogram Equalization: ```python3 equalize.py --path ../lena.jpg --method adaptive --clip 2 --grid 8```
![alt text](https://github.com/rohan1198/Computer-Vision-Projects/blob/main/06_histogram_equalization/assets/adaptive_eq.png)