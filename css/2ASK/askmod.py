import numpy as np
from math import pi
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import math
from awgn import awgn


def askmod(n, fc, fs):  # n为码元数，fc为载波频率，fs为采样频率
    sampling_t = 0.01
    t = np.arange(0, n, sampling_t)
    # 随机生成信号序列
    a = np.random.randint(0, 2, n)
    bitstream = np.zeros(len(t), dtype=np.float32)
    for i in range(len(t)):
        bitstream[i] = a[math.floor(t[i])]
    fig = plt.figure()
    fig.add_subplot(3, 1, 1)
    # 解决中文乱码
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置图片中的字体
    plt.rcParams['axes.unicode_minus'] = False  # 识别负号
    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.axis([0, n, -0.5, 1.5])
    plt.plot(t, bitstream, 'b')
    ts = np.arange(0, (100 * n) / fs, 1 / fs)
    ask = bitstream * np.cos(np.dot(2 * pi * fc, ts))
    # 2ASK调制信号波形
    ax2 = fig.add_subplot(3, 1, 2)
    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
    ax2.set_title('2ASK调制信号')
    plt.axis([0, n, -1.5, 1.5])
    plt.plot(t, ask, 'r')
    # 加AWGN噪声
    noise_ask = awgn(ask, 5)

    # 2ASK调制信号叠加噪声波形
    ax3 = fig.add_subplot(3, 1, 3)
    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax3.set_title('2ASK调制信号叠加噪声波形')
    plt.axis([0, n, -1.5, 1.5])
    plt.plot(t, noise_ask, 'r')
    #plt.savefig('2ask调制', dpi=300)
    plt.show()
    return ask


# _2askmod(10, 4000, 80000)
