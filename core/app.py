import customtkinter as ctk
import core

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.man = core.getMan()

        self.card = ctk.CTkFrame(self, corner_radius=15)
        self.card.pack(expand=True, fill="both", padx=20, pady=20)

        self.iconLb = ctk.CTkLabel(
            self.card, 
            text="", 
            image=core.getImg((48, 48), self.man["Icon"])
        )
        self.iconLb.pack(side="left", padx=(15, 20), pady=15)

        self.nameLb = ctk.CTkLabel(
            self.card, 
            text=self.man["Name"], 
            fg_color="transparent",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.nameLb.pack(side="left", pady=15)

        self.button = ctk.CTkButton(
            self.card, 
            text="Install",
            command=self.button_callbck,
            width=100
        )
        self.button.pack(side="right", padx=(20, 15), pady=15)

    def button_callbck(self):
        print("Install oga")

app = App()
app.mainloop()