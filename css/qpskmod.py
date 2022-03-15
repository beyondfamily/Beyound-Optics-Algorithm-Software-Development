import numpy as np
import matplotlib.pyplot as plt
import math
from awgn import awgn


def qpskmod(x, fc, fs):
    T = 1  # 基带信号宽度
    delta_T = 1 / fs  # 采样间隔
    nb = len(x)
    t1 = np.arange(0, nb, delta_T)
    t = np.arange(0, nb * T, delta_T)
    N = len(t)

    data = np.zeros(len(t1), dtype=np.float32)
    for i in range(len(t1)):
        data[i] = x[math.floor(t1[i])]

    datanrz = np.array(x) * 2 - 1

    idata = datanrz[0:(nb - 1):2]  # 串并转换，将奇偶位分开，间隔为2，i是奇位 q是偶位
    qdata = datanrz[1:nb:2]
    ich = []  # 创建一个1*nb/delta_T/2的零矩阵，以便后面存放奇偶位数据
    qch = []
    for i in range(int(nb / 2)):
        ich += [idata[i]] * int(1 / delta_T)  # 奇位码元转换为对应的波形信号
        qch += [qdata[i]] * int(1 / delta_T)  # 偶位码元转换为对应的波形信号

    a = []  # 余弦函数载波
    b = []  # 正弦函数载波
    for j in range(int(N / 2)):
        a.append(np.math.sqrt(2 / T) * np.math.cos(2 * np.math.pi * fc * t[j]))  # 余弦函数载波
        b.append(np.math.sqrt(2 / T) * np.math.sin(2 * np.math.pi * fc * t[j]))  # 正弦函数载波
    idata1 = np.array(ich) * np.array(a)  # 奇数位数据与余弦函数相乘，得到一路的调制信号
    qdata1 = np.array(qch) * np.array(b)  # 偶数位数据与正弦函数相乘，得到另一路的调制信号
    s = idata1 + qdata1

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置图片中的字体
    plt.rcParams['axes.unicode_minus'] = False  # 识别负号

    #plt.figure(1)
    #plt.subplot(5, 1, 1)
    #plt.plot(t1, data)
    #plt.title('原信号', fontsize=10)
    #plt.axis([0, 100, -2, 2])
    #plt.subplot(5, 1, 2)
    #plt.plot(idata1)
    #plt.title('同相支路I', fontsize=10)
    #plt.axis([0, 500, -3, 3])
    #plt.subplot(5, 1, 3)
    #plt.plot(qdata1)
    #plt.title('正交支路Q', fontsize=10)
    #plt.axis([0, 500, -3, 3])
    #plt.subplot(5, 1, 4)
    #plt.plot(s)
    #plt.title('调制信号', fontsize=10)
    #plt.axis([0, 500, -3, 3])
    # 引入高斯噪声
    s1 = awgn(s, 15)
    #plt.subplot(5, 1, 5)
    #plt.plot(s1)
    #plt.title('调制信号(Awgn)', fontsize=10)
    #plt.tight_layout()
    #plt.savefig('qpsk调制', dpi=300)
    return s1
