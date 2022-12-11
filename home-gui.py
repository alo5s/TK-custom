import customtkinter

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.set_appearance_mode("light")
        self.geometry(f"{550}x{560}")
        #self.resizable(0,0)
        self.title("home")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


    
        self.Edit_tex()

    def Edit_tex(self):

        self.text_edit =customtkinter.CTkTextbox(fg_color='#373636',text_color='red', width=100)
        self.text_edit.grid(row=0, column=0, sticky="nsew")

        self.texto_scroll = customtkinter.CTkScrollbar(command=self.text_edit.yview)
        self.texto_scroll.grid(row=0, column=1, sticky="ns")
        self.text_edit.configure(yscrollcommand=self.texto_scroll.set)

        
    

if __name__ == "__main__":
    App = App()
    App.mainloop()