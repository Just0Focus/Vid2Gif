import os
import datetime
from moviepy.editor import VideoFileClip

def get_video_info(video_file_path):
    video = VideoFileClip(video_file_path)

    # Video file name
    file_name = os.path.basename(video_file_path)

    # Video file size
    file_size = os.path.getsize(video_file_path)

    # Video file duration
    duration = video.duration

    # Video file resolution
    resolution = f"{video.size[0]}x{video.size[1]}"

    # Video file frame rate
    frame_rate = video.fps

    # Video file creation date
    creation_date = datetime.datetime.fromtimestamp(os.path.getctime(video_file_path))

    # Video file modification date
    modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(video_file_path))

    video.close()

    return {
        "File Name": file_name,
        "File Size": file_size,
        "Duration": duration,
        "Resolution": resolution,
        "Frame Rate": frame_rate,
        "Creation Date": creation_date,
        "Modification Date": modification_date
    }

if __name__ == "__main__":
    fileIn = '2023-05-14 10-21-34_cropped.mp4'

    video_info = get_video_info(fileIn)

    print("Video Information:")
    for key, value in video_info.items():
        if isinstance(value, datetime.datetime):
            value = value.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{key}: {value}")
