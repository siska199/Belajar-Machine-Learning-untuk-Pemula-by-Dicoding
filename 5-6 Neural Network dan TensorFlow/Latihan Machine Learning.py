# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:47:54 2021

@author: KyuuChan199
"""

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
print(tf.__version__)

(X_train, y_train), (X_test, y_test) = datasets.cifar10.load_data()
print(X_train.shape)
print(X_test.shape)

#Melihat data dalam bentuk matriks berupa matriks dengan ukuran 32 x 32:
print(X_train[0])

#melihat data dalam bentuk gambar:
plt.imshow(X_train[0])
#resize ukuran data
plt.figure(figsize = (15,2))
plt.imshow(X_train[0])

