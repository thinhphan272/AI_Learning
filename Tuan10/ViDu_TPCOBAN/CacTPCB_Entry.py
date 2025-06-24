import tkinter as tk

def show_text():
    text = entry.get()
    label.config(text=f'Hello {text}')


root = tk.Tk()
root.title("Entry Demo")

#Tạo ô nhập liệu
entry = tk.Entry(root, width=30,
                 font=('Arial', 12),
                 show="*",
                 insertbackground="green",
                 state="normal",
                 justify="center")
entry.pack(pady=10)


# Tạo nút để hiển thị văn bản trong ô nhập liệu
button = tk.Button(root, text="Hiển thị",
                   command=show_text)
button.pack()


# Nhãn để hiển thị văn bản từ ô nhập liệu
label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()