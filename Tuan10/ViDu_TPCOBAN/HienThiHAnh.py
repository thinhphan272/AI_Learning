import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Hiển thị Hình Ảnh")

# Load hình ảnh từ đường dẫn
image = Image.open("../image/TkinterTutorials.png")
# Chuyển đổi hình ảnh thành định dạng có thể sử dụng trong tkinter
photo = ImageTk.PhotoImage(image)


label = tk.Label(root, image=photo)
label.pack()

root.mainloop()