import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.ttk
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from linklist import *
from qpskmod import *
from qpskdemod import *

plt.rcParams.update({'figure.max_open_warning': 0})  # 防止图片过多报警


class MainPage:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('MainPage')
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (self.w, self.h))  # 窗口全屏
        self.root['background'] = "white"  # 背景白色
        self.root.update()
        self.button_num = 0
        self.line_num = -1
        self.lianxian = False
        self.move = False
        self.tiaocan = False
        self.folder_flag = True  # 文件夹相关的flag
        self.drawbutton_list = []
        self.line_list = []

        self.finished_element = 0

        self.create_menu()  # 定义菜单
        self.control_frame()  # 定义控制窗
        self.element_frame()  # 定义元件窗口
        self.draw_frame()  # 定义绘图窗口

        self.root.mainloop()

    def create_menu(self):
        self.menu = tkinter.Menu(self.root)  # 建立菜单
        # ------------------文件菜单-------------------------------------------------------#
        self.file_menu = tkinter.Menu(self.menu, tearoff=False)
        self.file_menu.add_command(label='打开', command=self.menu_handle)
        self.file_menu.add_command(label='保存', command=self.menu_handle)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='关闭', command=self.root.quit)
        self.menu.add_cascade(label='文件', menu=self.file_menu)
        # ------------------编辑菜单-------------------------------------------------------#
        self.edit_menu = tkinter.Menu(self.menu, tearoff=False)
        self.edit_menu.add_command(label='复制', command=self.menu_handle)
        self.edit_menu.add_command(label='粘贴', command=self.menu_handle)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='设置', command=self.menu_handle)
        self.menu.add_cascade(label='编辑', menu=self.edit_menu)
        # ------------------右键弹出菜单----------------------------------------------------#
        self.pop_menu = tkinter.Menu(self.root, tearoff=False)
        self.pop_menu.add_command(label='复制', command=self.pop_menu_handle)
        self.pop_menu.add_command(label='粘贴', command=self.pop_menu_handle)
        self.pop_menu.add_command(label='删除', command=self.pop_menu_handle)
        self.pop_menu.add_separator()
        self.pop_menu.add_command(label='Beyond Family', command=self.pop_menu_handle)
        self.pop_menu.add_command(label='119484182@qq.com', command=self.pop_menu_handle)

        self.root.config(menu=self.menu)
        self.root.bind('<Button-3>', self.popup_handle)
        # -------------------------------------------------------------------------------#

    def control_frame(self):  # 控制区
        self.control_frame = tkinter.Frame(self.root, width=1920, height=50, bg='gray')
        self.control_frame.place(x=0, y=0)
        # --------------------添加图片------------------------------------------#
        self.new_file_image_path = "images/control_frame/newfile.png"
        self.new_file_image = tkinter.PhotoImage(file=self.new_file_image_path)
        self.new_file_over_image_path = "images/control_frame/newfile_o.png"
        self.new_file_over_image = tkinter.PhotoImage(file=self.new_file_over_image_path)
        self.new_file_k_image_path = "images/control_frame/newfile_k.png"
        self.new_file_k_image = tkinter.PhotoImage(file=self.new_file_k_image_path)

        self.open_image_path = "images/control_frame/open.png"
        self.open_image = tkinter.PhotoImage(file=self.open_image_path)
        self.open_over_image_path = "images/control_frame/open_o.png"
        self.open_over_image = tkinter.PhotoImage(file=self.open_over_image_path)
        self.open_k_image_path = "images/control_frame/open_k.png"
        self.open_k_image = tkinter.PhotoImage(file=self.open_k_image_path)

        self.save_image_path = "images/control_frame/save.png"
        self.save_image = tkinter.PhotoImage(file=self.save_image_path)
        self.save_over_image_path = "images/control_frame/save_o.png"
        self.save_over_image = tkinter.PhotoImage(file=self.save_over_image_path)
        self.save_k_image_path = "images/control_frame/save_k.png"
        self.save_k_image = tkinter.PhotoImage(file=self.save_k_image_path)

        self.run_image_path = "images/control_frame/run.png"
        self.run_image = tkinter.PhotoImage(file=self.run_image_path)
        self.run_over_image_path = "images/control_frame/run_o.png"
        self.run_over_image = tkinter.PhotoImage(file=self.run_over_image_path)
        self.run_k_image_path = "images/control_frame/run_k.png"
        self.run_k_image = tkinter.PhotoImage(file=self.run_k_image_path)

        self.ligature_image_path = "images/control_frame/ligature.png"
        self.ligature_image = tkinter.PhotoImage(file=self.ligature_image_path)
        self.ligature_over_image_path = "images/control_frame/ligature_o.png"
        self.ligature_over_image = tkinter.PhotoImage(file=self.ligature_over_image_path)
        self.ligature_k_image_path = "images/control_frame/ligature_k.png"
        self.ligature_k_image = tkinter.PhotoImage(file=self.ligature_k_image_path)

        self.move_image_path = "images/control_frame/move.png"
        self.move_image = tkinter.PhotoImage(file=self.move_image_path)
        self.move_over_image_path = "images/control_frame/move_o.png"
        self.move_over_image = tkinter.PhotoImage(file=self.move_over_image_path)
        self.move_k_image_path = "images/control_frame/move_k.png"
        self.move_k_image = tkinter.PhotoImage(file=self.move_k_image_path)

        self.tiaocan_image_path = "images/control_frame/tiaocan.png"
        self.tiaocan_image = tkinter.PhotoImage(file=self.tiaocan_image_path)
        self.tiaocan_over_image_path = "images/control_frame/tiaocan_o.png"
        self.tiaocan_over_image = tkinter.PhotoImage(file=self.tiaocan_over_image_path)
        self.tiaocan_k_image_path = "images/control_frame/tiaocan_k.png"
        self.tiaocan_k_image = tkinter.PhotoImage(file=self.tiaocan_k_image_path)

        self.cancel_image_path = "images/control_frame/cancel.png"
        self.cancel_image = tkinter.PhotoImage(file=self.cancel_image_path)
        self.cancel_over_image_path = "images/control_frame/cancel_o.png"
        self.cancel_over_image = tkinter.PhotoImage(file=self.cancel_over_image_path)
        self.cancel_k_image_path = "images/control_frame/cancel_k.png"
        self.cancel_k_image = tkinter.PhotoImage(file=self.cancel_k_image_path)

        self.shibo_image_path = "images/control_frame/shibo.png"
        self.shibo_image = tkinter.PhotoImage(file=self.shibo_image_path)
        self.shibo_over_image_path = "images/control_frame/shibo_o.png"
        self.shibo_over_image = tkinter.PhotoImage(file=self.shibo_over_image_path)
        self.shibo_k_image_path = "images/control_frame/shibo_k.png"
        self.shibo_k_image = tkinter.PhotoImage(file=self.shibo_k_image_path)

        # -------------------------按钮动画------------------------

        def new_file_over(event):
            self.control_button[0].config(image=self.new_file_over_image)

        def new_file_leave(event):
            self.control_button[0].config(image=self.new_file_image)

        def new_file_k(event):
            self.control_button[0].config(image=self.new_file_k_image)

        def open_over(event):
            self.control_button[1].config(image=self.open_over_image)

        def open_leave(event):
            self.control_button[1].config(image=self.open_image)

        def open_k(event):
            self.control_button[1].config(image=self.open_k_image)

        def save_over(event):
            self.control_button[2].config(image=self.save_over_image)

        def save_leave(event):
            self.control_button[2].config(image=self.save_image)

        def save_k(event):
            self.control_button[2].config(image=self.save_k_image)

        def run_over(event):
            self.control_button[3].config(image=self.run_over_image)

        def run_leave(event):
            self.control_button[3].config(image=self.run_image)

        def run_k(event):
            self.control_button[3].config(image=self.run_k_image)

        def ligature_over(event):
            self.control_button[4].config(image=self.ligature_over_image)

        def ligature_leave(event):
            self.control_button[4].config(image=self.ligature_image)

        def ligature_k(event):
            self.control_button[4].config(image=self.ligature_k_image)

        def move_over(event):
            self.control_button[5].config(image=self.move_over_image)

        def move_leave(event):
            self.control_button[5].config(image=self.move_image)

        def move_k(event):
            self.control_button[5].config(image=self.move_k_image)

        def tiaocan_over(event):
            self.control_button[6].config(image=self.tiaocan_over_image)

        def tiaocan_leave(event):
            self.control_button[6].config(image=self.tiaocan_image)

        def tiaocan_k(event):
            self.control_button[6].config(image=self.tiaocan_k_image)

        def cancel_over(event):
            self.control_button[7].config(image=self.cancel_over_image)

        def cancel_leave(event):
            self.control_button[7].config(image=self.cancel_image)

        def cancel_k(event):
            self.control_button[7].config(image=self.cancel_k_image)

        def shibo_over(event):
            self.control_button[8].config(image=self.shibo_over_image)

        def shibo_leave(event):
            self.control_button[8].config(image=self.shibo_image)

        def shibo_k(event):
            self.control_button[8].config(image=self.shibo_k_image)
        # --------------------添加控制按钮-------------------------------------------------#
        self.control_button = []
        self.control_button = []
        self.control_button.append(
            tkinter.Button(self.control_frame, image=self.new_file_image, bd=0))
        self.control_button.append(
            tkinter.Button(self.control_frame, image=self.open_image, bd=0))
        self.control_button.append(
            tkinter.Button(self.control_frame, image=self.save_image, bd=0))
        self.control_button.append(
            tkinter.Button(self.control_frame, image=self.run_image, bd=0))
        self.control_button.append(
            tkinter.Button(self.control_frame, image=self.ligature_image, bd=0))
        self.control_button.append(
            tkinter.Button(self.control_frame, image=self.move_image, bd=0))
        self.control_button.append(
            tkinter.Button(self.control_frame, image=self.tiaocan_image, bd=0))
        self.control_button.append(
            tkinter.Button(self.control_frame, image=self.cancel_image, bd=0))
        self.control_button.append(
            tkinter.Button(self.control_frame, image=self.shibo_image, bd=0))
        # ----------------------绑定动画----------------------
        self.control_button[0].bind("<Enter>", new_file_over)
        self.control_button[0].bind("<Leave>", new_file_leave)
        self.control_button[0].bind("<Button-1>", new_file_k)
        self.control_button[0].bind("<ButtonRelease-1>", new_file_over)

        self.control_button[1].bind("<Enter>", open_over)
        self.control_button[1].bind("<Leave>", open_leave)
        self.control_button[1].bind("<Button-1>", open_k)
        self.control_button[1].bind("<ButtonRelease-1>", open_over)

        self.control_button[2].bind("<Enter>", save_over)
        self.control_button[2].bind("<Leave>", save_leave)
        self.control_button[2].bind("<Button-1>", save_k)
        self.control_button[2].bind("<ButtonRelease-1>", save_over)

        self.control_button[3].bind("<Enter>", run_over)
        self.control_button[3].bind("<Leave>", run_leave)
        self.control_button[3].bind("<Button-1>", run_k)
        self.control_button[3].bind("<ButtonRelease-1>", run_over)

        self.control_button[4].bind("<Enter>", ligature_over)
        self.control_button[4].bind("<Leave>", ligature_leave)
        self.control_button[4].bind("<Button-1>", ligature_k)
        self.control_button[4].bind("<ButtonRelease-1>", ligature_over)

        self.control_button[5].bind("<Enter>", move_over)
        self.control_button[5].bind("<Leave>", move_leave)
        self.control_button[5].bind("<Button-1>", move_k)
        self.control_button[5].bind("<ButtonRelease-1>", move_over)

        self.control_button[6].bind("<Enter>", tiaocan_over)
        self.control_button[6].bind("<Leave>", tiaocan_leave)
        self.control_button[6].bind("<Button-1>", tiaocan_k)
        self.control_button[6].bind("<ButtonRelease-1>", tiaocan_over)

        self.control_button[7].bind("<Enter>", cancel_over)
        self.control_button[7].bind("<Leave>", cancel_leave)
        self.control_button[7].bind("<Button-1>", cancel_k)
        self.control_button[7].bind("<ButtonRelease-1>", cancel_over)

        self.control_button[8].bind("<Enter>", shibo_over)
        self.control_button[8].bind("<Leave>", shibo_leave)
        self.control_button[8].bind("<Button-1>", shibo_k)
        self.control_button[8].bind("<ButtonRelease-1>", shibo_over)
        self.column = 0
        for i in self.control_button:
            i.grid(row=0, column=self.column)
            self.column += 1

        self.control_button[1].bind('<ButtonRelease-1>', lambda event: self.open_handle())  # 绑定打开事件
        self.control_button[2].bind('<ButtonRelease-1>', lambda event: self.save_handle())  # 绑定保存事件
        self.control_button[3].bind('<ButtonRelease-1>', lambda event: self.list_run(event))  # 绑定运行事件
        self.control_button[4].bind('<ButtonRelease-1>', lambda event: self.lianxian_handle())  # 绑定连线事件
        self.control_button[5].bind('<ButtonRelease-1>', lambda event: self.move_handle())  # 绑定拖动事件
        self.control_button[6].bind('<ButtonRelease-1>', lambda event: self.tiaocan_handle())  # 绑定调参
        self.control_button[7].bind('<ButtonRelease-1>', lambda event: self.cancel_handle())  # 撤销
        self.control_button[8].bind('<ButtonRelease-1>', lambda event: self.Oscilloscope())  # 示波器
        # -------------------------------------------------------------------------------#

    def delete_element(self):  # 删除
        pass

    def cancel_handle(self):  # 撤销 未完成，还需要改动
        if (self.line_num >= 0):
            self.canvas.delete(self.line_list[self.line_num])
            self.line_num -= 1
        else:
            pass

    def lianxian_handle(self):
        self.lianxian = True
        self.move = False
        self.tiaocan = False

    def move_handle(self):
        self.lianxian = False
        self.tiaocan = False
        self.move = True

    def tiaocan_handle(self):
        self.lianxian = False
        self.move = False
        self.tiaocan = True

    def element_frame(self):  # 元件列表区
        self.element_frame = tkinter.Frame(self.root, width=300, height=1030, bg='LightSlateGray')
        self.element_frame.place(x=0, y=50)
        # ---------------------下拉菜单--------------------------------------------------#
        # self.element_tuple = ('1','2','3')
        # self.element_combobox = tkinter.ttk.Combobox(self.element_frame, values= self.element_tuple)
        # self.element_combobox.bind('<<ComboboxSelected>>',self.combobox_handle)
        # self.element_combobox.place(x=50,y=50)
        # -----------------------------------------------------------------------------#

        # --------------------添加按钮--------------------------------------------------#
        self.button_list = [[], [], []]
        self.button_list[0].append(
            tkinter.Button(self.element_frame, text='发送', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[0].append(
            tkinter.Button(self.element_frame, text='接收', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[0].append(
            tkinter.Button(self.element_frame, text='QPSK', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[0].append(
            tkinter.Button(self.element_frame, text='QPSK\n解调', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[0].append(
            tkinter.Button(self.element_frame, text='ASK', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[0].append(
            tkinter.Button(self.element_frame, text='ASK', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[0].append(
            tkinter.Button(self.element_frame, text='QAM', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[0].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))

        self.button_list[1].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[1].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[1].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[1].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[1].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[1].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))

        self.button_list[2].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[2].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[2].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[2].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[2].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[2].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[2].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[2].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[2].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        self.button_list[2].append(
            tkinter.Button(self.element_frame, text='undef', fg='black', width='5', height='2', font=('微软雅黑', 10)))
        # -----------------------------------------------------------------------------#

        # -----------------------------整成文件夹的样子--------------------------------------------#
        self.folder_image = ImageTk.PhotoImage(file='images/img.png')
        self.return_button_image = ImageTk.PhotoImage(file='images/return.png')
        self.return_button = tkinter.Button(self.element_frame, image=self.return_button_image, borderwidth=0)
        self.folder_label = []
        self.folder_label.append(tkinter.Label(self.element_frame, image=self.folder_image, borderwidth=0))
        self.folder_label.append(tkinter.Label(self.element_frame, image=self.folder_image, borderwidth=0))
        self.folder_label.append(tkinter.Label(self.element_frame, image=self.folder_image, borderwidth=0))
        self.folder_label_text = []
        self.folder_label_text.append(tkinter.Label(self.element_frame, bg='#E8E8E8',
                                                    text='1', font=('微软雅黑', 6), fg='black'))
        self.folder_label_text.append(tkinter.Label(self.element_frame, bg='#E8E8E8',
                                                    text='2', font=('微软雅黑', 6), fg='black'))
        self.folder_label_text.append(tkinter.Label(self.element_frame, bg='#E8E8E8',
                                                    text='3', font=('微软雅黑', 6), fg='black'))
        if self.folder_flag:
            self.show_folder()

    def show_folder(self):
        self.folder_label[0].place(x=10, y=20)
        self.folder_label[1].place(x=110, y=20)
        self.folder_label[2].place(x=210, y=20)

        self.folder_label_text[0].place(x=40, y=40)
        self.folder_label_text[1].place(x=140, y=40)
        self.folder_label_text[2].place(x=240, y=40)

        self.folder_label[0].bind("<Button-1>", lambda event: self.show_element(event, n=0))
        # self.folder_label[0].bind_class("Label","<Double-Button-1>",self.return_last)
        self.folder_label[1].bind("<Button-1>", lambda event: self.show_element(event, n=1))
        self.folder_label[2].bind("<Button-1>", lambda event: self.show_element(event, n=2))
        self.return_button.bind("<Button-1>", self.return_last)

    def show_element(self, event, n):  # n代表第n组按钮
        # -----------------------------布局按钮并--------------------------------------------#
        self.folder_flag = False
        for i in range(0, 3):
            if i != n:
                self.folder_label[i].place_forget()
                self.folder_label_text[i].place_forget()
            else:
                self.return_button.place(x=40, y=20)
                self.folder_label[i].place(x=140, y=20)
                self.folder_label_text[i].place(x=170, y=40)
        self.label_x = [50, 150, 50, 150, 50, 150, 50, 150, 50, 150, 50, 150]
        self.label_y = [150, 150, 250, 250, 350, 350, 450, 450, 550, 550, 650, 650]
        num1 = 0
        for button in self.button_list[n]:
            button.bind('<Double-Button-1>', lambda event: self.pop_element(event))
            button.place(x=self.label_x[num1], y=self.label_y[num1] - 40)
            num1 += 1

        # --------------------------------------------------------------------------------#

    # 返回上一级文件夹
    def return_last(self, event):
        for i in self.button_list:
            for button in i:
                button.place_forget()
        self.return_button.place_forget()
        self.folder_label[0].place(x=10, y=20)
        self.folder_label[1].place(x=110, y=20)
        self.folder_label[2].place(x=210, y=20)
        self.folder_label_text[0].place(x=40, y=40)
        self.folder_label_text[1].place(x=140, y=40)
        self.folder_label_text[2].place(x=240, y=40)

    def combobox_handle(self, event):
        for button in self.button_list[self.now]:  # 隐藏当前显示的按钮列表
            button.place_forget()
        # ----------------显示选择的按钮列表--------------------------------------------------#
        self.now = int(self.element_combobox.get()) - 1
        num = 0
        for button in self.button_list[self.now]:
            button.place(x=self.label_x[num], y=self.label_y[num])
            num += 1
        # ---------------------------------------------------------------------------------#

    def draw_frame(self):  # 画图区
        self.element_list = []  # 绘图区的元件列表
        self.grid1 = np.zeros(2)  # 用于保存点击的元件的坐标
        self.grid2 = np.zeros(2)  # 用于保存点击的元件的坐标
        self.element_name1 = ''  # 用于保存点击的元件的名称
        self.element_name2 = ''  # 用于保存点击的元件的名称
        self.position = 0  # 以前写的，忘了具体作用，删了也不影响正常运行，但为了保险还是留着
        self.flag = False  # flag,用于连线

        self.draw_frame = tkinter.Frame(self.root, width=1620, height=830, bg='white')
        self.draw_frame.place(x=300, y=50)
        # -------------------------建立绘图的Canvas--------------------------------------#
        self.canvas = tkinter.Canvas(self.draw_frame, width=1620, height=830, bg='Gray')
        self.canvas.bind("<Button-1>", lambda event: self.draw_lines(event))
        self.canvas.place(x=0, y=0)
        # -----------------------------------------------------------------------------#

    def pop_element(self, event):  # 双击元件列表中的按钮后在绘图区生成相应的按钮
        button = event.widget['text'] + str(self.button_num)
        self.drawbutton_list.append(
            tkinter.Button(self.draw_frame, text=button, fg='black', width='5', height='2', font=('微软雅黑', 10)))
        button_name = ''
        for i in button:
            if i == '\n':
                pass
            else:
                button_name = button_name + i

        cmd = 'self.' + button_name + ' = Node(\'' + button_name + '\')'
        exec(cmd)

        # 用来代替原来初始变量的设置
        def pop_cmd(self):
            cmd = 'self.' + button_name + '.para1=10'
            exec(cmd)
            cmd = 'self.' + button_name + '.para2=100'
            exec(cmd)
            cmd = 'self.' + button_name + '.x_label=50+60*(self.button_num%15)'
            exec(cmd)
            cmd = 'self.' + button_name + '.y_label=100'
            exec(cmd)

        # cmd = 'print(self.' + button_name + '.item)'
        # exec(cmd)
        self.drawbutton_list[self.button_num].place(x=50 + 60 * (self.button_num % 15), y=100)
        self.drawbutton_list[self.button_num].bind('<ButtonRelease-1>',
                                                   lambda event: self.element_handle(event))  # 点击连线
        self.drawbutton_list[self.button_num].bind('<B1-Motion>', lambda event: self.element_move(event))  # 移动元件
        # ----------------------------------------------------------------------------------------------
        # 根据按钮名绑定不同的调参界面，并设置默认参数
        if '发送' in button_name:
            self.drawbutton_list[self.button_num].bind('<Double-Button-1>',
                                                       lambda event: self.fasong_get_parameters(event))
            cmd = 'self.' + button_name + '.para1=100'
            exec(cmd)
            cmd = 'self.' + button_name + '.x_label=50+60*(self.button_num%15)'
            exec(cmd)
            cmd = 'self.' + button_name + '.y_label=100'
            exec(cmd)
        elif 'QPSK' in button_name and button_name[4] in (str(shuzi) for shuzi in range(10)):
            self.drawbutton_list[self.button_num].bind('<Double-Button-1>',
                                                       lambda event: self.qpsk_get_parameters(event))
            pop_cmd(self)
            # print(self.QPSK1.para1)
        elif 'QPSK解调' in button_name:
            self.drawbutton_list[self.button_num].bind('<Double-Button-1>',
                                                       lambda event: self.qpsk_get_parameters(event))
            pop_cmd(self)
            # print(self.QPSK解调2.para1)
        # 接收，QAM,PAPR的
        elif '接收' in button_name:
            self.drawbutton_list[self.button_num].bind('<Double-Button-1>',
                                                       lambda event: self.jieshou_get_parameters(event))
            pop_cmd(self)
        elif 'QAM' in button_name:
            self.drawbutton_list[self.button_num].bind('<Double-Button-1>',
                                                       lambda event: self.qam_get_parameters(event))
            pop_cmd(self)
        elif 'PAPR' in button_name:
            self.drawbutton_list[self.button_num].bind('<Double-Button-1>',
                                                       lambda event: self.papr_get_parameters(event))
            pop_cmd(self)
        elif '压扩' in button_name:
            self.drawbutton_list[self.button_num].bind('<Double-Button-1>',
                                                       lambda event: self.yakuo_get_parameters(event))
            pop_cmd(self)
        else:
            self.drawbutton_list[self.button_num].bind('<Double-Button-1>',
                                                       lambda event: self.button_get_parameters(event))
            cmd = 'self.' + button_name + '.x_label = 50 + 60 * (self.button_num % 15)'
            exec(cmd)
            cmd = 'self.' + button_name + '.y_label = 100'
            exec(cmd)
        self.button_num += 1

    def menu_handle(self):  # 暂无
        pass

    def popup_handle(self, event):  # 显示右键菜单
        self.pop_menu.post(event.x_root, event.y_root)

    def element_popup_handle(self, event):  # 暂无
        self.element_pop_menu.post(event.x_root, event.y_root)

    def pop_menu_handle(self):  # 暂无
        pass

    def element_move(self, event):  # 用于拖动按钮
        if self.move:
            name = event.widget['text']
            move_x = event.x_root - self.root.winfo_x() - 308
            move_y = event.y_root - self.root.winfo_y() - 100
            event.widget.place(x=move_x, y=move_y)
            element_name = ''
            for i in name:
                if i == '\n':
                    pass
                else:
                    element_name = element_name + i
            # ------------------------------------------------------
            # 将元件的坐标保存在节点中
            cmd = 'self.' + element_name + '.x_label = move_x'
            exec(cmd)
            cmd = 'self.' + element_name + '.y_label = move_y'
            exec(cmd)
            # ------------------------------------------------------

    def draw_lines(self, event):  # 绘图区用于连线
        if self.lianxian:
            self.grid1[0] = self.grid2[0]
            self.grid1[1] = self.grid2[1]
            self.grid2[0] = event.x
            self.grid2[1] = event.y
            if self.flag:
                if abs(self.grid2[0] - self.grid1[0]) > abs(self.grid2[1] - self.grid1[1]):
                    self.line_list.append(
                        self.canvas.create_line(self.grid1[0], self.grid1[1], self.grid2[0], self.grid1[1],
                                                arrow='last',
                                                arrowshape=(8, 15, 3)))
                    self.grid2[1] = self.grid1[1]
                else:
                    self.line_list.append(
                        self.canvas.create_line(self.grid1[0], self.grid1[1], self.grid1[0], self.grid2[1],
                                                arrow='last',
                                                arrowshape=(8, 15, 3)))
                    self.grid2[0] = self.grid1[0]
                self.line_num += 1

    def element_handle(self, event):  # 绘图区按钮绑定的事件，用于连线
        if self.lianxian:
            self.element_name1 = self.element_name2
            self.element_name = event.widget['text']
            self.element_name2 = ''
            for i in self.element_name:
                if i == '\n':
                    pass
                else:
                    self.element_name2 = self.element_name2 + i
            self.grid1[0] = self.grid2[0]
            self.grid1[1] = self.grid2[1]
            self.grid2[0] = event.x_root - self.root.winfo_x() - 308
            self.grid2[1] = event.y_root - self.root.winfo_y() - 100
            if self.flag:
                if abs(self.grid2[0] - self.grid1[0]) > abs(self.grid2[1] - self.grid1[1]):
                    self.line_list.append(
                        self.canvas.create_line(self.grid1[0], self.grid1[1], self.grid2[0], self.grid1[1],
                                                arrow='last',
                                                arrowshape=(8, 15, 3)))
                    self.line_list.append(
                        self.canvas.create_line(self.grid2[0], self.grid1[1], self.grid2[0], self.grid2[1],
                                                arrow='last',
                                                arrowshape=(8, 15, 3)))
                else:
                    self.line_list.append(
                        self.canvas.create_line(self.grid1[0], self.grid1[1], self.grid1[0], self.grid2[1],
                                                arrow='last',
                                                arrowshape=(8, 15, 3)))
                    self.line_list.append(
                        self.canvas.create_line(self.grid1[0], self.grid2[1], self.grid2[0], self.grid2[1],
                                                arrow='last',
                                                arrowshape=(8, 15, 3)))
                self.line_num += 2
            if self.flag == True:
                cmd = 'self.' + self.element_name1 + '.next = self.' + self.element_name2
                exec(cmd)
            self.flag = not self.flag

    def list_run(self, event):  # 运行事件
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置图片中的字体
        plt.rcParams['axes.unicode_minus'] = False  # 识别负号
        flag = True
        try:
            bit_list = []
            # 因为所有button名字都加了编号，用for找到对应类的按钮
            for i in self.drawbutton_list:
                if '发送' in i['text']:
                    cur=self.发送0  #随便设的，为了让他不报错
                    cmd='cur=self.'+i['text']
                    exec(cmd)
                    print(cur)
                    break

            n = int(cur.para1)
            for i in range(n):
                bit_list.append(random.randint(0, 1))
            #cur = self.发送
            print(str(cur.output))
            cur.output = bit_list
            plt.figure(figsize=(10, 5))
            plt.plot(cur.output, drawstyle='steps-pre')
            plt.grid()
            plt.savefig('./images/fasong.png')
        except:
            flag = False
            print('没有发送端')
        if flag == True:
            while cur.next is not None:
                last = cur
                cur = cur.next
                cur.input = last.output
                #print(cur.item)
                if 'QPSK'in cur.item:
                    cur.output = qpskmod(cur.input, int(cur.para1), int(cur.para2))
                    plt.figure(figsize=(10, 5))
                    plt.plot(cur.output)
                    plt.grid()
                    plt.savefig('./images/QPSKmod.png')
                elif 'QPSK解调' in cur.item:
                    cur.output = qpskdemod(cur.input, int(cur.para1), int(cur.para2))
                    plt.figure(figsize=(10, 5))
                    plt.plot(cur.output)
                    plt.grid()
                    plt.savefig('./images/QPSKdemod.png')
                elif cur.item == 'jieshou':
                    pass
                else:
                    pass

    def save_handle(self):
        self.save_window = tkinter.Toplevel()
        self.save_window.title("保存")
        self.save_window.geometry("500x450")
        self.save_window.resizable(width=False, height=False)

        self.label_file_name = tkinter.Label(self.save_window, text='文件名', font=('微软雅黑', 10))
        self.text_file_name = tkinter.Text(self.save_window, width=30, height=1, font=('微软雅黑', 10))
        self.text_file_name.insert("insert", "save1")
        self.text_file_name.place(x=150, y=100)
        self.label_file_name.place(x=100, y=100)
        self.label_file_address = tkinter.Label(self.save_window, text='地址', font=('微软雅黑', 10))
        self.text_file_address = tkinter.Text(self.save_window, width=30, height=1, font=('微软雅黑', 10))
        self.text_file_address.insert("insert", "./save_file/")
        self.label_file_address.place(x=100, y=200)
        self.text_file_address.place(x=150, y=200)

        self.save_determine = tkinter.Button(self.save_window, text='确定', width=4, font=('微软雅黑', 10))
        self.save_determine.bind('<ButtonRelease-1>', lambda event: self.save_file())
        self.save_determine.place(x=100, y=300)
        self.save_back = tkinter.Button(self.save_window, text='返回', width=4, font=('微软雅黑', 10))
        self.save_back.bind('<ButtonRelease-1>', lambda event: self.save_quit())
        self.save_back.place(x=300, y=300)

        self.save_window.mainloop()
        self.save_window.destroy()

    def save_file(self):
        empty = 0
        file_name = self.text_file_name.get('0.0', 'end')
        file_address = self.text_file_address.get('0.0', 'end')
        a = file_address + file_name + '.txt'
        file_path = ''
        for i in a:
            if i == '\n':
                pass
            else:
                file_path = file_path + i
        txt = open(file_path, 'w')
        try:
            cur = self.发送
        except:
            empty = 1
            self.save_window.quit()
        if empty == 0:
            txt.write(cur.item + ' ')
            try:
                txt.write(str(cur.next.item) + ' ')
            except:
                txt.write('None' + ' ')
            txt.write(str(cur.para1) + ' ')
            txt.write(str(cur.para2) + ' ')
            txt.write(str(cur.para3) + ' ')
            txt.write(str(cur.para4) + ' ')
            txt.write(str(cur.para5) + ' ')
            txt.write(str(cur.x_label) + ' ')
            txt.write(str(cur.y_label) + ' ')
            txt.write('\n')
            while cur.next is not None:
                cur = cur.next
                txt.write(cur.item + ' ')
                try:
                    txt.write(str(cur.next.item) + ' ')
                except:
                    txt.write('None' + ' ')
                txt.write(str(cur.para1) + ' ')
                txt.write(str(cur.para2) + ' ')
                txt.write(str(cur.para3) + ' ')
                txt.write(str(cur.para4) + ' ')
                txt.write(str(cur.para5) + ' ')
                txt.write(str(cur.x_label) + ' ')
                txt.write(str(cur.y_label) + ' ')
                txt.write('\n')

        self.save_window.quit()

    def save_quit(self):
        self.save_window.quit()

    def open_handle(self):
        self.open_window = tkinter.Toplevel()
        self.open_window.title("打开")
        self.open_window.geometry("500x450")
        self.open_window.resizable(width=False, height=False)

        self.label_file_name = tkinter.Label(self.open_window, text='文件名', font=('微软雅黑', 10))
        self.text_file_name = tkinter.Text(self.open_window, width=30, height=1, font=('微软雅黑', 10))
        self.text_file_name.insert("insert", "save1")
        self.text_file_name.place(x=150, y=100)
        self.label_file_name.place(x=100, y=100)
        self.label_file_address = tkinter.Label(self.open_window, text='地址', font=('微软雅黑', 10))
        self.text_file_address = tkinter.Text(self.open_window, width=30, height=1, font=('微软雅黑', 10))
        self.text_file_address.insert("insert", "./save_file/")
        self.label_file_address.place(x=100, y=200)
        self.text_file_address.place(x=150, y=200)

        self.open_determine = tkinter.Button(self.open_window, text='确定', width=4, font=('微软雅黑', 10))
        self.open_determine.bind('<ButtonRelease-1>', lambda event: self.open_file())
        self.open_determine.place(x=100, y=300)
        self.open_back = tkinter.Button(self.open_window, text='返回', width=4, font=('微软雅黑', 10))
        self.open_back.bind('<ButtonRelease-1>', lambda event: self.open_quit())
        self.open_back.place(x=300, y=300)

        self.open_window.mainloop()
        self.open_window.destroy()

    def open_file(self):
        empty = 0
        file_name = self.text_file_name.get('0.0', 'end')
        file_address = self.text_file_address.get('0.0', 'end')
        a = file_address + file_name + '.txt'
        file_path = ''
        for i in a:
            if i == '\n':
                pass
            else:
                file_path = file_path + i
        txt = open(file_path, 'r')
        data = txt.readlines()
        for line in data:
            element = line.split()[0]
            cmd = 'self.' + element + ' = Node(\'' + element + '\')'
            exec(cmd)
        for line in data:
            element = line.split()[0]
            try:
                cmd = 'self.' + element + '.next = self.' + line.split()[1]
                exec(cmd)
            except:
                cmd = 'self.' + element + '.next = None'
                exec(cmd)
            cmd = 'self.' + element + '.para1 = ' + line.split()[2]
            exec(cmd)
            cmd = 'self.' + element + '.para2 = ' + line.split()[3]
            exec(cmd)
            cmd = 'self.' + element + '.para3 = ' + line.split()[4]
            exec(cmd)
            cmd = 'self.' + element + '.para4 = ' + line.split()[5]
            exec(cmd)
            cmd = 'self.' + element + '.para5 = ' + line.split()[6]
            exec(cmd)
            cmd = 'self.' + element + '.x_label = ' + line.split()[7]
            exec(cmd)
            cmd = 'self.' + element + '.y_label = ' + line.split()[8]
            exec(cmd)

        try:
            cur = self.发送
        except:
            empty = 1
        if empty == 0:
            self.drawbutton_list.append(
                tkinter.Button(self.draw_frame, text='发送', fg='black', width='5', height='2', font=('微软雅黑', 10)))
            self.drawbutton_list[0].place(x=cur.x_label, y=cur.y_label)
            self.drawbutton_list[0].bind('<ButtonRelease-1>',
                                         lambda event: self.element_handle(event))  # 点击连线
            self.drawbutton_list[0].bind('<B1-Motion>',
                                         lambda event: self.element_move(event))  # 移动元件
            self.drawbutton_list[0].bind('<Double-Button-1>',
                                         lambda event: self.fasong_get_parameters(event))
            button_num = 0
            while cur.next is not None:
                last = cur
                cur = cur.next
                if cur.item == 'QPSK解调':
                    self.drawbutton_list.append(
                        tkinter.Button(self.draw_frame, text='QPSK\n解调', fg='black', width='5', height='2',
                                       font=('微软雅黑', 10)))
                    button_num += 1
                else:
                    self.drawbutton_list.append(
                        tkinter.Button(self.draw_frame, text=cur.item, fg='black', width='5', height='2',
                                       font=('微软雅黑', 10)))
                    button_num += 1
                self.drawbutton_list[button_num].place(x=cur.x_label, y=cur.y_label)

                self.line_list.append(
                    self.canvas.create_line(last.x_label, last.y_label, cur.x_label, last.y_label, arrow='last',
                                            arrowshape=(8, 15, 3)))
                self.line_list.append(
                    self.canvas.create_line(cur.x_label, last.y_label, cur.x_label, cur.y_label, arrow='last',
                                            arrowshape=(8, 15, 3)))

                self.drawbutton_list[self.button_num].bind('<ButtonRelease-1>',
                                                           lambda event: self.element_handle(event))  # 点击连线
                self.drawbutton_list[self.button_num].bind('<B1-Motion>',
                                                           lambda event: self.element_move(event))  # 移动元件

                if cur.item == 'QPSK':
                    self.drawbutton_list[button_num].bind('<Double-Button-1>',
                                                          lambda event: self.qpsk_get_parameters(event))
                elif cur.item == 'QPSK解调':
                    self.drawbutton_list[button_num].bind('<Double-Button-1>',
                                                          lambda event: self.qpsk_get_parameters(event))
                else:
                    self.drawbutton_list[button_num].bind('<Double-Button-1>',
                                                          lambda event: self.button_get_parameters(event))

        self.open_window.quit()

    def open_quit(self):
        self.open_window.quit()

    def button_get_parameters(self, event):
        if self.tiaocan == True:
            try:
                os.system("python fasong_para.py")
                para1 = np.load('tmp1.npy')
                os.remove('tmp1.npy')
                para2 = np.load('tmp2.npy')
                os.remove('tmp2.npy')

                button_name = event.widget['text']
                cmd = 'self.' + button_name + '.para1 = para1'
                exec(cmd)
                cmd = 'self.' + button_name + '.para2 = para2'
                exec(cmd)
            except:
                pass

    def fasong_get_parameters(self, event):
        if self.tiaocan == True:
            try:
                os.system("python para_fasong.py")
                para1 = np.load('tmp1.npy')
                os.remove('tmp1.npy')

                button_name = event.widget['text']
                cmd = 'self.' + button_name + '.para1 = para1'
                exec(cmd)
            except:
                pass

    def qpsk_get_parameters(self, event):
        if self.tiaocan == True:
            try:
                os.system("python para_qpsk.py")
                para1 = np.load('tmp1.npy')
                os.remove('tmp1.npy')
                para2 = np.load('tmp2.npy')
                os.remove('tmp2.npy')

                button = event.widget['text']
                button_name = ''
                for i in button:
                    if i == '\n':
                        pass
                    else:
                        button_name = button_name + i

                cmd = 'self.' + button_name + '.para1 = para1'
                exec(cmd)
                cmd = 'self.' + button_name + '.para2 = para2'
                exec(cmd)
            except:
                pass

    def jieshou_get_parameters(self, event):
        if self.tiaocan == True:
            try:
                os.system("python para_jieshou.py")
                para1 = np.load('tmp1.npy')
                os.remove('tmp1.npy')
                para2 = np.load('tmp2.npy')
                os.remove('tmp2.npy')

                button = event.widget['text']
                button_name = ''
                for i in button:
                    if i == '\n':
                        pass
                    else:
                        button_name = button_name + i

                cmd = 'self.' + button_name + '.para1 = para1'
                exec(cmd)
                cmd = 'self.' + button_name + '.para2 = para2'
                exec(cmd)
            except:
                pass

    def qam_get_parameters(self, event):
        if self.tiaocan == True:
            try:
                os.system("python para_QAM.py")
                para1 = np.load('tmp1.npy')
                os.remove('tmp1.npy')
                para2 = np.load('tmp2.npy')
                os.remove('tmp2.npy')

                button = event.widget['text']
                button_name = ''
                for i in button:
                    if i == '\n':
                        pass
                    else:
                        button_name = button_name + i

                cmd = 'self.' + button_name + '.para1 = para1'
                exec(cmd)
                cmd = 'self.' + button_name + '.para2 = para2'
                exec(cmd)
            except:
                pass

    def papr_get_parameters(self, event):
        if self.tiaocan == True:
            try:
                os.system("python para_PAPR.py")
                para1 = np.load('tmp1.npy')
                os.remove('tmp1.npy')
                para2 = np.load('tmp2.npy')
                os.remove('tmp2.npy')

                button = event.widget['text']
                button_name = ''
                for i in button:
                    if i == '\n':
                        pass
                    else:
                        button_name = button_name + i

                cmd = 'self.' + button_name + '.para1 = para1'
                exec(cmd)
                cmd = 'self.' + button_name + '.para2 = para2'
                exec(cmd)
            except:
                pass

    def yakuo_get_parameters(self, event):
        if self.tiaocan == True:
            try:
                os.system("python para_yakuo.py")
                para1 = np.load('tmp1.npy')
                os.remove('tmp1.npy')
                para2 = np.load('tmp2.npy')
                os.remove('tmp2.npy')

                button = event.widget['text']
                button_name = ''
                for i in button:
                    if i == '\n':
                        pass
                    else:
                        button_name = button_name + i

                cmd = 'self.' + button_name + '.para1 = para1'
                exec(cmd)
                cmd = 'self.' + button_name + '.para2 = para2'
                exec(cmd)
            except:
                pass

    # 加个参数，记录已经跑过数据的元件个数，避免一个元件数据被多次调用

    def Oscilloscope(self):
        self.min = 0
        self.max = 0
        self.now = 0
        # ------------------------------------------------------------------------------------
        self.oscilloscope = tkinter.Toplevel()
        self.oscilloscope.title("示波器")
        self.oscilloscope.geometry("1000x750")
        self.oscilloscope.resizable(width=False, height=False)
        # ------------------------------------------------------------------------------------
        self.wave_frame = tkinter.Frame(self.oscilloscope, width=1000, height=500, bg='white')
        self.wave_frame.place(x=0, y=0)
        self.label_img = tkinter.Label(self.wave_frame)
        self.label_img.bind("<MouseWheel>", lambda event: self.wheel_handle(event))
        self.label_img.pack()
        # ------------------------------------------------------------------------------------
        self.ctrl_frame = tkinter.Frame(self.oscilloscope, width=1000, height=250)
        self.ctrl_frame.place(x=0, y=500)

        self.wave_tuple = []
        try:
            # 因为所有button名字都加了编号，用for找到对应类的按钮
            for i in self.drawbutton_list:
                if '发送' in i['text']:
                    cur = self.发送0  # 随便设的，为了让他不报错
                    cmd = 'cur=self.' + i['text']
                    exec(cmd)
                    print(cur)
                    #break
            self.wave_tuple.append(cur.item)
            while cur.next is not None:
                cur = cur.next
                self.wave_tuple.append(cur.item)
        except:
            pass
            self.wave_tuple = tuple(self.wave_tuple)
        self.wave_combobox = tkinter.ttk.Combobox(self.ctrl_frame, values=self.wave_tuple)
        self.wave_combobox.bind('<<ComboboxSelected>>', self.wave_combobox_handle)
        self.wave_combobox.place(x=150, y=50)

        self.label_text1 = tkinter.Label(self.ctrl_frame, text='起始位置', font=('微软雅黑', 10))
        self.label_text2 = tkinter.Label(self.ctrl_frame, text='结束位置', font=('微软雅黑', 10))
        self.label_text1.place(x=400, y=50)
        self.label_text2.place(x=400, y=100)
        self.text_start = tkinter.Text(self.ctrl_frame, width=15, height=1, font=('微软雅黑', 10))
        self.text_end = tkinter.Text(self.ctrl_frame, width=15, height=1, font=('微软雅黑', 10))
        self.text_start.place(x=475, y=50)
        self.text_end.place(x=475, y=100)
        self.text_start.insert("insert", self.min)
        self.text_end.insert("insert", self.max)
        self.range_button = tkinter.Button(self.ctrl_frame, text='确定', font=('微软雅黑', 10))
        self.range_button.bind('<ButtonRelease-1>', lambda event: self.get_range())
        self.range_button.place(x=700, y=50)
        # ------------------------------------------------------------------------------------
        self.oscilloscope.mainloop()

    def wave_combobox_handle(self, event):
        wave_name = self.wave_combobox.get()
        #print(f'wave_naem={wave_name}')
        if '发送' in wave_name:
            img = Image.open('./images/fasong.png')
            self.image_png = ImageTk.PhotoImage(img)
            self.label_img.configure(image=self.image_png)
            self.min = 0
            for i in self.drawbutton_list[self.finished_element :]:
                if '发送' in i['text']:
                    now = self.发送0  # 随便设的，为了让他不报错
                    cmd = 'now=self.' + i['text']
                    exec(cmd)
                    break
            self.finished_element+=1

            self.max = len(now.output)
            self.x_label = range(self.max)
            self.text_start.delete('1.0', 'end')
            self.text_end.delete('1.0', 'end')
            self.text_start.insert("insert", self.min)
            self.text_end.insert("insert", self.max)
        elif 'QPSK' in wave_name and wave_name[4] in (str(shuzi) for shuzi in range(10)):
            img = Image.open('./images/QPSKmod.png')
            self.image_png = ImageTk.PhotoImage(img)
            self.label_img.configure(image=self.image_png)
            self.min = 0
            for i in self.drawbutton_list[self.finished_element :]:
                if 'QPSK' in i['text'] and i['text'][4] in (str(shuzi) for shuzi in range(10)):
                    now = self.发送0  # 随便设的，为了让他不报错
                    cmd = 'now=self.' + i['text']
                    exec(cmd)
                    break
            self.finished_element += 1

            self.max = len(now.output)
            self.x_label = range(self.max)
            self.text_start.delete('1.0', 'end')
            self.text_end.delete('1.0', 'end')
            self.text_start.insert("insert", self.min)
            self.text_end.insert("insert", self.max)
        elif 'QPSK解调' in wave_name:
            img = Image.open('./images/QPSKdemod.png')
            self.image_png = ImageTk.PhotoImage(img)
            self.label_img.configure(image=self.image_png)
            self.min = 0
            for i in self.drawbutton_list[self.finished_element :]:
                if 'QPSK解调' in i['text']:
                    now = self.发送0  # 随便设的，为了让他不报错
                    cmd = 'now=self.' + i['text']
                    exec(cmd)
                    break
            self.finished_element += 1

            self.max = len(now.output)
            self.x_label = range(self.max)
            self.text_start.delete('1.0', 'end')
            self.text_end.delete('1.0', 'end')
            self.text_start.insert("insert", self.min)
            self.text_end.insert("insert", self.max)
        else:
            pass
        self.maxi = self.max

    def get_range(self):
        start = self.text_start.get('0.0', 'end')
        end = self.text_end.get('0.0', 'end')
        wave_name = self.wave_combobox.get()
        if '发送' in wave_name:
            plt.figure(figsize=(10, 5))
            for i in self.drawbutton_list:
                if '发送' in i['text']:
                    now_1 = self.发送0  # 随便设的，为了让他不报错
                    cmd = 'now_1=self.' + i['text']
                    exec(cmd)
                    #break
            plt.plot(self.x_label[int(start):int(end)], now_1.output[int(start):int(end)], drawstyle='steps-pre')
            plt.grid()
            plt.savefig('./images/fasong2.png')
            self.min = start
            self.max = end
            img = Image.open('./images/fasong2.png')
            self.image_png = ImageTk.PhotoImage(img)
            self.label_img.configure(image=self.image_png)
        elif 'QPSK' in wave_name and wave_name[4] in (str(shuzi) for shuzi in range(10)):
            plt.figure(figsize=(10, 5))
            for i in self.drawbutton_list:
                if 'QPSK' in i['text'] and i['text'][4] in (str(shuzi) for shuzi in range(10)):
                    now_1 = self.发送0  # 随便设的，为了让他不报错
                    cmd = 'now_1=self.' + i['text']
                    exec(cmd)
                    #break
            plt.plot(self.x_label[int(start):int(end)], now_1.output[int(start):int(end)])
            plt.grid()
            plt.savefig('./images/QPSKmod2.png')
            self.min = start
            self.max = end
            img = Image.open('./images/QPSKmod2.png')
            self.image_png = ImageTk.PhotoImage(img)
            self.label_img.configure(image=self.image_png)
        elif  'QPSK解调' in wave_name:
            plt.figure(figsize=(10, 5))
            for i in self.drawbutton_list:
                if 'QPSK解调' in i['text']:
                    now_1 = self.发送0  # 随便设的，为了让他不报错
                    cmd = 'now=self.' + i['text']
                    exec(cmd)
                    #break
            plt.plot(self.x_label[int(start):int(end)], now_1.output[int(start):int(end)])
            plt.grid()
            plt.savefig('./images/QPSKdemod2.png')
            self.min = start
            self.max = end
            img = Image.open('./images/QPSKdemod2.png')
            self.image_png = ImageTk.PhotoImage(img)
            self.label_img.configure(image=self.image_png)
        else:
            pass

    def wheel_handle(self, event):
        wave_name = self.wave_combobox.get()
        self.max = int(self.max)
        self.min = int(self.min)
        len = self.max - self.min
        self.now = int(self.min) + len * (event.x - 162) / 713

        if event.delta > 0:  # 滚轮向上滚动，放大
            self.min = int(self.min + len * (event.x - 162) / 713 / 4)
            self.max = int(self.max - len * (875 - event.x) / 713 / 4)
            if ((self.max - self.min) < 10):
                self.max = int(self.now + 10 * (875 - event.x) / 713)
                self.min = int(self.now - 10 * (event.x - 162) / 713)
            self.text_start.delete('1.0', 'end')
            self.text_end.delete('1.0', 'end')
            self.text_start.insert("insert", self.min)
            self.text_end.insert("insert", self.max)
        else:  # 滚轮向下滚动，缩小
            self.min = int(self.min - len * (event.x - 162) / 713 / 4)
            self.max = int(self.max + len * (875 - event.x) / 713 / 4)
            if self.min < 0:
                self.min = 0
            if self.max > self.maxi:
                self.max = self.maxi
            self.text_start.delete('1.0', 'end')
            self.text_end.delete('1.0', 'end')
            self.text_start.insert("insert", self.min)
            self.text_end.insert("insert", self.max)

        if '发送'in wave_name:
            plt.figure(figsize=(10, 5))
            for i in self.drawbutton_list:
                if '发送' in i['text']:
                    now_2 = self.发送0  # 随便设的，为了让他不报错
                    cmd = 'now_2=self.' + i['text']
                    exec(cmd)
                    #break
            plt.plot(self.x_label[self.min:self.max], now_2.output[self.min:self.max], drawstyle='steps-pre')
            plt.grid()
            plt.savefig('./images/fasong2.png')
            img = Image.open('./images/fasong2.png')
            self.image_png = ImageTk.PhotoImage(img)
            self.label_img.configure(image=self.image_png)
        elif 'QPSK' in wave_name and wave_name[4] in (str(shuzi) for shuzi in range(10)):
            plt.figure(figsize=(10, 5))
            for i in self.drawbutton_list:
                if 'QPSK' in i['text'] and i['text'][4] in (str(shuzi) for shuzi in range(10)):
                    now_2 = self.发送0  # 随便设的，为了让他不报错
                    cmd = 'now_2=self.' + i['text']
                    exec(cmd)
                    #break
            plt.plot(self.x_label[self.min:self.max], now_2.output[self.min:self.max])
            plt.grid()
            plt.savefig('./images/QPSKmod2.png')
            img = Image.open('./images/QPSKmod2.png')
            self.image_png = ImageTk.PhotoImage(img)
            self.label_img.configure(image=self.image_png)
        elif 'QPSK解调' in wave_name:
            plt.figure(figsize=(10, 5))
            for i in self.drawbutton_list:
                if 'QPSK解调' in i['text']:
                    now_2 = self.发送0  # 随便设的，为                       了让他不报错
                    cmd = 'now_2=self.' + i['text']
                    exec(cmd)
                    #break
            plt.plot(self.x_label[self.min:self.max], now_2.output[self.min:self.max])
            plt.grid()
            plt.savefig('./images/QPSKdemod2.png')
            img = Image.open('./images/QPSKdemod2.png')
            self.image_png = ImageTk.PhotoImage(img)
            self.label_img.configure(image=self.image_png)
        else:
            pass


def main():
    MainPage()


if __name__ == '__main__':
    main()
