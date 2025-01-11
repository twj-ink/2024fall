import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

file_path=r"D:\临时下载\deleted_citation.xlsx"
df=pd.read_excel(file_path)
#print(df.head())
#print(df.info())
#print(df.isnull().sum())

########################################
# #初始查看
# plt.hist(df['被引量'],bins=150)
# plt.xlabel('count of citation')
# plt.ylabel('nums')
# plt.title('the nums of the count of citation')
# plt.show()

#查看前一部分的直方图
#plt.hist(df['被引量'],bins=150)
#plt.xlim(0,60)
#plt.xlabel('count of citation')
#plt.ylabel('nums')
#plt.title('the nums of the count of citation')
#plt.show()

#查看前一部分的密度图
#sns.kdeplot(filtered_data['被引量'],shade=True)
#plt.xlim(0，60)
#plt.show()

#查看后一部分的直方图
#plt.hist(df['被引量'],bins=60)
#plt.xlim(60,300)
#plt.ylim(0,3)
#plt.xlabel('count of citation')
#plt.ylabel('nums')
#plt.title('the nums of the count of citation')
#plt.show()

# #查看后一部分的密度图
# filtered_data=df[df['被引量'] >= 60]
# sns.kdeplot(filtered_data['被引量'],shade=True)
# plt.xlim(60,300)
# plt.show()
#
# ############################################
# #归一化之前的数据平均值和标准差
# pre_average=df['被引量'].mean()
# pre_variance=df['被引量'].var()
# print('Pre_average:',format(pre_average,'.5f'))
# print('Pre_variance:',format(pre_variance,'.5f'))
#
# #使用pandas实现0-1归一化
# df['0-1_normalized_data']=(df['被引量']-df['被引量'].min()) / (df['被引量'].max()-df['被引量'].min())
# df.to_excel('D:\临时下载\deleted_citation.xlsx',index=False)
#
# # 01归一化之后的数据平均值和标准差
# curr_average=df['0-1_normalized_data'].mean()
# curr_variance=df['0-1_normalized_data'].var()
# print('0-1_Curr_average:',format(curr_average,'.5f'))
# print('0-1_Curr_variance:',format(curr_variance,'.5f'))
#
# # #查看01归一化结果
# plt.hist(df['0-1_normalized_data'],bins=150)
# plt.show()
#
# ############################################
#boxcox归一化
df['boxcox_normalized_data'], fit_lambda = stats.boxcox(df['被引量'] + 1)  # Box-Cox变换，+1是因为数据中可能包含0

# #绘制Box-Cox变换后的数据的直方图
# sns.histplot(df['boxcox_normalized_data'], kde=True)
# plt.show()
# df.to_excel('D:\临时下载\deleted_citation.xlsx',index=False)
#
# #计算boxcox的均值和标准差
# curr_average=df['boxcox_normalized_data'].mean()
# curr_variance=df['boxcox_normalized_data'].var()
# print('boxcox_Curr_average:',format(curr_average,'.5f'))
# print('boxcox_Curr_variance:',format(curr_variance,'.5f'))

###############################################3

#计算归一化得到的分割点对应的原始数据分割点
def back_boxcox(x,fit_lambda):
    if fit_lambda==0:
        return np.exp(x)-1
    else:
        return (x*fit_lambda+1)**(1/fit_lambda)-1

#三等分点
# points=pd.qcut(df['boxcox_normalized_data'],q=3).quantile
# #print(points)
# # group_points=[0.64,1.344]                       #deleted_data
# group_points=[0.643,1.356]
# source_points=[]
# for point in group_points:
#     p=back_boxcox(point,fit_lambda)
#     source_points.append(p)
# print(*source_points)
# #0.9990717436140832 4.002675736904996
# #1.0001923515755733 4.003466381902354             #deleted_data


# #五等分点
# points=pd.qcut(df['boxcox_normalized_data'],q=5).quantile
# print(points)
# group_points=[0.64,0.97,1.344,1.65]
# group_points=[0.643,0.976,1.356,1.669]               #deleted_data
# source_points=[]
# for point in group_points:
#     p=back_boxcox(point,fit_lambda)
#     source_points.append(p)
# print(*source_points)
# #0.9990717436140832 1.9998480848531397 4.002675736904996 6.994161943278529
# 1.0001923515755733 1.9999768097588837 4.003466381902354 7.000265540422092     #deleted_data

#计算01归一化得到的分割点的对应原始数据
#三等分点
def back_01(x):
    return x*(df['被引量'].max()-df['被引量'].min())+df['被引量'].min()
# points=pd.qcut(df['0-1_normalized_data'],q=3).quantile
# print(points)
# group_points=[0.00337,0.0135]
# group_points=[0.00676,0.027]
# source_points=[]
# for point in group_points:
#     p=back_01(point)
#     source_points.append(p)
# print(*source_points)
#0.9990717436140832 2.118721083639879
#1.00048 3.996

#五等分点
# points=pd.qcut(df['0-1_normalized_data'],q=5).quantile
# print(points)
# points=[0.00676,0.0135,0.027,0.0473]
# source_points=[]
# for point in points:
#     p=back_01(point)
#     source_points.append(p)
# print(*source_points)
#1.00048 1.998 3.996 7.0004