from PIL import Image,ImageFont,ImageDraw
import req


class ImageGenerator:
    def __init__(self):
        self.img = Image.open("empty_page.jpg")
        self.font = ImageFont.truetype("arial.ttf",16)
        self.draw = ImageDraw.Draw(self.img)

    def generate_menu(self,text_list):
        coordinates = (150,150)
        color = 2
        self.draw.text((150,150), text_list, font=self.font)


        self.img.save("text.png")


if __name__ == '__main__':
    generator = ImageGenerator()
    requester = req.Menu()
    print(requester.get_menu())
    generator.generate_menu(requester.get_menu())



