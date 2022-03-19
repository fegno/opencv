import cv2
# Reading the image using imread() function
image = cv2.imread('media/abhishek.jpeg')

# Extracting the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {},  Width = {}".format(h, w))


# Using 0 to read image in grayscale mode

img = cv2.imread(r'media/abhishek.jpeg', 0)


# We will calculate the region of interest
# by slicing the pixels of the image
region_of_interest = image[100:200, 300:500]


# display the image
cv2.imshow('image', img)
cv2.waitKey(0)

# and finally destroy/close all open windows
cv2.destroyAllWindows()