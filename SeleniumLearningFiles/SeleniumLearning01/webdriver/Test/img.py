from PIL import  Image

im=Image.open('D:\\test.jpg')
print(im.format, im.size, im.mode)

im.thumbnail((20,10))
im.save('D:\\thumb.jpg', 'JPEG')
