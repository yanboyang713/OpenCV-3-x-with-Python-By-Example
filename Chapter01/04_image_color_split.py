import cv2

print ([x for x in dir(cv2) if x.startswith ('COLOR_')])

img = cv2.imread('./images/input.jpg', cv2.IMREAD_COLOR)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

'''
#slow method
y,u,v = cv2.split(yuv_img)

cv2.imshow('Grayscale image', gray_img)
cv2.imshow('Y channel', y)
cv2.imshow('U channel', u)
cv2.imshow('V channel', v)
'''

# faster way
cv2.imshow('Grayscale image', gray_img)
cv2.imshow('Y channel', yuv_img[:, :, 0])
cv2.imshow('U channel', yuv_img[:, :, 1])
cv2.imshow('V channel', yuv_img[:, :, 2])
cv2.waitKey()
