'''
This program is for bit-plane slicing
1. 8th and 7th Bit
2. 8th, 7th and 6th Bit
3. 8th, 7th, 6th and 5th bit
Authors: Vaibhav Khamesra - 21UCS224
         Shreyas Acharya - 21UCS200
         Divyansh Garg - 21DCS003
'''

import cv2
import numpy as np
def decimal_to_binary(n):
    return format(n,'08b')
img = cv2.imread("lena_color.tif",0)
if img is None:
    print("Image Loading Failed")
    exit(0)
height,width = img.shape
eight_bit_plane = np.zeros((height,width))
seven_bit_plane = np.zeros((height,width))
six_bit_plane = np.zeros((height,width))
five_bit_plane = np.zeros((height,width))
for i in range(height):
    for j in range(width):
        binary_value = decimal_to_binary(img[i][j])
        eight_bit_plane[i][j] = int(binary_value[0])
        seven_bit_plane[i][j] = int(binary_value[1])
        six_bit_plane[i][j] = int(binary_value[2])
        five_bit_plane[i][j] = int(binary_value[3])
img_one = np.zeros((height,width))
img_two = np.zeros((height,width))
img_three = np.zeros((height,width))
for i in range(height):
    for j in range(width):
        img_one[i][j] = eight_bit_plane[i][j]*128 + seven_bit_plane[i][j]*64
        img_two[i][j] = eight_bit_plane[i][j]*128 + seven_bit_plane[i][j]*64 + six_bit_plane[i][j]*32
        img_three[i][j] = eight_bit_plane[i][j]*128 + seven_bit_plane[i][j]*64 + six_bit_plane[i][j]*32 + five_bit_plane[i][j]*16

img_one = img_one.astype(np.uint8)
img_two = img_two.astype(np.uint8)
img_three = img_three.astype(np.uint8)
cv2.namedWindow("8 and 7 bit plane",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("8 7 and 6 bit plane",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("8 7 6 and 5 bit plane",cv2.WINDOW_AUTOSIZE)
cv2.imshow("8 and 7 bit plane",img_one)
cv2.imshow("8 7 and 6 bit plane",img_two)
cv2.imshow("8 7 6 and 5 bit plane",img_three)
cv2.waitKey(0);
cv2.destroyAllWindows()