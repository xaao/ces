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
sheetname = pd.read_excel("C:\\Users\\11699\\Desktop\\20220714统计数据.xls", sheet_name=None)
sheet_list = list(sheetname.keys())[0:]
#print(sheet_list)
runNum = 0
#创建pdf文件
pp = PdfPages('江西营业厅智能视频分析系统.pdf')
for name in sheet_list:
    #读取目标表格文件，并用people代表读取到的表格数据
    sheet = pd.read_excel("C:\\Users\\11699\\Desktop\\20220714统计数据.xls", sheet_name=name)
    print(sheet)
    sheetname_list = list(sheet.keys())[0:]
    print(sheetname_list)
    #x轴是姓名，y轴是年龄，让直方图排序显示，默认升序
    sheet.sort_values(by=sheetname_list[0], inplace=True, ascending=False)
    #按顺序显示
    #将直方图颜色统一设置为蓝色
    x = sheetname_list[0]
    y = sheetname_list[1]
    color = ['#6d8346', '#2a5caa', '#444693', '#769149', '#2b4490', '#78a355', '#224b8f', '#74905d', '#003a6c', '#007d65']
    sheet.plot.bar(x, y, color=color[runNum], label=sheetname_list[0])
    #旋转X轴标签，让其横向写
    plt.xticks(rotation=360)
    # 添加数据标签 就是矩形上面的数值
    for a, b in enumerate(sheet[y]):
        plt.text(a - 0.13, b, '%s' % round(b), ha='left', va='bottom', fontsize=12, color='black')

#    plt.show()
    pp.savefig()
    runNum = runNum + 1
    # plt.savefig("C:\\Users\\11699\\Desktop\\" + x + '.jpg')

pp.close()
