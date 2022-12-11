import customtkinter, tkinter
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{200}x{250}")
        self.resizable(0,0)
        self.title("Calculadora")

    
        self.nomeros()
        self.resultado_ver()
        self.button = customtkinter.CTkButton(text="resultado", command=self.suma)
        self.button.pack()


    def nomeros(self):
        self.n1=customtkinter.CTkEntry(justify =tkinter.CENTER,)
        self.n1.pack(padx=5 , pady=10)
    
        self.n2=customtkinter.CTkEntry(justify =tkinter.CENTER)
        self.n2.pack(padx=10 , pady=10)
  
        
    def resultado_ver(self):
        self.total=customtkinter.CTkLabel(fg_color="#FFFFFF", text='', text_color='red',)
        self.total.pack(padx=15 , pady=10)
        
    def suma(self): 
        n1=int(self.n1.get())
        n2=int(self.n2.get())
        sum = int(n1) + int(n2)
        self.total.configure(text=sum)

    
if __name__=="__main__":
    app=App()
    app.mainloop()
