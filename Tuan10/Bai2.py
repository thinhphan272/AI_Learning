import tkinter as tk
import tkinter.messagebox as mb

def on_button_click():
    mb.showinfo("Thông báo", "Bạn đã nhấn vào nút")


root = tk.Tk()
root.title("Hello Tkinter")

label = tk.Label(root, text="Chào mừng đến với Tkinter")
label.pack(pady=10)

button = tk.Button(root, text="Nhấn vào đây",
                   command=on_button_click)
button.pack(pady=5)

root.mainloop()
