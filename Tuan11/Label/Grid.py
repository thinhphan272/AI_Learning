import tkinter as tk
root = tk.Tk()
root.title("Sử Dụng Phương Thức Grid")

#Tạo các widget
label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label3 = tk.Label(root, text="Label 3", bg="blue", fg="white")

#Sắp xếp các widget bằng Grid

label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=1, column=0, sticky="nsew")
label3.grid(row=0, column=1, rowspan=2, sticky="nsew")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()