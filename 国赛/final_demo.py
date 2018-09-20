#conding = utf-8
import time

start = time.time()

#定义扑克类，属性为花色和数值
class Poker:
    def __init__(self, color, value):

        #初始化花色、数值
        self.color = color
        self.value = 0

        #初始化数值，将 J、Q、K 转化为数值，便于计算
        if value == "J":
            self.value = 11
        elif value == "Q":
            self.value = 12
        elif value == "K":
            self.value = 13
        else:
            self.value = int(value)

    def __str__(self):
        #展示扑克信息
        return "%s : %d" % (self.color, self.value)



#poker = Poker("D","K")
#print(poker)


class Pokers:

    # 扑克牌的flag
    #flag = 0

    def __init__(self):

        # 5张扑克列表
        self.poker_list = []

        # 存放扑克的数值
        self.value_list = []
        # 存放排序后相邻数值的差
        self.diff_list = []

        #扑克牌的flag
        self.flag = 0

    def add_poker(self, poker):

        self.poker_list.append(poker)

    def culValue(self):

        for pk in self.poker_list:
            self.value_list.append(pk.value)

        # 从小到大排序
        self.value_list.sort()

        i = 0
        while i < len(self.value_list) - 1:
            self.diff_list.append(self.value_list[i + 1] - self.value_list[i])
            i += 1

    def getFlag(self):
        return self.flag


 #   def __str__(self):
#      print("扑克牌是 %s " % self.poker_list)

#同花类
class SuitedPokers(Pokers):

    def getFlag(self):

        if (self.poker_list[0].color == self.poker_list[1].color == self.poker_list[2].color ==
                self.poker_list[3].color == self.poker_list[4].color):
            self.flag = 7

        return self.flag

        i += 1

#顺子
class Connector(Pokers):

    def getFlag(self):

        if (self.value_list[0] == 1 and
                self.value_list[1] + self.value_list[2] + self.value_list[3] + self.value_list[4] == 46):
            self.flag = 2
            return self.flag

        #如果各个扑克数值差1，则为顺子，flag置2
        flg = True

        for di in self.diff_list:
            if di != 1:
                flg = False
                #print(di)
                break
     #   print(self.flag)
        if flg:
            self.flag = 2

        return self.flag

#同花顺，继承SuitedPokers和Connector类
class Flush(SuitedPokers,Connector):

    def getFlag(self):
    #    print("Flush:"+str(Connector.getFlag(self)))
        if SuitedPokers.getFlag(self) > 1 and Connector.getFlag(self) > 1:
            if (self.value_list[0] == 1 and
                    self.value_list[1] + self.value_list[2] + self.value_list[3] + self.value_list[4] == 46):
                self.flag = 1
            else:
                self.flag = 3

        return self.flag

#一个对子
class Pairs(Pokers):

    def getFlag(self):

        #数值相同个数-1
        zero = 0
        #差值为0的个数
        zero_num = 0
        #第一个0的位置
        zero_position = 0

        #计算差值0的个数
        zero_num = self.diff_list.count(0)

        #如果0的个数为1，那么只有一个对子
        if zero_num == 1:
            #将标记置为8
            self.flag = 8

        #当0的个数为2时，有两种情况，一个是2个对子，另一个是连续3个数字相同
        elif zero_num == 2:
            zero_position = self.diff_list.index(0)
            #如果两个0连续，那么说明三个数字相同
            if self.diff_list[zero_position+1] == 0:
                self.flag = 9
            #两个对子
            else:
                self.flag = 4
        #当0的个数为3，一种情况是2+3的模式，另一种是4张牌一样
        elif zero_num == 3:
            #2+3的模式
            if self.diff_list[zero_position+1] != 0 :
                self.flag = 6
            else:
                self.flag = 5

        return self.flag


import numpy as np
import pandas as pd

#读如数据
pokers_rows = np.loadtxt("Semifinal-testing-final.csv", dtype=np.str, delimiter=",")
#打开写入文件
fw = open('dsjyycxds_semifinal.txt', 'w')
#判断5张扑克的代码
pokers = Pokers()
#print(type(number))
for pokers_row in pokers_rows:

    suited = SuitedPokers()

    conn = Connector()

    pairs = Pairs()

    flush = Flush()

    i = 0
    #读取每张扑克的信息，存入Poker类
    while i < 5:

        #新建Poker类对象，初始化扑克的花色和数字
        poker = Poker(pokers_row[i * 2], pokers_row[i * 2 + 1])
        pokers.add_poker(poker)

        suited.add_poker(poker)

        conn.add_poker(poker)

        pairs.add_poker(poker)

        flush.add_poker(poker)

        i += 1

    suited.culValue()
    conn.culValue()
    pairs.culValue()
    flush.culValue()


    if suited.getFlag() == 0:
        
        if conn.getFlag():
            print(conn.getFlag(), fw)
        else:
            print(pairs.getFlag(), fw)
    else:
        if conn.getFlag() > 0:
            print(flush.getFlag(), fw)
        else:
            print(suited.getFlag(), fw)

fw.close()
end =time.time()
print ('totally cost',end-start)












