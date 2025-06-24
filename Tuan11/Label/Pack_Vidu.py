import tkinter as tk

root = tk.Tk()
root.title("Sử Dụng Phương Thức Pack")

#Tạo các widget
label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label2 = tk.Label(root, text="Label 1", bg="blue", fg="white")
label3 = tk.Label(root, text="Label 1", bg="green", fg="white")

#Sắp xếp các widget bằng Pack

label1.pack(side="top", fill="x")
label2.pack(side="left", fill="y")
label3.pack(side="right", fill="both", expand=True)
root.mainloop()