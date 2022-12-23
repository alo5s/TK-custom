from customtkinter import CTk, CTkFrame, CTkButton
from PIL import Image , ImageTk
from tkinter import PhotoImage

root = CTk()
#root.set_appearance_mode("light")

root.geometry(f"{450}x{550}")
root.title("")

#---------------------------##----------------------------------#
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
#----------------------------------------------------------------#
barra = CTkFrame(master=root,height=1080 , width=50) 
barra.configure(fg_color="#1F1F1F", bg_color="#1F1F1F")
barra.grid(row=1 , column=0,)
#-----------------------------------------------------------------#

#height=30
#width=30

#img_home= Image.open("iconos/home (3).png")
#img_home = img_home.resize((height,width), Image.ANTIALIAS)
#img_home = ImageTk.PhotoImage(img_home)

#img_settings= Image.open("iconos/settings.png")
#img_settings = img_settings.resize((height,width), Image.ANTIALIAS)
#img_settings= ImageTk.PhotoImage(img_settings)

#-----------------------------------------------------------------------#
def switch_event():
    print("switch toggled, current value:")
#------------------------------------------------------------------#
bt= CTkButton(master=barra, text="" , command=switch_event,)
bt.configure(height=10,width=10, fg_color="#1F1F1F", hover_color="#1F1F1F" )
bt.place(y=10, x=6)

btn_settings= CTkButton(master=barra, text="" , command=switch_event,)
btn_settings.configure(height=10,width=10, fg_color="#1F1F1F", hover_color="#1F1F1F" )
btn_settings.place(y=55, x=6)

root.mainloop()