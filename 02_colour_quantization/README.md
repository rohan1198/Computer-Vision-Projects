<h2> Colour Quantization: </h2>


- Reduce the distinct colours in a given image while preserving the overall appearance.
<br><br>
- Here, the K-Means algorithm is used to group similar pixels, after which the number of colours are reduced explicitly.


- Colour conversion from RGB to LAB is carried out beacuse, in the LAB colour space, the euclidean distance (which is used in K-means) between colours has actual perceptual meaning.

<br><br><br><br>

<b> Usage: </b> <br><br>
For Images: python3 image_quantization.py --path ../lena.jpg --levels 4
<br>
For Videos: python3 video_quantization.py --path ../demo.mp4 --levels 4