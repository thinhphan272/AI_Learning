import tkinter.messagebox as mb
response = mb.askyesno("Xác nhận", "Bạn có chắc chắn muốn tiếp tục?")
if response:
    print("Đã chọn Yes")
else:
    print("Đã chọn No")