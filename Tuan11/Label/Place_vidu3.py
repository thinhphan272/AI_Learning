import tkinter as tk
root = tk.Tk()
root.title("Ví dụ Sử Dụng Phương thức Place với Các Tùy Chọn")
# Tạo label

label = tk.Label(root, text="Hello, Place!", bg="yellow", fg="black")

#Sử dụng các tùy chọn place

label.place(anchor="nw",
            relx=0.5,
            rely=0.5,
            relwidth=0.75,
            relheight=0.5,
            bordermode="inside")

root.mainloop()