import moviepy.editor as mp

def convert_video_to_gif(video_file_path, fps):
    
    original_fileName = video_file_path.split('.')[0]
    
    video_clip = mp.VideoFileClip(video_file_path)
    gif_clip = video_clip.set_duration(video_clip.duration)
    
    output_file_path = original_fileName + '.gif'
    gif_clip.write_gif(output_file_path, fps=fps)

if __name__ == "__main__":
    
    fileIn = '2023-05-14 10-21-34_cropped.mp4'
    fps = 30
    
    convert_video_to_gif(fileIn, fps)
