from tkinter import *

window = Tk()

photo = PhotoImage(file="image/like.png")
count =0
def click():
    global count
    count+=1
    print(f"You clicked the button {count} time")

button = Button(window,
                text="Click Me!",
                command=click, #gán 1 hàm hoặc 1 phương thức để thực thi
                font=("Comic Sans", 30),
                fg='#32a852',
                bg='black',
                activeforeground='#6f89ad', #màu chữ sau khi bấm
                activebackground='#aa6fad', #màu nền sau khi bấm 
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()