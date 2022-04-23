<h2> Image Blurring and Smoothing </h2>

1. Average Blurring
2. Gaussian Blurring
3. Median Blurring
4. Bilateral Blurring


<br><br><br><br>

<b> Usage: </b>
<br><br>
<b> General: </b> ```python3 blur.py --path ../lena.jpg --method average --kernel 7 --diameter 11 --colour 61 --space 39```


<b> Specific Method: </b>
- Average Blurring: ```python3 blur.py --path ../lena.jpg --method average --kernel 7``` <br>
![alt text](https://github.com/rohan1198/Computer-Vision-Projects/blob/main/04_image_blurring/assets/avg_blur.png)


<br><br>
- Gaussian Blurring: ```python3 blur.py --path ../lena.jpg --method gaussian --kernel 7``` <br>
![alt text](https://github.com/rohan1198/Computer-Vision-Projects/blob/main/04_image_blurring/assets/gaus_blur.png)


<br><br>
- Median Blurring: ```python3 blur.py --path ../lena.jpg --method median --kernel 7``` <br>
![alt text](https://github.com/rohan1198/Computer-Vision-Projects/blob/main/04_image_blurring/assets/med_blur.png)


<br><br>
- Bilateral Blurring: ```python3 blur.py --path ../lena.jpg --method bilateral --diameter 11 --colour 61 --space 39``` <br>
![alt text](https://github.com/rohan1198/Computer-Vision-Projects/blob/main/04_image_blurring/assets/avg_blur.png)
