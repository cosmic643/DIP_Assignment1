'''
This program is for bit-plane slicing
and shows all the bit planes
Authors: Vaibhav Khamesra - 21UCS224
         Shreyas Acharya - 21UCS200
         Divyansh Garg - 21DCS003
'''

import cv2
import numpy as np
def decimal_to_binary(n):
    return format(n,'08b')
img = cv2.imread('lena_color.tif',0)
if img is None:
    print("Image Loading Failed")
    exit(0)
height,width = img.shape
eight_bit_plane = np.zeros((height,width))
seven_bit_plane = np.zeros((height,width))
six_bit_plane = np.zeros((height,width))
five_bit_plane = np.zeros((height,width))
four_bit_plane = np.zeros((height,width))
three_bit_plane = np.zeros((height,width))
two_bit_plane = np.zeros((height,width))
one_bit_plane = np.zeros((height,width))

for i in range(height):
    for j in range(width):
        binary_value = decimal_to_binary(img[i][j])
        eight_bit_plane[i][j] = int(binary_value[0])
        seven_bit_plane[i][j] = int(binary_value[1])
        six_bit_plane[i][j] = int(binary_value[2])
        five_bit_plane[i][j] = int(binary_value[3])
        four_bit_plane[i][j] = int(binary_value[4])
        three_bit_plane[i][j] = int(binary_value[5])
        two_bit_plane[i][j] = int(binary_value[6])
        one_bit_plane[i][j] = int(binary_value[7])

img_one = np.zeros((height,width))
img_two = np.zeros((height,width))
img_three = np.zeros((height,width))
img_four = np.zeros((height,width))
img_five = np.zeros((height,width))
img_six = np.zeros((height,width))
img_seven = np.zeros((height,width))
img_eight = np.zeros((height,width))

for i in range(height):
    for j in range(width):
        img_eight[i][j] = eight_bit_plane[i][j]*128
        img_seven[i][j] = seven_bit_plane[i][j]*64
        img_six[i][j] = six_bit_plane[i][j]*32
        img_five[i][j] = five_bit_plane[i][j]*16
        img_four[i][j] = four_bit_plane[i][j]*8
        img_three[i][j] = three_bit_plane[i][j]*4
        img_two[i][j] = two_bit_plane[i][j]*2
        img_one[i][j] = one_bit_plane[i][j]*1


img_one = img_one.astype(np.uint8)
img_two = img_two.astype(np.uint8)
img_three = img_three.astype(np.uint8)
img_four = img_four.astype(np.uint8)
img_five = img_five.astype(np.uint8)
img_six = img_six.astype(np.uint8)
img_seven = img_seven.astype(np.uint8)
img_eight = img_eight.astype(np.uint8)

cv2.namedWindow("8 bit plane",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("7 bit plane",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("6 bit plane",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("5 bit plane",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("4 bit plane",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("3 bit plane",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("2 bit plane",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("1 bit plane",cv2.WINDOW_AUTOSIZE)

cv2.imshow("8 bit plane",img_eight)
cv2.imshow("7 bit plane",img_seven)
cv2.imshow("6 bit plane",img_six)
cv2.imshow("5 bit plane",img_five)
cv2.imshow("4 bit plane",img_four)
cv2.imshow("3 bit plane",img_three)
cv2.imshow("2 bit plane",img_two)
cv2.imshow("1 bit plane",img_one)

cv2.waitKey(0)
cv2.destroyAllWindows()