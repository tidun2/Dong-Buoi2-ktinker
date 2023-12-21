import customtkinter

buttonNumber = 1000


class FrameScrollBar(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color="yellow")
        for item in range(buttonNumber):
            button = customtkinter.CTkButton(
                master=self, text=f'Nút thứ {item+1}', command=lambda index=item: self.getNumberButton(index+1))
            button.pack()

    def getNumberButton(self, id):
        print(id)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Đông Sun")
        self.geometry("800x800")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        frameScrollBar = FrameScrollBar(self)
        frameScrollBar.pack(expand=True, fill="both")


app = App()
app.mainloop()
