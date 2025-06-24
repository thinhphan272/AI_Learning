import tkinter as tk

def say_hello():
    label.config(text="Hello Button!")

root = tk.Tk()
root.title("Button Demo")

#Tạo một nhãn
label = tk.Label(root, text="Nhấn nút để thay đổi văn bản")
label.pack(pady=10)

# Tạo nút để thực hiện hành động
button = tk.Button(root, text="Click Me!",
                   command=say_hello,
                   width=15,
                   height=2,
                   bg="blue",
                   fg="white",
                   font=("Arial", 12, "bold"),
                   relief="raised",
                   state="normal")
button.pack()

root.mainloop()