from PIL import Image, ImageDraw

if __name__ == "__main__":
    im = Image.new('RGB', (400, 400), (0, 255, 0, 0)) 
    draw = ImageDraw.Draw(im) 
    draw.line((50, 50, 350, 350), fill=128, width=30)
    im.show()
    
