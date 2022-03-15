import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class MainForm:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('MainPage')
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (self.w, self.h))
        self.root['background'] = "LightSlateGray"
        self.root.update()

        self.canvas = tkinter.Canvas(self.root,height = 3000,width = 3000,bg = 'white')
        self.canvas.place(x=0,y=0)
        self.canvas.bind("<Button-1>", lambda event:self.draw_lines(event))

        self.element_list = []
        self.grid1 = np.zeros(2)
        self.grid2 = np.zeros(2)
        self.position = 0
        self.flag = False

        self.button_fasong = tkinter.Button(self.root, text='fasong', fg='black', width=6, font=('微软雅黑', 10))
        self.button_QAM = tkinter.Button(self.root, text='QAM', fg='black', width=6, font=('微软雅黑', 10))
        self.button_jieshou = tkinter.Button(self.root, text='jieshou', fg='black', width=6, font=('微软雅黑', 10))
        self.button_yakuo = tkinter.Button(self.root, text='yakuo', fg='black', width=6, font=('微软雅黑', 10))
        self.button_jieya = tkinter.Button(self.root, text='jieya', fg='black', width=6, font=('微软雅黑', 10))
        self.button_PAPR = tkinter.Button(self.root, text='PAPR', fg='black', width=6, font=('微软雅黑', 10))
        self.button_run = tkinter.Button(self.root,text='RUN',fg='black',width=6,font=('微软雅黑',10))

        self.button_fasong.pack(side='left', expand='True', anchor='center', padx=5)
        self.button_QAM.pack(side='left', expand='True', anchor='center', padx=5)
        self.button_jieshou.pack(side='left', expand='True', anchor='center', padx=5)
        self.button_yakuo.pack(side='left', expand='True', anchor='center', padx=5)
        self.button_jieya.pack(side='left', expand='True', anchor='center', padx=5)
        self.button_PAPR.pack(side='left', expand='True', anchor='center', padx=5)
        self.button_run.place(x=500,y=480)

        self.button_fasong.bind('<ButtonRelease-1>',lambda event:self.element_handle(event))
        self.button_QAM.bind('<ButtonRelease-1>', lambda event: self.element_handle(event))
        self.button_jieshou.bind('<ButtonRelease-1>', lambda event: self.element_handle(event))
        self.button_yakuo.bind('<ButtonRelease-1>', lambda event: self.element_handle(event))
        self.button_jieya.bind('<ButtonRelease-1>', lambda event: self.element_handle(event))
        self.button_PAPR.bind('<ButtonRelease-1>', lambda event: self.element_handle(event))
        self.button_run.bind('<ButtonRelease-1>', lambda  event: self.list_run(event))

        self.root.mainloop()

    def element_handle(self,event):
        self.grid1[0] = self.grid2[0]
        self.grid1[1] = self.grid2[1]
        self.grid2[0] = event.x_root-self.root.winfo_x()-8
        self.grid2[1] = event.y_root-self.root.winfo_y()-30
        if self.flag == True:
            if abs(self.grid2[0]-self.grid1[0])>abs(self.grid2[1]-self.grid1[1]):
                self.canvas.create_line(self.grid1[0], self.grid1[1], self.grid2[0], self.grid1[1], arrow='last',
                                        arrowshape=(8, 15, 3))
                self.canvas.create_line(self.grid2[0], self.grid1[1], self.grid2[0], self.grid2[1], arrow='last',
                                        arrowshape=(8, 15, 3))
            else:
                self.canvas.create_line(self.grid1[0], self.grid1[1], self.grid1[0], self.grid2[1], arrow='last',
                                        arrowshape=(8, 15, 3))
                self.canvas.create_line(self.grid1[0], self.grid2[1], self.grid2[0], self.grid2[1], arrow='last',
                                        arrowshape=(8, 15, 3))
        if len(self.element_list) == 0:
            self.element_list.append(event.widget['text'])
        elif self.flag == True:
            self.element_list.append(event.widget['text'])
        self.flag = not self.flag

    def list_run(self,event):
        print(self.element_list)
        for element in self.element_list:
            if element == 'fasong':
                print('fasong')
            elif element == 'QAM':
                print('QAM')
            elif element == 'jieshou':
                print('jieshou')
            elif element == 'yakuo':
                print('yakuo')
            elif element == 'jieya':
                print('jieya')
            elif element == 'PAPR':
                print('PAPR')

    def draw_lines(self,event):
        self.grid1[0] = self.grid2[0]
        self.grid1[1] = self.grid2[1]
        self.grid2[0] = event.x
        self.grid2[1] = event.y
        if self.flag == True:
            if abs(self.grid2[0] - self.grid1[0]) > abs(self.grid2[1] - self.grid1[1]):
                self.canvas.create_line(self.grid1[0], self.grid1[1], self.grid2[0], self.grid1[1], arrow='last',
                                        arrowshape=(8, 15, 3))
                self.grid2[1] = self.grid1[1]
            else:
                self.canvas.create_line(self.grid1[0], self.grid1[1], self.grid1[0], self.grid2[1], arrow='last',
                                        arrowshape=(8, 15, 3))
                self.grid2[0] = self.grid1[0]
def main():
    MainForm()

if __name__ == '__main__':
    main()