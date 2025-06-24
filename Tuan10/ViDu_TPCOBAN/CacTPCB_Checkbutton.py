import tkinter as tk

def show_selection():
    selection = ""
    if check_var1.get():
        selection += "Tùy chọn 1 được chọn. "
    if check_var2.get():
        selection += "Tùy chọn 2 được chọn. "
    label.config(text=selection)


root = tk.Tk()
root.title('Checkbutton Demo')

#Biến BooleanVar cho các Check button
check_var1 = tk.BooleanVar()
check_var2 = tk.BooleanVar()

#Tạo các Checkbutton
checkbutton1 = tk.Checkbutton(root, text="Tùy chọn 1",
                              variable=check_var1)
checkbutton2 = tk.Checkbutton(root, text="Tùy chọn 2",
                              variable=check_var2)
checkbutton1.pack()
checkbutton2.pack()


#Tạo nút để hiển thị tùy chọn đã chọn
button = tk.Button(root, text="Hiển thị tùy chọn",
                   command=show_selection)
button.pack()

# Nhãn để hiển thị tùy chọn đã chọn
label = tk.Label(root, text="")
label.pack()

root.mainloop()
