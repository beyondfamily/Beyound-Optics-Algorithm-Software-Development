from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import math


def qpskdemod(x, fc, fs):
    T = 1
    N = 2*int(len(x))
    nb = int(N/fs)
    a = []  # 余弦函数载波
    b = []  # 正弦函数载波
    delta_T = 1 / fs  # 采样间隔
    t1 = np.arange(0, nb, delta_T)
    t = np.arange(0, nb * T, delta_T)
    for j in range(int(N / 2)):
        a.append(np.math.sqrt(2 / T) * np.math.cos(2 * np.math.pi * fc * t[j]))  # 余弦函数载波
        b.append(np.math.sqrt(2 / T) * np.math.sin(2 * np.math.pi * fc * t[j]))  # 正弦函数载波
    idata2 = x * np.array(a)
    qdata2 = x * np.array(b)

    # 低通滤波
    [b, a] = signal.butter(2, 2 * fc / fs)
    idata22 = signal.filtfilt(b, a, idata2)
    qdata22 = signal.filtfilt(b, a, qdata2)
    demodata0 = idata22 + qdata22

    idata3 = []  # 建立1*nb/2数组，以存放判决之后的奇信号
    qdata3 = []  # 建立1*nb/2数组，以存放判决之后的偶信号
    # 抽样判决的过程，与0作比较，data> = 0,  则置1，否则置0
    for i in range(int(nb / 2)):
        if np.sum(idata22[i * int(1 / delta_T):(i + 1) * int(1 / delta_T)]) >= 0:
            idata3.append(1)
        else:
            idata3.append(0)
        if np.sum(qdata22[i * int(1 / delta_T):(i + 1) * int(1 / delta_T)]) >= 0:
            qdata3.append(1)
        else:
            qdata3.append(0)

    # 将判决后的数据存放进数据组
    demodata = []
    for i in range(nb):
        if i % 2 == 0:
            demodata.append(idata3[i // 2])  # 并串变换，存放奇数位
        else:
            demodata.append(qdata3[i // 2])  # 并串变换，存放偶数位

    demodata1 = []  # 创建一个1*nb/delta_T的零矩阵
    for i in range(nb):
        demodata1 += [demodata[i]]

    demodata2 = np.zeros(len(t1), dtype=np.float32)
    for i in range(len(t1)):
        demodata2[i] = demodata1[math.floor(t1[i])]

    #plt.figure(2)
    #plt.subplot(2, 1, 1)
    #plt.plot(demodata0)
    #plt.title('解调输出', fontsize=10)
    #plt.axis([0, 5000, -4, 4])
    #plt.plot(t1, demodata2)
    #plt.subplot(2, 1, 2)
    #plt.title('抽样判决后的解调信号', fontsize=10)
    #plt.plot(t1, demodata2)
    #plt.axis([0, 100, -2, 2])
    #plt.tight_layout()
    #plt.savefig('qpsk解调', dpi=300)
    #plt.show()
    return demodata2

