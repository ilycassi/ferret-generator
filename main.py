import tkinter
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pyperclip

url = "https://ferrets.leodog896.com/v1/image/random"

def img_from_url():
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((720, 720))
    return img
root = tkinter.Tk()
root.configure(bg="black")
root.title("ferret generator")
root.geometry("720x720")
root.resizable(False, False)
def set_image():
    ferret_image=ImageTk.PhotoImage(img_from_url())
    label.configure(image=ferret_image)
    label.image=ferret_image
button=ttk.Button(root,text="copy link",command=pyperclip.copy(url))
button.pack(side="bottom",padx=10,pady=10)
button=ttk.Button(root,text="click me",command=set_image)
button.pack(side="bottom",padx=10,pady=10)
ferret_image=ImageTk.PhotoImage(img_from_url())
label = ttk.Label(root, image=ferret_image)
label.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

root.mainloop()