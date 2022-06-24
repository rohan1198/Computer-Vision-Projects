<h2> Camera Calibration using OpenCV </h2>

Extract the intrinsic and extrinsic properties of the camera, and undistort images.

<br><br><br><br>

<b> Usage: </b>
<br><br>

<b> Get the calibration parameters: </b>
<br>```python calibrate.py --path images/low_resolution --res low --vis --save-params --save-vis```
![alt text](https://github.com/rohan1198/Image-Processing-Projects/blob/main/08_camera_calibration/corners.png)
<br><br>


<br><br><br>

<b> Undistort images: </b>
<br>```python inference.py --path low_res_test.jpg --params params.json --vis --save```

![alt text](https://github.com/rohan1198/Image-Processing-Projects/blob/main/08_camera_calibration/low_res_test.jpg) 
![alt text](https://github.com/rohan1198/Image-Processing-Projects/blob/main/08_camera_calibration/output.jpg)


<br><br><br><br>
Reference: https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html#calibration
