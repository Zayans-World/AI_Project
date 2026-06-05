import cv2

image = cv2.imread('image.png')

if image is None:
    print("Error: Image not found!")
    exit()


sizes = [
    (100, 100),
    (224, 224),
    (500, 500)
]


for i, size in enumerate(sizes, start=1):
    resized_image = cv2.resize(image, size)

 

    cv2.imshow(f'Resized Image {size}', resized_image)

    filename = f'resized_image_{i}.png'
    cv2.imwrite(filename, resized_image)

    print(f"Saved: {filename}")
    print(f"Dimensions: {resized_image.shape}")

cv2.waitKey(0)
cv2.destroyAllWindows()