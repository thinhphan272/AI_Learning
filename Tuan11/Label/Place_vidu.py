import tkinter as tk
root = tk.Tk()
root.title("Sử Dụng Phương thức Place")

#Tạo label
label = tk.Label(root, text="Hello, Place!")
label.place(x=100, y=50)

root.mainloop()