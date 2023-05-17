import os
from PIL import Image
from loading import progress_bar

def resize_png_files(fileIn, resolution=(300, 300), fileOut=None):
    # Set default output directory
    if fileOut is None:
        origin = fileIn.split('--')[0]
        fileOut = f"{origin}_resized--frames"

    # Create output directory if it doesn't exist
    os.makedirs(fileOut, exist_ok=True)

    # Get the list of PNG files in the input directory
    png_files = [filename for filename in os.listdir(fileIn) if filename.lower().endswith('.png')]

    # Resize each PNG file
    total_files = len(png_files)
    for i, filename in enumerate(png_files):
        input_path = os.path.join(fileIn, filename)
        output_path = os.path.join(fileOut, filename)

        try:
            with Image.open(input_path) as img:
                img = img.resize(resolution, Image.ANTIALIAS)
                img.save(output_path, 'PNG')
        except IOError:
            print(f"Failed to resize {filename}")
        
        progress_bar(i + 1, total_files, prefix=f'Resizing frames ({i + 1}/{total_files}):')

    print("Resizing complete!")

# Usage example
if __name__ == '__main__':
    fileIn = '2023-05-14 10-21-34_cropped--frames'  # Replace with the actual input directory path
    resolution = (128, 128)  # Replace with the desired resolution
    fileOut = None  # Replace with the desired output directory path or leave as None for default
    
    resize_png_files(fileIn, resolution, fileOut)
