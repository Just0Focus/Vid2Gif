import moviepy.editor as mp

def crop_video(video_file_path, resolution, center):
    
    original_filename = video_file_path.split('.')[0]
    
    # Load the video clip
    video_clip = mp.VideoFileClip(video_file_path)

    # Calculate the coordinates for cropping
    width, height = resolution
    x, y = center
    x1 = int(x - width / 2)
    y1 = int(y - height / 2)
    x2 = int(x + width / 2)
    y2 = int(y + height / 2)

    # Crop the video clip
    cropped_clip = video_clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)

    # Save the cropped video to the output file
    cropped_clip.write_videofile(original_filename + '_cropped.mp4')

    # Close the video clip
    video_clip.close()

if __name__ == '__main__':
    
    fileIn = '2023-05-14 10-21-34.mp4'
    resolution = (300, 300)
    center = (640, 360)
    # (1280x720)
    
    crop_video(fileIn, resolution, center)
