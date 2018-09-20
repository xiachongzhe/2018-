# -*- coding: utf-8 -*-

import numpy as np

# 调用numpy库
number = np.loadtxt("Semifinal-testing-final.csv", dtype=np.str, delimiter=",")
# 读取数据文件，以str类型接收（以逗号分隔）
fw = open('dsjyycxds_semifinal.txt', 'w')
# 写入提交文件

# 如果数据有牌值为 J,Q,K 的牌，转化成对应值
elven = (number == 'J')
number[elven] = '11'
twelve = (number == 'Q')
number[twelve] = '12'
thirteen = (number == 'K')
number[thirteen] = '13'
for num in range(0, len(number)):
    # 给num 赋值
    even = np.array(number[num])
    # 接收要判断的数据  (调用numpy的array函数)

    color = np.array(even[0:10:2])
    value = np.array(even[1:11:2])
    # 把数据以特征值分成两种(颜色和数值)

    value = value.astype(int)
    # 接收的数值部分转化成int类型，便于后续计算
    summ = np.sum([value])
    # 计算数值部分的总和   (调用numpy的sum函数)
    Norepeat = len(value) - len(set(value))
    # 计算数值不重复的个数
    value.sort()
    # 把数据的数值部分，从小到大升序
    xiangcha = value[4] - value[0]
    # 计算最值之间的长度   (用索引值接收到数值后 计算 最大值于最小值之间的差， 并接收)
    Tag = 1
    while Tag == 1:
        # 颜色全部相同的  1，3，7，分为一类
        if color[0] == color[1] == color[2] == color[3] == color[4]:
            # 判断接收的数据颜色是否全部相同

            if value[0] == 1 and summ == 47:
                # 先判断第一个数值是否为A，并且数值总和47
                print(1, file=fw)
                # 输出 1 ，并写入文件里
                Tag = 0
            elif xiangcha == 4:
                # 再判断间隔为 1
                print(3, file=fw)
                Tag = 0
            else:
                # 否则就只是颜色全部相同
                print(7, file=fw)
                Tag = 0
        elif Norepeat == 0:
            # 数值大小全部不同的 1 和 2 分为一类

            if (xiangcha == 4) or (value[0] == 1 and summ == 47):
                print(2, file=fw)
                # 判断（数值部分是否前后间隔为 1）或者（第一个数值是否为A，并且数值总和47）
                Tag = 0
            else:
                # 否则就是没有规则的数据
                print(0, file=fw)
                Tag = 0

        elif Norepeat == 1:
            # 数值大小有 1 张数值重复的
            print(8, file=fw)
            Tag = 0

        elif Norepeat == 2:
            # 数值大小有 2 张数值重复的

            if value[0] == value[2] or value[1] == value[3] or value[2] == value[4]:
                # 判断是否有 2 张数值一样的
                print(9, file=fw)
                Tag = 0
            else:
                # 否则就是有 3 个数值  俩俩 相同的牌
                print(4, file=fw)
                Tag = 0
                # 数值大小有3 张数值重复的
        elif Norepeat == 3:
            # 判断是否有 4 张数值一样的
            if value[0] == value[3] or value[1] == value[4]:
                print(5, file=fw)
                Tag = 0
            else:
                # 否则就是有 3 张数值相同牌并且另外 2 张数值也相同
                print(6, file=fw)
                Tag = 0
fw.close()
