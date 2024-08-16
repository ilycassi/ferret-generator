import tkinter
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pyperclip

url = "https://ferrets.leodog896.com/v1/data/random"
baseurl = "https://ferrets.leodog896.com"
currenturl = ""

def img_from_url():
    response = requests.get(url)
    imageurl=baseurl+response.json()['url']
    print(imageurl)
    global currenturl
    currenturl = str (imageurl)
    print (currenturl)
    imagedata = requests.get(str (imageurl))
    img = Image.open(BytesIO(imagedata.content))
    img = img.resize((720, 720))
    return img
def copy_link():
    global currenturl
    pyperclip.copy(currenturl)
root = tkinter.Tk()
root.configure(bg="black")
root.title("ferret generator")
root.geometry("720x720")
root.resizable(False, False)
def set_image():
    ferret_image=ImageTk.PhotoImage(img_from_url())
    label.configure(image=ferret_image)
    label.image=ferret_image
button=ttk.Button(root,text="copy link",command=copy_link)
button.pack(side="bottom",padx=10,pady=10)
button=ttk.Button(root,text="click me",command=set_image)
button.pack(side="bottom",padx=10,pady=10)
ferret_image=ImageTk.PhotoImage(img_from_url())
label = ttk.Label(root, image=ferret_image)
label.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

root.mainloop()