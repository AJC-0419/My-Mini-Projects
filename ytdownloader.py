from pytubefix import YouTube
import tkinter as tk
import os





def download_video():
    url = entry.get()
    if url:
        try:
           yt = YouTube(url)
           print(yt.title)
           stream = yt.streams.get_highest_resolution()
           print("Download completed!")
            
        except Exception as e:
            status.config(text=f"Error: {str(e)}", fg="red")
    else:
        status.config(text="Please enter a valid URL.", fg="red")


root = tk.Tk()
root.title("YouTube Video Downloader")
root.resizable(False, False)

Frame1 = tk.Frame(root, width=400, height=200)
label = tk.Label(Frame1, text="Enter YouTube URL:")
entry = tk.Entry(Frame1, width=40)
submit_button = tk.Button(Frame1, text="Download", command=download_video)
status = tk.Label(Frame1, text="", fg="green")
label.pack()
entry.pack(pady=10)
submit_button.pack()
status.pack(pady=10)

Frame1.pack(padx=10, pady=10)
root.mainloop()