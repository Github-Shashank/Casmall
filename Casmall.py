import tkinter as tk
from tkinter import filedialog
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.withdraw()

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
d={'a': '🇦', 'b': '🇧', 'c': '🇨', 'd': '🇩', 'e': '🇪', 'f': '🇫', 'g': '🇬', 'h': '🇭', 'i': '🇮', 'j': '🇯', 'k': '🇰', 'l': '🇱', 'm': '🇲', 'n': '🇳', 'o': '🇴', 'p': '🇵', 'q': '🇶', 'r': '🇷', 's': '🇸', 't': '🇹', 'u': '🇺', 'v': '🇻', 'w': '🇼', 'x': '🇽', 'y': '🇾', 'z': '🇿'}

file_path = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
)

if file_path:
    print("You selected:", file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        a = content 

else:
    print("No file selected.")
    quit()

for i in range(len(a)):
    if a[i] == ' ':
        a=a[:i+1]+a[i+1].capitalize()+a[i+2:]
        
for i in l:
    a=a.replace(i,d[i])

save_path = filedialog.asksaveasfilename(
    defaultextension=".txt",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    title="Save your file as..."
)

if save_path:
    print("You chose to save the file at:", save_path)
    # Example: Write something to the file
    with open(save_path, "w") as file:
        file.write(a)
else:
    print("Save cancelled.")
