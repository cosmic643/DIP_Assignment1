'''
This program scales up an image using Intepolation
scaling factor: 2
Authors: Vaibhav Khamesra - 21UCS224
         Shreyas Acharya - 21UCS200
         Divyansh Garg - 21DCS003

To exit the window press X on your keyboard
'''

import cv2
import numpy as np


cropping = False
img = cv2.imread("lena_color.tif")
if img is None:
    print("Image Loading Failed")
    exit(0)


height,width,colors = img.shape
scaled_up_img = np.zeros((2*height,2*width,colors))
for k in range(colors):
    for i in range(height):
        for j in range(width):
            if(i != height-1):
                if(j != width-1):
                    scaled_up_img[2*i][2*j][k] = img[i][j][k]
                    scaled_up_img[2*i + 1][2*j][k] = (img[i][j][k]/2 + img[i+1][j][k]/2)
                    scaled_up_img[2*i][2*j + 1][k] = (img[i][j][k]/2 + img[i][j+1][k]/2)
                    scaled_up_img[2*i + 1][2*j + 1][k] = (img[i][j][k]/4 + img[i+1][j][k]/4 + img[i][j+1][k]/4 + img[i+1][j+1][k]/4)
                else:
                    scaled_up_img[2*i][2*j][k] = img[i][j][k]
                    scaled_up_img[2*i + 1][2*j][k] = (img[i][j][k]/2 + img[i+1][j][k]/2)
                    scaled_up_img[2*i][2*j + 1][k] = (img[i][j][k]/2)
                    scaled_up_img[2*i + 1][2*j + 1][k] = (img[i][j][k]/4 + img[i+1][j][k]/4)
            else:
                if(j != width-1):
                    scaled_up_img[2*i][2*j][k] = img[i][j][k]
                    scaled_up_img[2*i + 1][2*j][k] = (img[i][j][k])/2
                    scaled_up_img[2*i][2*j + 1][k] = (img[i][j][k]/2 + img[i][j+1][k]/2)
                    scaled_up_img[2*i + 1][2*j + 1][k] = (img[i][j][k]/4 + img[i][j+1][k]/4)
                else:
                    scaled_up_img[2*i][2*j][k] = img[i][j][k]
                    scaled_up_img[2*i + 1][2*j][k] = (img[i][j][k])/2
                    scaled_up_img[2*i][2*j + 1][k] = (img[i][j][k])/2
                    scaled_up_img[2*i + 1][2*j + 1][k] = (img[i][j][k])/4

scaled_up_img = scaled_up_img.astype(np.uint8)

def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping

    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y

    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False  # cropping is finished

        cropped_coordinates = [(x_start, y_start), (x_end, y_end)]

        if len(cropped_coordinates) == 2:  # when two points were found
            roi = scaled_up_img[2*cropped_coordinates[0][1]:2*cropped_coordinates[1][1], 2*cropped_coordinates[0][0]:2*cropped_coordinates[1][0]]
            cv2.imshow("Cropped", roi)


cv2.namedWindow("Interpolation")
cv2.setMouseCallback("Interpolation", mouse_crop)

while True:

    i = img.copy()

    if not cropping:
        cv2.imshow("Interpolation", img)

    elif cropping:
        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
        cv2.imshow("Interpolation", i)
    k = cv2.waitKey(1) & 0xFF
    if(k == ord('x')):
        exit(0)
cv2.destroyAllWindows()