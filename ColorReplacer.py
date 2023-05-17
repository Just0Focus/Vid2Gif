import os
from PIL import Image
from loading import progress_bar

def replace_color_with_transparency(fileIn, color=(0, 0, 0), color_similarity=0):
    # Create output directory
    origin = fileIn.split('--')[0]
    output_directory = origin + '_transparent--frames'
    os.makedirs(output_directory, exist_ok=True)

    # Get a list of files in the input directory
    files = os.listdir(fileIn)

    # Iterate through each file
    total_files = len(files)
    for i, file_name in enumerate(files):
        file_path = os.path.join(fileIn, file_name)
        output_path = os.path.join(output_directory, file_name)

        # Open the image
        image = Image.open(file_path).convert("RGBA")
        pixels = image.load()

        # Iterate through each pixel and replace the specified color with transparency
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                r, g, b, a = pixels[x, y]
                if (r, g, b) == color or abs(r - color[0]) <= color_similarity and abs(g - color[1]) <= color_similarity and abs(b - color[2]) <= color_similarity:
                    pixels[x, y] = (r, g, b, 0)

        # Save the modified image with transparency
        image.save(output_path, "PNG")

        # Update the progress bar
        progress_bar(i + 1, total_files, prefix=f'Processing frames ({i + 1}/{total_files}): ')

    print(f"All frames processed. Transparent frames saved in: {output_directory}")

# Test the function
if __name__ == "__main__":
    fileIn = "Crown_cropped--frames"
    color = (177,188,179)
    # Set this to 0 to only replace the exact color
    color_similarity = 50
    
    replace_color_with_transparency(fileIn, color, color_similarity)
