#!/usr/bin/env python3

import os
import numpy as np
import matplotlib.image as mpimg

images = [mpimg.imread(x) for x in os.listdir('./input') if x.endswith('.png')]

dims = [0, 0, 0]
for image in images:
    shape = image.shape
    for i in range(3):
        dims[i] = dims[i] if shape[i] < dims[i] else shape[i]

canvas = np.zeros(dims)
for image in images:
    shape = image.shape
    for index in np.ndindex(shape[0], shape[1]):
        canvas[index] = abs(canvas[index] - image[index])

mpimg.imsave('output.png', canvas)
