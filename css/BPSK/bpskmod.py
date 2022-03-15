import numpy as np
from math import pi
import matplotlib.pyplot as plt
from matplotlib import font_manager
import math
from awgn import awgn


def bpskmod(n, fc, fs):  # n为码元数，fc为载波频率，fs为采样频率
    sampling_t = 0.01
    t = np.arange(0, n, sampling_t)

    # 随机生成信号序列
    a = np.random.randint(0, 2, n)
    m = np.zeros(len(t), dtype=np.float32)

    for i in range(len(t)):
        m[i] = a[math.floor(t[i])]

    fig = plt.figure()
    ax1 = fig.add_subplot(3, 1, 1)
    zhfont1 = font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')
    ax1.set_title('产生随机n位二进制信号', fontproperties=zhfont1, fontsize=10)
    plt.axis([0, n, -0.5, 1.5])
    plt.plot(t, m, 'b')

    ts = np.arange(0, (100 * n) / fs, 1 / fs)
    bpsk = np.cos(np.dot(2 * pi * fc, ts) + pi * (m - 1) + pi / 4)

    # BPSK调制信号波形
    ax2 = fig.add_subplot(3, 1, 2)
    ax2.set_title('BPSK调制信号', fontproperties=zhfont1, fontsize=10)
    plt.axis([0, n, -1.5, 1.5])
    plt.plot(t, bpsk, 'r')

    # 加AWGN噪声
    noise_bpsk = awgn(bpsk, 5)

    # BPSK调制信号叠加噪声波形
    ax3 = fig.add_subplot(3, 1, 3)
    ax3.set_title('BPSK调制信号叠加噪声波形', fontproperties=zhfont1, fontsize=10)
    plt.axis([0, n, -1.5, 1.5])
    plt.plot(t, noise_bpsk, 'r')
    plt.tight_layout()
    plt.savefig('bpsk调制', dpi=300)
    plt.show()
    return noise_bpsk


