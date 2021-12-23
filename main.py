from PIL import Image
import numpy as np
from matplotlib import cm, pyplot as plt
import random

filename = 'tree1.jpg'
im = Image.open(filename).convert('L')

im = np.asarray(im)
im = im/255

# plt.imshow(im, cmap='gray')
# plt.show()

convo = (4, 2)

s = ''
index = 0
word = 'STEM'
for i in range(0, im.shape[0], convo[0]):
  for j in range(0, im.shape[1], convo[1]):
    piece = im[i: i + convo[0], j : j + convo[1]]
    size = piece.shape[0] * piece.shape[1]
    s += word[index] if piece.sum() <= size / 2 else ':'
    index = 0 if index + 1 == len(word) else index + 1
  s += '\n'

with open('result.txt', 'w') as f:
  f.write(s)