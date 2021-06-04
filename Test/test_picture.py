from PIL import Image, ImageDraw, ImageFont
     
if __name__ == "__main__":
    img = Image.new('RGB', (800, 600), color = 'red')
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", 32)

    draw.text((100, 100), "Пробный текст", font=font)
    img.show()
    # img.save('pil_red.png')
