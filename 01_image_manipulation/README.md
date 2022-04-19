<h2> Basic Image Manipulation: </h2>

1. Scaling
2. Rotation
3. Translation
4. Cropping


<br><br><br><br>

Usage: 

<b> General </b>: python3 manipulation.py --img ../lena.jpg --transform crop --dim 100 --angle 45 --translate 10 40 --crop-x 0 400 --crop-y 0 400


<b> Operation specific </b>:
- Scaling: python3 manipulation.py --img ../lena.jpg --transform scale --dim 100
<br><br>
- Rotation: python3 manipulation.py --img ../lena.jpg --transform rotate --angle 45
<br><br>
- Translation: python3 manipulation.py --img ../lena.jpg --transform translate --translate 10 40
<br><br>
- Cropping: python3 manipulation.py --img ../lena.jpg --transform crop --crop-x 0 400 --crop-y 0 400
