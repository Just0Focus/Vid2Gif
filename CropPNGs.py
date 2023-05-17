import os
from PIL import Image
import sys

# Progress bar function
def progress_bar(current, total, prefix=''):
    length = 20
    filled_width = int(round(length * current / total))
    percentage = round(100.0 * current / total, 1)
    bar = '⬜' * filled_width + '⬛' * (length - filled_width)

    sys.stdout.write(f'\r{prefix} |{bar}| {percentage}%')
    sys.stdout.flush()

    if current == total:
        sys.stdout.write('\n')
        sys.stdout.flush()

# Function to crop/resize PNG files
def crop_png_files(fileIn, resolution=(300, 300), center=(960, 540), fileOut=None):
    if fileOut is None:
        origin = fileIn.split('--')[0]
        fileOut = origin + '_cropped--frames'

    # Create output directory if it doesn't exist
    os.makedirs(fileOut, exist_ok=True)

    # Get a list of all PNG files in the input directory
    png_files = [file for file in os.listdir(fileIn) if file.endswith('.png')]

    total_files = len(png_files)

    for i, file in enumerate(png_files):
        input_file = os.path.join(fileIn, file)
        output_file = os.path.join(fileOut, file)
        
        # Open the image
        image = Image.open(input_file)
        
        # Crop/resize the image
        cropped_image = image.crop((center[0]-resolution[0]/2, center[1]-resolution[1]/2,
                                    center[0]+resolution[0]/2, center[1]+resolution[1]/2))
        resized_image = cropped_image.resize(resolution, Image.ANTIALIAS)
        
        # Save the resized image
        resized_image.save(output_file, 'PNG')

        # Display progress
        progress_bar(i + 1, total_files, prefix='Processing files')

    print(f'Finished processing {total_files} files. Saved to {fileOut}')

# Example usage
if __name__ == '__main__':
    fileIn = 'Crown--frames'
    resolution = (250, 250)
    center = (250, 250)
    #fileOut = '/path/to/output_directory'
    crop_png_files(fileIn, resolution, center)
