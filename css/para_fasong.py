import tkinter as tk
import numpy

def fasongquit():
    fasong.quit()

def output():
    para1=input_para_1.get()
    numpy.save('tmp1.npy',para1)

    fasong.quit()


fasong = tk.Tk()

fasong.title("发送")

fasong.geometry("200x200")
fasong.resizable(width=False, height=False)#锁定窗口大小

label_para_1 = tk.Label(fasong, text="随机信号长度",font=("微软雅黑",10))
label_para_1.pack(side=tk.TOP,anchor="n")

input_para_1=tk.Entry(fasong)
input_para_1.pack(side=tk.TOP,pady=5,anchor='n')



b1=tk.Button(fasong, text='确认', command=output)
b1.place (x=20,y=150, anchor='w', width=60, height=40)

b2=tk.Button(fasong, text='返回', command=fasongquit)
b2.place (x=120,y=150, anchor='w', width=60, height=40)


fasong.mainloop()