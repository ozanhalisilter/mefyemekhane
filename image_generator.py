from PIL import Image,ImageFont,ImageDraw



class ImageGenerator:
    def __init__(self):
        self.img = Image.open("empty_page.jpg")
        self.font = ImageFont.truetype("cassandra.ttf",25)
        self.draw = ImageDraw.Draw(self.img)

    def generate_menu(self,text):
        coordinates = (150,150)
        color = 2
        self.draw.text(coordinates, text, font=self.font)
        self.img.save("text.png")


if __name__ == '__main__':
    generator = ImageGenerator()
    generator.generate_menu("Hello world!")



