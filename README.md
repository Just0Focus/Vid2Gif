# Vid2Gif

Vid2Gif is a collection of scripts for processing video files and converting them into GIFs. Each script serves a specific purpose and can be used independently or in combination with other scripts.

## VidInfo.py

This script prints information about a video file, including its name, size, duration, resolution, frame rate, creation date, and modification date.

### Attributes
- `video_file_path`: The path to the video file to be processed.

## CropVid.py

CropVid.py allows you to crop a video by specifying the desired resolution and center coordinates. The cropped video is saved as a new file.

### Attributes
- `video_file_path`: The path to the video file to be processed.
- `resolution`: The resolution of the cropped video.
- `center`: The center coordinates of the cropped video.
- `output_file_path`: The path to save the output file.

## FrameCrop.py

This script saves an original and cropped image of the first frame of a video. It helps visualize the cropping operation.

### Attributes
- `video_file_path`: The path to the video file to be processed.
- `resolution`: The resolution of the cropped video.
- `center`: The center coordinates of the cropped video.

## GUI-VidFrameCrop.py

GUI-VidFrameCrop.py provides a simple graphical user interface (GUI) window for running FrameCrop.py and previewing the cropping results.

## v2g.py

v2g.py converts a video file into a GIF. You can specify the dots per inch (dpi), frames per second (fps), and the path to save the output file.

### Attributes
- `video_file_path`: The path to the video file to be processed.
- `dpi`: The dots per inch of the output GIF.
- `fps`: The frames per second of the output GIF.
- `output_file_path`: The path to save the output file.

## GifSplitter.py

GifSplitter.py splits a GIF file into individual PNG frames and saves them in a directory. The output directory will have the same name as the original file with "_frames" appended.

### Attributes
- `fileIn`: The path to the GIF file to be processed.
- `fileOut`: The directory to save the frames (default: `<original_filename>_frames`).

## ResizePNGs.py

ResizePNGs.py resizes all the PNG files within a directory and saves them in a new directory. You can specify the resolution of the output PNG files.

### Attributes
- `fileIn`: The directory containing the PNG files to be processed.
- `resolution`: The resolution of the output PNG files (default: 300x300).
- `fileOut`: The directory to save the output PNG files (default: `<original_filename>_resized_frames`).

## ColorReplacer.py

ColorReplacer.py replaces pixels in each file within a directory that are similar to a specific color with transparency. This script is useful for cutting out multiple colors.

### Attributes
- `fileIn`: The directory containing the frames to be processed.
- `color`: The color to be replaced (default: black).
- `color_similarity`: The similarity of the color to be replaced.

## ColorCutter.py

ColorCutter.py replaces pixels in each file within a directory that are not similar to a specific color with transparency. This script is useful for cutting out a specific color.

### Attributes
- `fileIn`: The directory containing the PNG files to be processed.
- `color`: The color not to be replaced (default: black).
- `color_similarity`: The similarity of the color not to be replaced (default: 0.1).

## GifRebuilder.py

GifRebuilder.py creates a GIF from sequenced PNG frames within a given directory. Each frame is transparent, and frames do not stack on top of each other. You can specify the frames per second (fps), number of loop cycles, starting frame, and ending frame.

### Attributes
- `fileIn`: The directory containing the frames to be processed.
- `fps`: The frames per second of the output GIF (default: 30).
- `loop`: The number of times the GIF should loop (default: 0).
- `start`: The frame number to start the GIF from (default: 0).
- `end`: The frame number to end the GIF at (default: -1, end of the sequence).

## loading.py

loading.py is a module used by some of the scripts to display a progress bar in the terminal. It accepts the following arguments:

### Arguments
- `current`: The current progress.
- `total`: The total progress.
- `prefix`: The prefix to be displayed before the progress bar.

Example:
```
Progress: 39 / 100 |⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛| 39.0%
```