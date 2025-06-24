import tkinter as tk

def show_selection():
    selected_option = radio_var.get()
    if selected_option == 1:
        label.config(text="Bạn chọn Lựa chọn 1")
    elif selected_option == 2:
        label.config(text="Bạn chọn Lựa chọn 2")

root = tk.Tk()
root.title("Radiobutton Demo")

# Biến IntVar để lưu trạng thái của Radiobutton
radio_var = tk.IntVar()

#Tạo các Radiobutton
radiobutton1 = tk.Radiobutton(root, text="Lựa chọn 1",
                              variable=radio_var,
                              value=1)
radiobutton2 = tk.Radiobutton(root, text="Lựa chọn 2",
                              variable=radio_var,
                              value=2)
radiobutton1.pack()
radiobutton2.pack()

#Tạo nút để hiển thị lựa chọn đã chọn
button = tk.Button(root, text="Hiền thị",
                   command=show_selection)
button.pack()

#Nhãn để hiển thị lựa chọn đã chọn
label = tk.Label(root, text="")
label.pack()

root.mainloop()