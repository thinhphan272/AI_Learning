import tkinter as tk

def show_text():
    text = entry.get()
    label.config(text=f"Bạn đã nhập: {text}")

root = tk.Tk()

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack()

button = tk.Button(root, text="Submit",
                   command=show_text)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()