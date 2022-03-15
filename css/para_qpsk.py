import tkinter as tk
import numpy

def qpskquit():
    qpsk.quit()

def output():
    para1=input_para_1.get()
    para2=input_para_2.get()
    numpy.save('tmp1.npy',para1)
    numpy.save('tmp2.npy',para2)

    qpsk.quit()


qpsk = tk.Tk()

qpsk.title("QPSK")

qpsk.geometry("200x200")
qpsk.resizable(width=False, height=False)#锁定窗口大小

label_para_1 = tk.Label(qpsk, text="截止频率fc",font=("微软雅黑",10))
label_para_1.pack(side=tk.TOP,anchor="n")

input_para_1=tk.Entry(qpsk)
input_para_1.pack(side=tk.TOP,pady=5,anchor='n')

label_para_2 = tk.Label(qpsk, text="采样频率fs",font=("微软雅黑",10))
label_para_2.pack(side=tk.TOP,anchor="n")

input_para_2=tk.Entry(qpsk)
input_para_2.pack(side=tk.TOP,pady=5,anchor='n')

b1=tk.Button(qpsk, text='确认', command=output)
b1.place (x=20,y=150, anchor='w', width=60, height=40)

b2=tk.Button(qpsk, text='返回', command=qpskquit)
b2.place (x=120,y=150, anchor='w', width=60, height=40)

qpsk.mainloop()
