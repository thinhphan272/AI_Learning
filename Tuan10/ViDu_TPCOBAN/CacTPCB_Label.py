import tkinter as tk

root = tk.Tk()
root.title('Định dạng nhãn')

# Nhãn với văn bản đậm, màu đỏ, font Arial, và nền màu vàng
label1 = tk.Label(root, text="Nhãn đậm và đỏ,",
                  font=("Arial", 12, "bold"),
                  fg="red",
                  bg="yellow")
label1.pack()

# Nhãn căn giữa với font chữ và màu nền khác
label2 = tk.Label(root, text="Nhãn căn giữa",
                  font=("Times New Roman", 14),
                  justify="center",
                  bg="lightblue")
label2.pack()

# Nhãn có kích thước rộng và cao
label3 = tk.Label(root, text="Nhãn kích thước rộng và cao",
                  width=30,
                  height=2,
                  bg="lightgreen")
label3.pack()

root.mainloop()



