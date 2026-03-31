import json
from PIL import Image
import customtkinter as ctk
from pathlib import Path
import tkinter as tk

BASE_DIR = Path(__file__).parent.absolute()

def log(txt, args):
    match args:
        case 0:print(f"[LOG] - {txt}")
        case 1: print(f"[WARNING] - {txt}")
        case 2: print(f"[ERROR] - {txt}\nCreate issule on github!")

def getMan():
    with open(f"{BASE_DIR}/manifest.json", "r") as mf:
        manf = json.load(mf)
        log(f"Manifest loaded:\n{manf}", 0)
        return manf

def getImg(size, pathToImg, darkPathToImg=None):
    log(f"Getting img ({pathToImg})", 0)
    img = Image.open(BASE_DIR / pathToImg)
    if darkPathToImg is None:
        return ctk.CTkImage(light_image=img, dark_image=img, size=size)
    else:
        return ctk.CTkImage(light_image=img, dark_image=Image.open(BASE_DIR / darkPathToImg), size=size)

def install(method, dir, args=None):
    match method:
        case 1: pass