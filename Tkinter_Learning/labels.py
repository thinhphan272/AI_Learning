from tkinter import *

window = Tk()

photo = PhotoImage(file ='image/like.png')

label = Label(window,
              text="Hello", #nội dung
              font=('Arial', 40, 'bold'), #phông, size, kiểu chứ
              fg='#00FF00', #màu chữ
              bg='black', #màu background
              relief=RAISED, #kiểu đường viền
              bd=10, #độ dày viền
              padx=30, #căn trái phải
              pady=30, #căn trên dưới
              image=photo, #chèn hình
              compound='bottom') #vị trí hỉnh
label.pack()

#label.place(x=100, y=100)

window.mainloop()