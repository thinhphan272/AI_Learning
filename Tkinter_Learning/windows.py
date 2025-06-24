from tkinter import *

window = Tk() #khai báo 1 cửa sổ mới
window.geometry("420x420") #size cửa sổ
window.title("Bro Code first GUI program") #Tiêu đề cửa sổ
icon = PhotoImage(file='image/pngtree-wolf-logo-png-image_2306634.png') #khai báo 1 hình
window.iconphoto(False, icon) #thiết lập icon
window.config(background="black") #thiết lập các thuộc tính

window.mainloop() #duy trì chương trình
