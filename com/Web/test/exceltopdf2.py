#!/usr/bin/env python3
# encoding=UTF-8

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

#支持图表中显示中文
rcParams['font.family'] = 'simhei'

#获取sheet页名称
sheetname = pd.read_excel("C:\\Users\\11699\\Desktop\\20220722统计数据(1).xls", sheet_name=None)
sheet_list = list(sheetname.keys())#[0:] #获取所有表名
# print(sheet_list)
runNum = 0
#创建pdf文件
pp = PdfPages('C:\\Users\\11699\\Desktop\\jingke.pdf')
for name in sheet_list:
    #读取目标表格文件，并用sheet代表读取到的表格数据
    sheet = pd.read_excel("C:\\Users\\11699\\Desktop\\20220722统计数据(1).xls", sheet_name=name)
    print(sheet)
    sheetname_list = list(sheet.keys())#[0:]#获取表的所有属性
    # print(sheetname_list)
    #x轴是姓名，y轴是年龄，让直方图降序显示
    sheet.sort_values(by=sheetname_list[1], inplace=True, ascending=False)
    #配置依据by排序inplace=True表示在原数据上修改数据，ascending=False表示降序，反之可以理解
    #设置直方图颜色
    # print(sheet)
    x = sheetname_list[0]
    y = sheetname_list[1]
    color = ['#6d8346', '#2a5caa', '#444693', '#769149', '#2b4490', '#78a355', '#224b8f', '#74905d', '#003a6c', '#007d65']
    sheet.plot.bar(x, y, color=color[runNum], label=sheetname_list[0]) #此函数为确定横纵坐标生成柱图高，图名为label
    # len_type = []
    # for type in sheet_list[1]:
    #     print(type)
    #     len_type.append(len(type))
    # max_len = max(len_type)

    len_data = len(sheet)
    if len_data > 6:
        # 旋转X轴标签，让其斜30度写
        plt.xticks(rotation=30)
    # elif max_len > 4:
    #     # 旋转X轴标签，让其横向写
    #     plt.xticks(rotation=360)
    else:
        # 旋转X轴标签，让其横向写
        plt.xticks(rotation=0)
    # 添加数据标签 就是矩形上面的数值
    for a, b in enumerate(sheet[y]):
        plt.text(a-0.13, b,round(b), ha='left', va='bottom', fontsize=12, color='black')
    # try:
    #     for c in range(len(list(sheet[y]))):
    #         plt.text(c - 0.13, list(sheet[y])[c], round(sheet[y][c]), ha='left', va='bottom', fontsize=12, color='black')
    # except Exception as e:
    #     print("这里错了")
    #     print(e.args)
    #使生成的图片能完全展示
    plt.tight_layout()

#    plt.show()
    pp.savefig()
    runNum = runNum + 1
#    plt.savefig("D:\\禅道分析数据\\" + x + '.jpg')

pp.close()
