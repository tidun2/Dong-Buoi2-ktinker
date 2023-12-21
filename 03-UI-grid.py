import customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()

root.title("Đông Sun")
root.geometry("800x800")
root.resizable(width=False, height=False)

root.columnconfigure((0, 1), weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)


fTopLeft = customtkinter.CTkFrame(root, fg_color="yellow")
fTopLeft.grid(row=0, column=0, sticky="nswe")

fTopRight = customtkinter.CTkFrame(root, fg_color="red")
fTopRight.grid(row=0, column=1, sticky="nswe")

fBotLeft = customtkinter.CTkFrame(root, fg_color="gray")
fBotLeft.grid(row=1, column=0, sticky="nswe")

fBotRight = customtkinter.CTkFrame(root, fg_color="blue")
fBotRight.grid(row=1, column=1, sticky="nswe")


root.mainloop()
