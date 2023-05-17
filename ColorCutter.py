import os
from PIL import Image
from loading import progress_bar

def replace_pixels_with_transparency(fileIn, color=(0, 0, 0), color_similarity=0.1):
    origin = fileIn.split('--')[0]
    output_directory = origin + '_transparent--frames'
    os.makedirs(output_directory, exist_ok=True)

    files = os.listdir(fileIn)
    total_files = len(files)

    for i, filename in enumerate(files, start=1):
        progress_bar(i, total_files, prefix=f'Processing frames ({i}/{total_files}):')
        filepath_in = os.path.join(fileIn, filename)
        filepath_out = os.path.join(output_directory, filename)

        image = Image.open(filepath_in).convert('RGBA')
        width, height = image.size
        pixels = image.load()

        for x in range(width):
            for y in range(height):
                r, g, b, a = pixels[x, y]

                if calculate_color_similarity((r, g, b), color) > color_similarity:
                    # Replace non-similar color with transparency
                    pixels[x, y] = (r, g, b, 0)

        image.save(filepath_out)

def calculate_color_similarity(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2

    distance = ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5
    similarity = distance / (255 * (3 ** 0.5))
    return similarity

# Example usage

if __name__ == '__main__':

    fileIn = '2023-05-14 10-21-34_cropped_resized--frames'
    color = (249, 107, 75)
    color_similarity = 0.5
    
    
    replace_pixels_with_transparency(fileIn, color, color_similarity)
