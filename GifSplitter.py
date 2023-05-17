from PIL import Image
import os
from loading import progress_bar

def gif_splitter(fileIn, fileOut=None):
    gif = Image.open(fileIn)
    frames_directory = os.path.splitext(fileIn)[0] + '--frames'

    if fileOut is not None:
        frames_directory = fileOut

    if not os.path.exists(frames_directory):
        os.makedirs(frames_directory)

    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_file_path = os.path.join(frames_directory, f"frame_{frame}.png")
        gif.save(frame_file_path, 'PNG')
        progress_bar(frame + 1, gif.n_frames, prefix=f'Saving frames ({frame + 1}/{gif.n_frames}): ')

# Example usage
if __name__ == '__main__':
    fileIn = 'GlitchNado.gif'
    gif_splitter(fileIn)
