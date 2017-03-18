from PIL import Image,ImageEnhance

im = Image.open("girls.jpg")
enhancer = ImageEnhance.Sharpness(im)
enhancer.enhance(40).show()