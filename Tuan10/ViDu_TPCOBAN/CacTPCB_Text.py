import tkinter as tk

def get_text():
    text_content = text.get("1.0", tk.END)
    print("Nội dung văn bản: \n", text_content)

root = tk.Tk()
root.title("Text Demo")

#Tạo Text với chiều cao 10 dòng và chiều rộng 50 ký tự
text = tk.Text(root, height=10, width=50, wrap=tk.WORD)
text.pack(padx=10, pady=10)

#Tạo nút đê lấy nội dung văn bản từ Text
button = tk.Button(root, text="Lấy văn bản",
                   command=get_text)
button.pack(pady=5)

root.mainloop()