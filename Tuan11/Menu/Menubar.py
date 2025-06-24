import tkinter as tk

def hello():
    print("Hello!")

def quit_app():
    root.quit()

#Bước 1: Tạo cửa sổ gốc
root = tk.Tk()
root.title("Menu Demo")

#Bước 2: Ta MenuBar
menubar = tk.Menu(root)

#Bước 3: Thêm các menu vào MenuBar
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=hello)
file_menu.add_command(label="Open", command=hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)

edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=hello)
edit_menu.add_command(label="Copy", command=hello)
edit_menu.add_command(label="Paste", command=hello)

#Bước 5 Kích hoạt Menubar
root.config(menu=menubar)

root.mainloop()













