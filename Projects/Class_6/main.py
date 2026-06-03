import cv2
image = cv2.imread('image.png')
cv2.namedWindow('Loaded image', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Loaded image', 800, 500)
cv2.imshow('Loaded image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"Image Dimensions: {image.shape}")