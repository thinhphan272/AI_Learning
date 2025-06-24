import tkinter as tk

def show_selected():
    selected_items = listbox.curselection()
    selection = ""
    for index in selected_items:
        selection += listbox.get(index) + "\n"
    label.config(text=selection)


root = tk.Tk()
root.title("Listbox Demo")


# Tạo Listbox với chiều cao 4 mục và chế độ chọn nhiều mục
listbox = tk.Listbox(root, height=5,
                     selectmode=tk.MULTIPLE,
                     activestyle="dotbox")
listbox.pack(pady=10)

#Thêm mục vào listbox
for item in ["Mục 1", "Mục 2", "Mục 3", "Mục 4"]:
    listbox.insert(tk.END, item)

button = tk.Button(root, text="Hiển thị",
                   command=show_selected)
button.pack()

#Nhãn để hiển thị các mục đã chọn
label = tk.Label(root, text="")
label.pack()

root.mainloop()