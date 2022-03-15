import numpy as np
from math import pi
import matplotlib.pyplot as plt
from matplotlib import font_manager
import scipy.signal as signal


def bpskdemod(x, fc, fs):
    # 带通椭圆滤波器设计，   通带为[2000，   6000]
    [b11, a11] = signal.ellip(5, 0.5, 60, [fc / 2 / fs, 3 * fc / fs], btype='bandpass', analog=False,
                              output='ba')

    # 低通滤波器设计，   通带截止频率为2000Hz
    [b12, a12] = signal.ellip(5, 0.5, 60, (fc / 2 / fs), btype='lowpass', analog=False, output='ba')

    # 通过带通滤波器滤除带外噪声
    bandpass_out = signal.filtfilt(b11, a11, x)

    # 相干解调, 乘以同频同相的相干载波
    n = int(len(x) / 100)
    sampling_t = 0.01
    t = np.arange(0, n, sampling_t)
    ts = np.arange(0, (100 * n) / fs, 1 / fs)
    coherent_carrier = np.cos(np.dot(2 * pi * fc, ts))
    coherent_demod = bandpass_out * (coherent_carrier * 2)

    # 通过低通滤波器
    lowpass_out = signal.filtfilt(b12, a12, coherent_demod)
    fig2 = plt.figure()
    zhfont1 = font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')
    bx1 = fig2.add_subplot(2, 1, 1)
    bx1.set_title('本地载波下变频，   经低通滤波器后', fontproperties=zhfont1, fontsize=10)
    plt.axis([0, n, -1.5, 1.5])
    plt.plot(t, lowpass_out, 'r')

    #  抽样判决
    detection_bpsk = np.zeros(len(t), dtype=np.float32)
    flag = np.zeros(n, dtype=np.float32)

    for i in range(n):
        tempF = 0
        for j in range(100):
            tempF = tempF + lowpass_out[i * 100 + j]
        if tempF > 0:
            flag[i] = 1
        else:
            flag[i] = 0

    for i in range(n):
        if flag[i] == 0:
            for j in range(100):
                detection_bpsk[i * 100 + j] = 0
        else:
            for j in range(100):
                detection_bpsk[i * 100 + j] = 1

    bx2 = fig2.add_subplot(2, 1, 2)
    bx2.set_title('BPSK信号抽样判决后的信号', fontproperties=zhfont1, fontsize=10)
    plt.axis([0, n, -0.5, 1.5])
    plt.plot(t, detection_bpsk, 'r')
    plt.tight_layout()
    plt.savefig('bpsk解调', dpi=300)
    plt.show()
    return detection_bpsk

