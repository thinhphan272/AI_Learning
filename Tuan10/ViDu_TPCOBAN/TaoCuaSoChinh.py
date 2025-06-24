import tkinter as tk

root = tk.Tk()
root.title("Cửa sổ chính")
root.geometry("400x300+100+50") # Kích thước 400x300, vị trí 100, 50 trên màn hình
root.resizable(width=True, height=True) # Cho phép thay đổi kích thước cửa sổ
root.configure(bg='lightblue')

label = tk.Label(root, text="Đây là cửa sổ chính")
label.pack(pady=20)

button = tk.Button(root, text="Click để đóng cửa sổ", command=root.quit)
button.pack()

root.mainloop()