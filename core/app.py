import customtkinter as ctk
import tkinter as tk
import core

class TitleFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.iconLb = ctk.CTkLabel(
            self,
            text="",
            image=core.getImg((48, 48), master.man["Icon"])
        )
        self.iconLb.pack(side="left", padx=(15, 20), pady=15)

        self.nameLb = ctk.CTkLabel(
            self,
            text=master.man["Name"],
            fg_color="transparent",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.nameLb.pack(side="left", pady=15)

        self.button = ctk.CTkButton(
            self,
            text="Install",
            command=master.button_callbck,
            width=100
        )
        self.button.pack(side="right", padx=(20, 15), pady=15)

class DirFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.nameLb = ctk.CTkLabel(
            self,
            text=f"{master.man['Name']} - Dir",
            fg_color="transparent",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.nameLb.pack(side="top", pady=10)
        self.chose = ctk.CTkButton(self, text="Open", command=self.choseFile, width=50)
        self.chose.pack(side="left", padx=15)
        self.entryVar = tk.StringVar(value="C:/Program Files/")
        self.dirEntr = ctk.CTkEntry(self, placeholder_text="Dir to app", textvariable=self.entryVar, width=200)
        self.dirEntr.pack(side="left")

        self.button = ctk.CTkButton(
            self,
            text="Next",
            command=lambda: master.windws(0),
            width=50
        )
        self.button.pack(side="left", padx=15)

    def choseFile(self):
        directory = tk.filedialog.askdirectory(title="Chose program dir:")
        self.entryVar.set(directory)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.man = core.getMan()

        self.windws(0)

    def windws(self, stage):
        if hasattr(self, 'frame1'):
            self.frame1.destroy()
        if hasattr(self, 'frame2'):
            self.frame2.destroy()
        self.update_idletasks()
        
        match stage:
            case 0:
                self.frame1 = TitleFrame(master=self)
                self.frame1.pack(fill="both", expand=True, padx=20, pady=20)
            case 1:
                self.frame2 = DirFrame(master=self)
                self.frame2.pack(fill="both", expand=True, padx=20, pady=20)

    def button_callbck(self):
        self.after(10, lambda: self.windws(1))

app = App()
app.mainloop()