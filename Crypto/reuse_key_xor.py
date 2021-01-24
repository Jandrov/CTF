from pwn import xor
import sys


key = np.load('key.npy')
secret = plt.imread('secret.bmp')

newArr = np.logical_xor(key, secret)
plt.imshow(newArr)