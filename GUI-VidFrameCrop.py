import cv2
import tkinter as tk
from PIL import ImageTk, Image
from FrameCrop import crop_video_frame

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Frame Crop")
        self.video_file_path = '2023-05-14 10-21-34.mp4'
        self.resolution = (640, 480)
        self.center = (640, 360)

        self.center_x_label = tk.Label(self.master, text="Center X:")
        self.center_x_label.pack()
        self.center_x_entry = tk.Entry(self.master)
        self.center_x_entry.insert(tk.END, str(self.center[0]))
        self.center_x_entry.pack()

        self.center_y_label = tk.Label(self.master, text="Center Y:")
        self.center_y_label.pack()
        self.center_y_entry = tk.Entry(self.master)
        self.center_y_entry.insert(tk.END, str(self.center[1]))
        self.center_y_entry.pack()

        self.width_label = tk.Label(self.master, text="Width:")
        self.width_label.pack()
        self.width_entry = tk.Entry(self.master)
        self.width_entry.insert(tk.END, str(self.resolution[0]))
        self.width_entry.pack()

        self.height_label = tk.Label(self.master, text="Height:")
        self.height_label.pack()
        self.height_entry = tk.Entry(self.master)
        self.height_entry.insert(tk.END, str(self.resolution[1]))
        self.height_entry.pack()

        self.frame_label = tk.Label(self.master)
        self.frame_label.pack()

        self.crop_button = tk.Button(self.master, text="Crop Frame", command=self.crop_frame)
        self.crop_button.pack()

    def crop_frame(self):
        center_x = int(self.center_x_entry.get())
        center_y = int(self.center_y_entry.get())
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())

        self.center = (center_x, center_y)
        self.resolution = (width, height)

        cropped_frame = crop_video_frame(self.video_file_path, self.resolution, self.center)

        if cropped_frame is not None:
            # Display the cropped frame image
            image = Image.fromarray(cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB))
            image = image.resize((640, 480), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.frame_label.config(image=photo)
            self.frame_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
