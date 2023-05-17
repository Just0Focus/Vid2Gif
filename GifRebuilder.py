import os
import re
from PIL import Image
from loading import progress_bar

def extract_number(filename):
    # Extract the numeric part of the filename and convert it to an integer
    match = re.search(r'(\d+)', filename)
    if match:
        return int(match.group(1))
    return filename

def create_gif(fileIn, fileOut, fps=30, loop=0, start=0, end=-1):
    files = sorted(os.listdir(fileIn), key=extract_number)
    
    frames = []

    # If end is -1, process all frames
    if end == -1:
        end = len(files)

    for i, file in enumerate(files[start:end]):
        # Only process .png files
        if file.endswith('.png'):
            frame = Image.open(os.path.join(fileIn, file))
            frames.append(frame.convert('RGBA'))
            progress_bar(i + 1, end-start, prefix=f'Processing frames ({i + 1}/{end-start}): ')

    # Save frames as gif
    frames[0].save(fileOut, format='GIF',
                   append_images=[frame.copy() for frame in frames[1:]],
                   save_all=True,
                   duration=1000/fps, loop=loop,
                   disposal=2)  # Clear the frame before rendering the next one
    print(f'GIF saved as {fileOut}')

if __name__ == '__main__':
    fileIn = 'GlitchNado_transparent--frames'
    origin = fileIn.split('--')[0]
    fileOut = origin + '.gif'
    
    fps = 15 # 30 is default
    #loop = 6 # 0 = infinite
    #start = 0
    #end = -1
    
    create_gif(fileIn, fileOut, fps)
