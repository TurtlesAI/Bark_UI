import tkinter as tk
from tkinter import filedialog
import webbrowser
import bark
from bark import SAMPLE_RATE, generate_audio
from scipy.io.wavfile import write as write_wav
import simpleaudio as sa
import numpy as np

def play_audio(file):
    wave_obj = sa.WaveObject.from_wave_file(file)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def save_audio():
    text = entry.get()
    if text:
        file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
        if file:
            audio = bark.generate_audio(text)
            
            # Convert the audio data to 16-bit integer format
            audio = (audio * np.iinfo(np.int16).max).astype(np.int16)
            
            write_wav(file, SAMPLE_RATE, audio)
            play_audio(file)

def open_website(event):
    webbrowser.open("https://www.turtlesai.com")

root = tk.Tk()
root.title("Bark Audio Generator")

# Create a canvas to display the image
canvas = tk.Canvas(root, width=150, height=150)
canvas.pack()

# Load the image using the tkinter.PhotoImage class
image = tk.PhotoImage(file="turtle.gif")

# Keep a reference to the image object to prevent it from being garbage collected
canvas.image = image

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=image)

label = tk.Label(root, text="Enter text to generate audio:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Generate and Save Audio", command=save_audio)
button.pack()

website_label = tk.Label(root, text="UI by DukeRem - https://www.turtlesai.com", fg="blue", cursor="hand2")
website_label.pack()
website_label.bind("<Button-1>", open_website)

root.mainloop()