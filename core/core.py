import json
from PIL import Image
import customtkinter as ctk

def getMan():
    with open("manifest.json", "r") as mf:
        return json.load(mf)

def getImg(size, pathToImg, darkPathToImg=None):
    img = Image.open(pathToImg)
    if darkPathToImg is None:
        return ctk.CTkImage(light_image=img, dark_image=img, size=size)
    else:
        return ctk.CTkImage(light_image=img, dark_image=Image.open(darkPathToImg), size=size)