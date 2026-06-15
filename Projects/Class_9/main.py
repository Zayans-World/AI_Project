import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    """Utility function to display an image."""
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    """Interactive activity for edge detection."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return
    
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", grayscale_image)

    print("Select an option: ")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            sobel_x = cv2.Sobel(grayscale_image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(grayscale_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
            display_image("Sobel Edge Detection", combined_sobel)

        elif choice == '2':
            print("Adjust the thresholds for Canny Edge Detection(default: 100, 200 ).")
            lower_thresh = int(input("Enter lower threshold: "))
            upper_thresh = int(input("Enter upper threshold: "))
            canny_edges = cv2.Canny(grayscale_image, lower_thresh, upper_thresh)
            display_image("Canny Edge Detection", canny_edges)

        elif choice == '3':
            laplacian = cv2.Laplacian(grayscale_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))

        elif choice == '4':
            print("Adjust the kernel size for Gaussian Smoothing (must be odd).")
            kernel_size = int(input("Enter kernel size (e.g., 3, 5, 7): "))
            
            blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
            display_image("Gaussian Smoothed Image", blurred)

        elif choice == '5':
            print("Adjust the kernel size for Median Filtering (must be odd, Default: 5).")
            kernel_size = int(input("Enter kernel size (e.g., 3, 5, 7): "))
            median_filtered = cv2.medianBlur(image, kernel_size)
            display_image("Median Filtered Image", median_filtered)

        elif choice == '6':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

interactive_edge_detection("image.png")  # Replace with your image path