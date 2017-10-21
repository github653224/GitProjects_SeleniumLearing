# 第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。
# 不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，因此，
# 基于PIL的Pillow项目开发非常活跃，并且支持最新的Python 3
from PIL import Image
im=Image.open("1.jpg")
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save("2.png","JPEG")

im2=Image.open("2.png")
print(im2.format,im2.size,im2.mode)