import tkinter as tk
import fnmatch
import os
from tkinter import font
from pygame import mixer

root = tk.Tk()
root.title("Music App")
root.geometry("600x800")
root.config(background='black')
rootpath = r"C:\Users\lenovo\Music"
mixer.init()

def selected():
    selected_index = listBox.curselection()
    if not selected_index: 
        selected_index = (0,)
        listBox.activate(selected_index)
        listBox.select_set(selected_index)
    selected_song = listBox.get(selected_index)
    label.config(text=selected_song)
    mixer.music.load(os.path.join(rootpath, selected_song))
    mixer.music.play()
def stop():
    mixer.music.stop()
    listBox.select_clear("active")
def prev():
    selected_index=listBox.curselection()
    if selected_index:
        prev_song_index=selected_index[0]-1
        if prev_song_index<0:
            prev_song_index=listBox.size()-1
        prev_song_name = listBox.get(prev_song_index)
        label.config(text=prev_song_name)
        mixer.music.load(os.path.join(rootpath, prev_song_name))
        mixer.music.play()
        listBox.select_clear(0, 'end')
        listBox.activate(prev_song_index)
        listBox.select_set(prev_song_index)
def next():
    selected_index = listBox.curselection()
    if selected_index:
        next_song_index = selected_index[0] + 1
        if next_song_index < listBox.size():
            next_song_name = listBox.get(next_song_index)
        else:
            next_song_name = listBox.get(0)  
            next_song_index = 0 
        label.config(text=next_song_name)
        mixer.music.load(os.path.join(rootpath, next_song_name))
        mixer.music.play()
        listBox.select_clear(0, 'end')
        listBox.activate(next_song_index)
        listBox.select_set(next_song_index)
def pause():
    if pausebutton["text"] == "Pause":
        mixer.music.pause()
        pausebutton['text'] = "UnPause"
    else:
        mixer.music.unpause()
        pausebutton['text'] = "Pause"

listbox_font = font.Font(size=12)
listBox = tk.Listbox(root, fg="cyan", background="black", width=100, font=listbox_font)
listBox.pack(padx=15, pady=15)
label = tk.Label(root, text='', background='black', fg='yellow', font=listbox_font)
label.pack(pady=15)
frame = tk.Frame(root, bg="black")
frame.pack(padx=10, pady=5, anchor="center")

prevbutton = tk.Button(root, text="Prev", bg='green', fg='black', borderwidth=0, width=15, height=2,border=1,command=prev)
prevbutton.pack(pady=15, in_=frame, side='left')
stopbutton = tk.Button(root, text="Stop", bg='red', fg='black', borderwidth=0, width=15, height=2,border=1,command=stop)
stopbutton.pack(pady=15, in_=frame, side='left')
playbutton = tk.Button(root, text="Play", bg='orange', fg='black', borderwidth=0, width=15, height=2,border=1,command=selected)
playbutton.pack(pady=15, in_=frame, side='left')
nextbutton = tk.Button(root, text="Next", bg='yellow', fg='black', borderwidth=0, width=15, height=2,border=1,command=next)
nextbutton.pack(pady=15, in_=frame, side='left')
pausebutton = tk.Button(root, text="Pause", bg='cyan', fg='black', borderwidth=0, width=15, height=2,border=1,command=pause)
pausebutton.pack(pady=15, in_=frame, side='left')

for dirpath, dirnames, filenames in os.walk(rootpath):
    for filename in fnmatch.filter(filenames, "*.mp3"):
        listBox.insert('end', filename)

root.mainloop()