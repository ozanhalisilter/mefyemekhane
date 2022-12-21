from PIL import Image,ImageFont,ImageDraw


img = Image.open("empty_page.jpg")
font = ImageFont.truetype("cassandra.ttf",32)
draw = ImageDraw.Draw(img)

text = "Menu!"

draw.text((110,150), text, 2,font=font)


img.save("text.png")
 