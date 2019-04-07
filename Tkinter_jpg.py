from tkinter import *
from PIL import Image, ImageTk

root = Tk()

textLabel = Label(root, text='您所下载的影片含有未成年人限制内容，请满18周岁后再点击观看！')
textLabel.pack()

img_jpg = Image.open('D:\\learnPython\\testCode\\HelloWorld\\FishC\\NetSpider\\image_download\\Meizitu\\01.jpg')
photo = ImageTk.PhotoImage(img_jpg)
img_jpg.close()

imgLabel = Label(root, image=photo)
imgLabel.pack()

mainloop()
