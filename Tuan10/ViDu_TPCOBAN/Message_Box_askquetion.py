import tkinter.messagebox as mb
response = mb.askquestion("Xác nhận", "Bạn có chắc chắn muốn tiếp tục?")
if response == "yes":
    print("Đã chọn Yes")
else:
    print("Đã chọn No")