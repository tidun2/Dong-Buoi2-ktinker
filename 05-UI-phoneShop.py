import customtkinter
import json
import os
from PIL import Image, ImageOps, ImageDraw


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Phone Shop")
        self.geometry("800x800")
        self.resizable(width=False, height=False)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        # label_name = customtkinter.CTkLabel(self, text="Phone Name:")
        # label_name.grid(row=0, column=0, padx=10, pady=5)
        image_folder = 'img'

        image_path = os.path.join(image_folder, "iphone1.png")
        rounded_image = add_border_radius(image_path, 20)
        my_image = customtkinter.CTkImage(light_image=rounded_image,
                                          dark_image=rounded_image,
                                          size=(300, 300))
        image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        image_label.pack()


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

    # Specify the path to your JSON file
    json_file_path = 'dataPhone.json'
    # Open the JSON file and load its contents into a Python dictionary
    with open(json_file_path, 'r') as file:
        python_data = json.load(file)
