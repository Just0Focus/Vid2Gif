import cv2
import sys

def crop_video_frame(video_file_path, resolution, center):
    # Read the video file
    video = cv2.VideoCapture(video_file_path)

    # Check if video file is opened successfully
    if not video.isOpened():
        print("Error opening video file")
        return

    # Read the first frame
    ret, frame = video.read()

    if not ret:
        print("Error reading video frame")
        video.release()
        return

    # Calculate the coordinates for cropping
    x, y = center
    w = resolution[0] // 2
    h = resolution[1] // 2
    left = x - w
    right = x + w
    top = y - h
    bottom = y + h

    # Perform the cropping
    cropped_frame = frame[top:bottom, left:right]

    # Save the original and cropped frames
    cv2.imwrite("original_frame.jpg", frame)
    cv2.imwrite("cropped_frame.jpg", cropped_frame)

    # Release the video file and close windows
    video.release()
    cv2.destroyAllWindows()
    
    return cropped_frame

if __name__ == "__main__":
    
    video_file_path = '2023-05-14 10-21-34.mp4'
    resolution = (300, 300)
    center = (960, 540)

    # Call the crop_video_frame function with the provided arguments
    crop_video_frame(video_file_path, resolution, center)
