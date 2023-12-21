import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.title("demo customtkinter")
root.geometry("800x800")
# root.resizable(width=False, height=False)

frameTop = customtkinter.CTkFrame(master=root, fg_color="#646568")
frameTop.pack(side=TOP, fill=BOTH, expand=True)

frameBot = customtkinter.CTkFrame(master=root, fg_color="#646568")
frameBot.pack(side=TOP, fill=BOTH, expand=True)

fTopLeft = customtkinter.CTkFrame(master=frameTop, fg_color="yellow")
fTopLeft.pack(side=LEFT, fill=BOTH, expand=True)
fTopRight = customtkinter.CTkFrame(master=frameTop, fg_color="red")
fTopRight.pack(side=LEFT, fill=BOTH, expand=True)


fBotLeft = customtkinter.CTkFrame(master=frameBot, fg_color="gray")
fBotLeft.pack(side=LEFT, fill=BOTH, expand=True)
fBotRight = customtkinter.CTkFrame(master=frameBot, fg_color="blue")
fBotRight.pack(side=LEFT, fill=BOTH, expand=True)


root.mainloop()
