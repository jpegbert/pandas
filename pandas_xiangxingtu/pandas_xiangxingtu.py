# https://blog.csdn.net/qq_41080850/article/details/83829045

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


def method1():
    tips = pd.read_csv('../data/train_city_23.csv')
    # tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
    fig, axes = plt.subplots()
    tips['gross_area'].plot(kind='box', ax=axes)
    axes.set_ylabel('values of tip_pct')
    fig.savefig('p1.png')  # 将绘制的图形保存为p1.png


def method2():
    tips = pd.read_csv('../data/train_city_23.csv')
    # fig, axes = plt.subplots(1, 4)
    fig, axes = plt.subplots(1, 2)
    color = dict(boxes='DarkGreen', whiskers='DarkOrange',
                 medians='DarkBlue', caps='Red')
    # boxes表示箱体，whisker表示触须线
    # medians表示中位数，caps表示最大与最小值界限

    tips = tips[['gross_area', 'future_avg_price']]
    tips.plot(kind='box', ax=axes, subplots=True,
              title='Different boxplots', color=color, sym='r+')
    # sym参数表示异常值标记的方式

    axes[0].set_ylabel('values of total_bill')
    axes[1].set_ylabel('values of tip')
    # axes[2].set_ylabel('values of size')
    # axes[3].set_ylabel('values of tips_pct')

    fig.subplots_adjust(wspace=1, hspace=1)  # 调整子图之间的间距
    fig.savefig('p2.png')  # 将绘制的图片保存为p2.png


def method3():
    tips = pd.read_csv('../data/train_city_23.csv')
    fig, axes = plt.subplots()
    tips.boxplot(column='tip_pct', by=['smoker', 'time'], ax=axes)
    # column参数表示要绘制成箱形图的数据，可以是一列或多列
    # by参数表示分组依据

    axes.set_ylabel('values of tip_pct')
    fig.savefig('p3.png')  # 将绘制的图形保存为p3.png


def method4():
    tips = pd.read_csv('../data/train_city_23.csv')
    fig, axes = plt.subplots()
    sns.catplot(x='tip_pct', y='day', hue='smoker', kind='box',
                data=tips[tips.tip_pct < 0.5])
    # hue表示分组的依据

    fig.savefig('p4.png')  # 将绘制的图形保存为p4.png


def method5():
    tips = pd.read_csv('../data/train_city_23.csv')
    fig, axes = plt.subplots()
    sns.boxplot(x='day', y='tip_pct', hue='smoker',
                data=tips[tips.tip_pct < 0.5], orient='v', ax=axes)
    # orient参数表示箱形图的方向

    axes.set_title('Boxplots grouped by smoker')
    fig.savefig('p5.png')  # 将绘制的图形保存为p5.png


def method6():
    tips = pd.read_csv('../data/train_city_23.csv')
    fig, axes = plt.subplots()
    axes.boxplot(x=tips.tip_pct, sym='rd', positions=[2])
    # sym参数表示异常值的标记方式
    # positions表示箱形图的位置标签

    axes.set_xlabel('tip_pct')
    fig.savefig('p6.png')  # 将绘制的图形保存为p6.png


def main():
    # method1()
    # method2()
    # method3()
    # method4()
    # method5()
    method6()


if __name__ == "__main__":
    main()
