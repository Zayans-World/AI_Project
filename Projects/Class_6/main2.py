import cv2
image = cv2.imread('image.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(gray_image, (224, 224))


cv2.imshow('Processed image', resized_image)

key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('grayimage.png', resized_image)
    print("Image saved as grayimage.png")
else:
    print("Image not saved")
cv2.destroyAllWindows()
print(f"Image Dimensions: {resized_image.shape}")