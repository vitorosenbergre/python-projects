from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        ytube = YouTube(url)
        streams = ytube.streams.filter(progressive=True, file_extension="mp4")
        high_resolution = streams.get_highest_resolution()
        high_resolution.download(output_path=save_path)
        status_label.config(text="Download completed!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")


def open_file_dialog(entry):
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, tk.END)
        entry.insert(0, folder)
        status_label.config(text=f"Selected folder: {folder}", fg="blue")


def start_download(url_entry, save_entry):
    video_url = url_entry.get()
    save_dir = save_entry.get()

    if not save_dir:
        status_label.config(text="Invalid save location", fg="red")
    else:
        status_label.config(text="Started download...", fg="black")
        download_video(video_url, save_dir)


# GUI setup
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x200")

frame = tk.Frame(root, pady=10)
frame.pack()

url_label = tk.Label(frame, text="Enter YouTube URL:", font=("Helvetica", 12))
url_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

url_entry = tk.Entry(frame, width=30, font=("Helvetica", 12))
url_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

save_label = tk.Label(frame, text="Save Path:", font=("Helvetica", 12))
save_label.grid(row=1, column=0, pady=5, padx=10, sticky="w")

save_entry = tk.Entry(frame, width=30, font=("Helvetica", 12))
save_entry.grid(row=1, column=1, pady=5, padx=10, sticky="w")

browse_button = tk.Button(frame, text="Browse", command=lambda: open_file_dialog(
    save_entry), font=("Helvetica", 10))
browse_button.grid(row=2, column=1, pady=5, padx=10, sticky="w")

download_button = tk.Button(frame, text="Download", command=lambda: start_download(
    url_entry, save_entry), font=("Helvetica", 12))
download_button.grid(row=3, column=0, columnspan=2, pady=20)

status_label = tk.Label(root, text="", font=("Helvetica", 12))
status_label.pack()

root.mainloop()
