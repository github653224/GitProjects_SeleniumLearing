from PIL import Image
im=Image.open("D:\\images\\test.jpg")
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save("D:\\images\\test00.jpg","JPEG")