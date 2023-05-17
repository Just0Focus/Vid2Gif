import glob
import imageio
from loading import progress_bar

def create_transparent_video(fileIn, fps=30, start=0, end=-1):
    # Get the list of PNG files in the directory
    frames = sorted(glob.glob(f"{fileIn}/*.png"))

    # Apply start and end frame numbers
    frames = frames[start:end]

    # Create the output file name
    origin = fileIn.split('_')[0] + '_' + fileIn.split('_')[1]
    fileOut = origin + '.mp4'

    # Read the first frame to get the dimensions
    first_frame = imageio.imread(frames[0])
    height, width, _ = first_frame.shape

    # Create the VideoWriter with VP9 codec and a transparent color mode
    writer = imageio.get_writer(fileOut, format='FFmpeg', mode='I', codec='libvpx-vp9',
                                output_params=['-pix_fmt', 'yuva420p'])

    total_frames = len(frames)
    for i, frame in enumerate(frames):4
        image = imageio.imread(frame)

        # Add the frame to the video writer
        writer.append_data(image)

        progress_bar(i + 1, total_frames, prefix='Creating Video')

    writer.close()
    print(f"Transparent video created successfully: {fileOut}")

# Example usage
fileIn = '2023-05-14 10-21-34_cropped--transparent_frames'
create_transparent_video(fileIn, fps=30, start=0, end=-1)
