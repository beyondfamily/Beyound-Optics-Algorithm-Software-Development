import numpy as np
import random
import pylab as plt
import math
from awgn import wgn

def qam4mod(n, SNR):
    bit_list = []
    for i in range(n):
        bit_list.append(random.randint(0, 1))
    input = np.array(bit_list)
    reshaped_input = np.reshape(input, (int(n / 2), 2))  # 每四组为一行

    def _trans_(_a, _b):
        return 2*_a + _b
    _map_ = dict([('0', (-math.sqrt(2)/2, -math.sqrt(2)/2)), ('1', (-math.sqrt(2)/2, math.sqrt(2)/2)), ('2', (math.sqrt(2)/2, -math.sqrt(2)/2)), ('3', (math.sqrt(2)/2, math.sqrt(2)/2))])

    qam_output_list = []     #星座图点位置
    qam_output_shishu = []   #星座图序号
    for i in range(int(n / 2)):
        num = _trans_(reshaped_input[i][0], reshaped_input[i][1])
        transed_num = complex(_map_[str(num)][0], _map_[str(num)][1])  # complex函数转换成复数形式，代表I Q两路
        qam_output_list.append(transed_num)
        qam_output_shishu.append(num)

    qam_output_array = np.array(qam_output_list)  # 将列表变为数组,完成16QAM调制
    qam_output_shishu = np.array(qam_output_shishu)  # 映射关系图,存放二进制转换为十进制的数据

    qam_output_real_array = qam_output_array.real  # 画图做准备
    qam_output_imag_array = qam_output_array.imag

    TX_array = wgn(qam_output_array, SNR)

    TX_re_real_array = TX_array.real
    TX_re_imag_array = TX_array.imag

    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10, 16))
    plt.subplot(211)
    plt.scatter(qam_output_real_array[0:int(n / 2)], qam_output_imag_array[0:int(n / 2)])
    plt.title('4QAM 调制')
    plt.subplot(212)
    plt.scatter(TX_re_real_array[0:int(n / 2)], TX_re_imag_array[0:int(n / 2)])
    plt.title('接收端')
    plt.show()

    return TX_array



def qam4demod(x):
    x_real = x.real
    x_imag = x.imag
    angle = math.atan2(x_real, x_imag)
    if 0 < angle < math.pi / 2:
        x = math.sqrt(2)/2 + math.sqrt(2)/2j   #3
        #x = "11"

    elif math.pi/2 < angle < math.pi:
        x = -math.sqrt(2)/2 + math.sqrt(2)/2j   #1

        #x = "01"
    elif -math.pi < angle < -math.pi/2:
        x = -math.sqrt(2)/2 - math.sqrt(2)/2j   #0

        #x = "00"
    else:
        x = math.sqrt(2)/2 - math.sqrt(2)/2j  # 2

        #x = "10"
    return x

TX_array = qam4mod(4000, 20)
y = []
for x in TX_array:
    y.append(qam4demod(x))

y = np.array(y)
# s = ''.join(y)
# print(s)

# for i in range(len(y)):
#     j = 0
#     if TX_array[i] == y[i]:
#         j += 1
#     ber = j / len(y)
# print(ber)
plt.scatter(y.real, y.imag)
plt.show()
