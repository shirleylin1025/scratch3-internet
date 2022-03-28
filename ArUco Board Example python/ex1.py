# -*- coding: utf-8 -*-


import numpy as np
import cv2, PIL
import cv2.aruco as ar
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd


aruco_dict = ar.Dictionary_get(ar.DICT_6X6_250)

fig = plt.figure()
nx = 4
ny = 3
for i in range(1, nx*ny+1):
    ax = fig.add_subplot(ny,nx, i)
    img = ar.drawMarker(aruco_dict,i, 700)
    plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
    ax.axis("off")

plt.savefig("markers.pdf")
plt.show()