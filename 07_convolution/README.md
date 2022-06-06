<h2> Convolution </h2>

General purpose image filtering.

<br><br><br><br>

<b> Usage: </b>
<br><br>
<b> General: </b> ```python3 main.py --path lena.jpg --kernel sharpen --stride 1 1 --padding 1 1 --dilation 1 1```


<b> Specific Filtering Operations: </b>
<br><br>
<b> Identity: </b> ```python3 main.py --path lena.jpg --kernel identity```

<br><br>
<b> 3x3 Gaussian Blurring: </b> ```python3 main.py --path lena.jpg --kernel blur3```

<br><br>
<b> 5x5 Gaussian Blurring: </b> ```python3 main.py --path lena.jpg --kernel blur5```

<br><br>
<b> Sharpen: </b> ```python3 main.py --path lena.jpg --kernel sharpen```

<br><br>
<b> Outline: </b> ```python3 main.py --path lena.jpg --kernel outline```

<br><br>
<b> Unsharp: </b> ```python3 main.py --path lena.jpg --kernel unsharp```

<br><br>
<b> Changing stride: </b> ```python3 main.py --path lena.jpg --kernel blur3 --stride 1 2```
