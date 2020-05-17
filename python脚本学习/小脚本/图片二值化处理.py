from PIL import Image
img = Image.open('one.jpg')

Img = img.convert('L')
Img.save('two.jpg')