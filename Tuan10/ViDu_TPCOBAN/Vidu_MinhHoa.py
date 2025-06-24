import tkinter as tk

#Tạo cửa sổ chính
root = tk.Tk()
root.title("Hello Tkinter")

#Thêm nhãn vào của sổ
label = tk.Label(root, text="Chào mừng bạn đến với Tkinter!")
label.pack()

#Thêm nút vào cửa sổ
button = tk.Button(root, text="Click me!", command=root.quit)
button.pack()

#Loop chạy ứng dụng
root.mainloop()