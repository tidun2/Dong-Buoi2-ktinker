import customtkinter
import json
import os
from PIL import Image, ImageOps, ImageDraw


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Specify the path to your JSON file
        json_file_path = 'dataPhone.json'
        # Open the JSON file and load its contents into a Python dictionary
        with open(json_file_path, 'r') as file:
            python_data = json.load(file)
        resizable = False
        self.title("Phone Shop")
        self.geometry("1500x800")
        self.resizable(width=resizable, height=resizable)
        # Configure both rows and columns to expand with the window size
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # # Create a frame for the scroll layout
        frame_width_percentage = 90
        frame_width = self.winfo_screenwidth() * frame_width_percentage / 100
        frame = customtkinter.CTkScrollableFrame(
            self, fg_color="gray", width=frame_width)

        # Center the frame
        frame.grid(row=0, column=0, padx=(
            self.winfo_screenwidth() - frame_width) / 2, sticky="nswe")

        # Configure the column to take up the desired percentage of the window width
        self.grid_columnconfigure(0, weight=1)

        num_columns = 4
        num_rows = len(python_data) // num_columns + \
            (len(python_data) % num_columns > 0)

        # Render phones
        for index in range(len(python_data)):
            iRow, iCol = divmod(index, num_columns)
            phone_data = python_data[index]
            phone_card = PhoneCard(frame, **phone_data)
            phone_card.grid(row=iRow, column=iCol, padx=5, pady=5)


class PhoneCard(customtkinter.CTkFrame):
    def __init__(self, master, id, name, price, category):
        # import image
        image_folder = 'img'
        image_path = os.path.join(image_folder, "iphone1.png")
        rounded_image = add_border_radius(image_path, 30)
        my_image = customtkinter.CTkImage(light_image=rounded_image,
                                          dark_image=rounded_image,
                                          size=(300, 300))

        super().__init__(master)
        self.grid(sticky='nswe')
        self.grid_columnconfigure(0, weight=1)

        # Create widgets for the PhoneCard frame
        image_label = customtkinter.CTkLabel(
            self, image=my_image, text='')
        image_label.grid(row=0, column=0, padx=5, pady=5, sticky="s")
        name_label = customtkinter.CTkLabel(self, text=f"Name: {name}")
        name_label.grid(row=1, column=0, padx=5, pady=5, sticky="s")

        price_label = customtkinter.CTkLabel(self, text=f"Price: {price}")
        price_label.grid(row=2, column=0, padx=5, pady=5, sticky="s")

        category_label = customtkinter.CTkLabel(
            self, text=f"Category: {category}")
        category_label.grid(row=3, column=0, padx=5, pady=5, sticky="s")
        buttonThemGioHang = customtkinter.CTkButton(
            self, text="Mua luôn", command=lambda: self.themVaoGioHang(id))
        buttonThemGioHang.grid(row=4, column=0, padx=5, pady=5, sticky="s")

    def themVaoGioHang(self, id):
        print(f"Đã mua {id}")


def add_border_radius(image_path, radius):
    image = Image.open(image_path)
    mask = Image.new('L', image.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)
    result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    result.putalpha(mask)
    return result


if __name__ == "__main__":
    app = App()
    app.mainloop()
