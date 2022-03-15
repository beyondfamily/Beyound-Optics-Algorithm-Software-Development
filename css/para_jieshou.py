import tkinter as tk
import numpy

def jieshouquit():
    jieshou.quit()

def output():
    para1=input_para_1.get()
    para2=input_para_2.get()
    numpy.save('tmp1.npy',para1)
    numpy.save('tmp2.npy',para2)

    jieshou.quit()


jieshou = tk.Tk()

jieshou.title("接收")

jieshou.geometry("200x200")
jieshou .resizable(width=False, height=False)#锁定窗口大小

label_para_1 = tk.Label(jieshou, text="参数1",font=("微软雅黑",10))
label_para_1.pack(side=tk.TOP,anchor="n")

input_para_1=tk.Entry(jieshou)
input_para_1.pack(side=tk.TOP,pady=5,anchor='n')

label_para_2 = tk.Label(jieshou, text="参数2",font=("微软雅黑",10))
label_para_2.pack(side=tk.TOP,anchor="n")

input_para_2=tk.Entry(jieshou)
input_para_2.pack(side=tk.TOP,pady=5,anchor='n')



b1=tk.Button(jieshou, text='确认', command=output)
b1.place (x=20,y=150, anchor='w', width=60, height=40)

b2=tk.Button(jieshou, text='返回', command=jieshouquit)
b2.place (x=120,y=150, anchor='w', width=60, height=40)





jieshou.mainloop()