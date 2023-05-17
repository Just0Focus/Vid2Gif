import cv2

def enhance_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Apply the bilateral filter to enhance edges
    enhanced = cv2.bilateralFilter(image, 9, 75, 75)
    
    # Display the original and enhanced images
    cv2.imshow('Original Image', image)
    cv2.imshow('Enhanced Image', enhanced)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save the enhanced image
    cv2.imwrite('enhanced_image.png', enhanced)

# Example usage
if __name__ == '__main__':
    
    # Specify the path to your image
    file = 'frame_0.png'
    dir = '2023-05-14 10-21-34_cropped--frames'
    
    image_path = dir + '/' + file

    # Call the function to enhance the image
    enhance_image(image_path)
