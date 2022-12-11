import customtkinter

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.set_appearance_mode("light")
        self.geometry(f"{150}x{160}")
        self.resizable(0,0)
        self.title("home")
        
        self.button =customtkinter.CTkButton(bg_color='#FFFFFF', command=self.hola)
        self.button.pack(padx=30, pady =10  )
        
        self.textbox = customtkinter.CTkEntry(border_width=2, bg_color='#FFFFFF', border_color='#FFFFFF',)
        self.textbox.pack(side="top", padx=20, pady=10)

    def hola(self):
        print(self.textbox.get())
    

if __name__ == "__main__":
    App = App()
    App.mainloop()