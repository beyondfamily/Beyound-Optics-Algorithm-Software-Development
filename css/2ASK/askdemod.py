import numpy as np
from math import pi
import matplotlib.pyplot as plt
import scipy.signal as signal
from matplotlib.pyplot import MultipleLocator
from askmod import askmod
from awgn import awgn


def askdemod(x, fc, fs):  # x为2ask信号,fc为载波频率，fs为采样频率
    # 带通椭圆滤波器设计，通带为[2000，6000]
    [b11, a11] = signal.ellip(5, 0.5, 60, [fc / 2 / fs, 3 * fc / fs], btype='bandpass', analog=False, output='ba')

    # 低通滤波器设计，通带截止频率为2000Hz
    [b12, a12] = signal.ellip(5, 0.5, 60, (fc / 2 / fs), btype='lowpass', analog=False, output='ba')

    # 通过带通滤波器滤除带外噪声
    bandpass_out = signal.filtfilt(b11, a11, x)

    # 相干解调,乘以同频同相的相干载波
    n = int(len(x)/100)
    sampling_t = 0.01
    t = np.arange(0, n, sampling_t)
    ts = np.arange(0, (100 * n) / fs, 1 / fs)
    coherent_carrier = np.cos(np.dot(2 * pi * fc, ts))
    coherent_demod = bandpass_out * (coherent_carrier * 2)

    # 通过低通滤波器
    lowpass_out = signal.filtfilt(b12, a12, coherent_demod)
    # 解决中文乱码
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置图片中的字体
    plt.rcParams['axes.unicode_minus'] = False  # 识别负号
    fig2 = plt.figure()
    bx1 = fig2.add_subplot(2, 1, 1)
    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    bx1.set_title('2ASK信号相干解调后、抽样判决前的信号')
    plt.axis([0, n, -1.5, 1.5])
    plt.plot(t, lowpass_out, 'r')

    # 抽样判决
    detection_2ask = np.zeros(len(t), dtype=np.float32)
    flag = np.zeros(n, dtype=np.float32)

    for i in range(n):
        tempF = 0
        for j in range(100):
            tempF = tempF + lowpass_out[i * 100 + j]
        if tempF > 50:
            flag[i] = 1
        else:
            flag[i] = 0
    for i in range(n):
        if flag[i] == 0:
            for j in range(100):
                detection_2ask[i * 100 + j] = 0
        else:
            for j in range(100):
                detection_2ask[i * 100 + j] = 1

    bx2 = fig2.add_subplot(2, 1, 2)
    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    bx2.set_title('2ASK信号抽样判决后的信号')
    plt.axis([0, n, -0.5, 1.5])
    plt.plot(t, detection_2ask, 'r')
    #plt.savefig('2ask解调', dpi=300)
    plt.show()

x = askmod(20,4000,80000)
y = awgn(x, 5)
askdemod(y, 4000, 80000)
