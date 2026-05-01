import os
import tkinter as tk
from PIL import Image, ImageTk

# -------- CONFIG --------
BASE_FOLDER = r"D:\yoloproject\testproj\read_folder2"

# -------- FIND IMAGES IN SUBFOLDER --------
def get_images(folder_path):
    files = os.listdir(folder_path)

    plate_img = None
    rider_img = None

    for f in files:
        if f.startswith("plate"):
            plate_img = os.path.join(folder_path, f)
        elif f.startswith("rider"):
            rider_img = os.path.join(folder_path, f)

    return plate_img, rider_img


# -------- OPEN WINDOW --------
def open_folder(folder_name):
    folder_path = os.path.join(BASE_FOLDER, folder_name)

    plate_path, rider_path = get_images(folder_path)

    if not plate_path or not rider_path:
        print("Missing images in", folder_name)
        return

    win = tk.Toplevel()
    win.title(folder_name)

    plate_img = Image.open(plate_path).resize((300, 150))
    rider_img = Image.open(rider_path).resize((300, 300))

    plate_photo = ImageTk.PhotoImage(plate_img)
    rider_photo = ImageTk.PhotoImage(rider_img)

    tk.Label(win, text="Plate").pack()
    tk.Label(win, image=plate_photo).pack()

    tk.Label(win, text="Rider").pack()
    tk.Label(win, image=rider_photo).pack()

    win.plate_photo = plate_photo
    win.rider_photo = rider_photo


# -------- MAIN UI --------
root = tk.Tk()
root.title("Plate Folders Viewer")

folders = [f for f in os.listdir(BASE_FOLDER)
           if os.path.isdir(os.path.join(BASE_FOLDER, f))]

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

for folder in folders:
    btn = tk.Button(
        frame,
        text=folder,
        width=30,
        command=lambda f=folder: open_folder(f)
    )
    btn.pack(pady=3)

root.mainloop()