#三层神经网络，含有一个隐藏层
#结果大约在84%左右
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#读入数据

dataset = pd.read_csv('train_data.csv',header=None)
#数据归一化
dataset /=256.0
dataset = dataset.values
#print (type(dataset))
dataset_label=pd.read_csv('train_data_labels.csv',header=None)
dataset_label = dataset_label.values


#神经网络配置
dataset_num = len(dataset)
input_num =dataset.shape[1]       #确定输入节点数
out_num = 10
hid_num = 12     #隐藏层节点数
#初始化输入权重矩阵
w12 = 0.2*np.random.random((input_num,hid_num)) - 0.1
# 初始化隐层权矩阵
w23 = 0.2*np.random.random((hid_num, out_num))- 0.1 
print(w12.shape)
hid_offset = np.zeros(hid_num)      # 隐层偏置向量
out_offset = np.zeros(out_num)      # 输出层偏置向量
input_learnrate = 0.15              # 输入层权值学习率
hid_learnrate = 0.15                # 隐层学权值习率
err_th = 0.01                       # 学习误差门限


#print(dataset.loc[1:2].shape)

#定义激活函数
def get_act(x):
    act_vec = []
    for i in x:
        act_vec.append(1/(1+math.exp(-i)))
    act_vec = np.array(act_vec)
    return act_vec

def get_err(e):
    return 0.5*np.dot(e,e)


# 训练——可使用err_th与get_err() 配合，提前结束训练过程

for count in range (0,dataset_num):
    t_label =  np.zeros(out_num)
    t_label[dataset_label[count]] = 1
    #前向过程
    hid_value = np.dot(dataset[count],w12)
    hid_act = get_act(hid_value)
    out_value = np.dot(hid_act,w23)
    out_act = get_act(out_value)

    #反向过程
    
    e = t_label - out_act
    out_delta = e*out_act*(1-out_act)
    hid_delta = hid_act * (1-hid_act)*np.dot(w23,out_delta)
    for i in range(0,out_num):
        #更新隐藏层到输出层权向量
        w23[:,i] += hid_learnrate * out_delta[i] * hid_act
    for i in range (0,hid_num):
        #更新输入层到隐藏层权重
        w12[:,i] += input_learnrate * hid_delta[i] * dataset[count]

    out_offset += hid_learnrate * out_delta
    hid_offset += input_learnrate * hid_delta


#测试
test_data = pd.read_csv('test_data.csv',header=None)
test_data /=256.0
test_data = test_data.values

test_label = pd.read_csv('test_data_label.csv',header=None)
test_label =test_label.values



right = np.zeros(10)
numbers = np.zeros(10)

# 统计测试数据中各个数字的数目
print(test_label.shape)


for i in test_label:
    numbers[i] += 1

for count in range(len(test_data)):
    hid_value = np.dot(test_data[count],w12) + hid_offset
    hid_act = get_act(hid_value)
    out_value = np.dot(hid_act,w23) + out_offset
    out_act = get_act(out_value)
    if np.argmax(out_act) == test_label[count]:
        right[test_label[count]] += 1



print (right)
print (numbers)
result = right/numbers
sum = right.sum()
print (result)
print (sum/len(test_data))
