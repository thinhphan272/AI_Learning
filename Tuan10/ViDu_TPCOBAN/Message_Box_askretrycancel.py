import tkinter.messagebox as mb
response = mb.askretrycancel("Xác nhận", "Đã xảy ra một lỗi. Bạn có muốn thử lại?")
if response:
    print("Đã chọn Retry")
else:
    print("Đã chọn Cancel")