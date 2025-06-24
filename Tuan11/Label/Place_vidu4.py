import tkinter as tk
root = tk.Tk()
root.title("Ví dụ Sử Dụng Phương thức Place với Nhiều Label")
# Tạo các label
label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label3 = tk.Label(root, text="Label 3", bg="blue", fg="white")

#Sử dụng các thuộc tính place
label1.place(x=50, y= 50, width=100, height=50, anchor="nw")
label2.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.3, anchor="center")
label3.place(x=200, y=200, width=150, height=50, anchor="se")

root.mainloop()