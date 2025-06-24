import tkinter.messagebox as mb
response = mb.askokcancel("Xác nhận", "Bạn có chắc chắn muốn tiếp tục?")
if response:
    print("Đã chọn OK")
else:
    print("Đã chọn Cancel")