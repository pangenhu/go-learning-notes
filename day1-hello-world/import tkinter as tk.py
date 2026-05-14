import tkinter as tk
from tkinter import messagebox

def hello():
    messagebox.showinfo('提示', "项目打包成功了")

root = tk.Tk()
root.title("my first project")
root.geometry("300x200")

btn = tk.Button(
    root,
    text="点我试试",
    command=hello,
    font=("微软雅黑",12)
)
btn.pack(expand=True)

root.mainloop()

