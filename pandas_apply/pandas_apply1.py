import pandas as pd
import numpy as np

# https://zhuanlan.zhihu.com/p/100064394
"""
pandas中针对Series而言，apply函数的使用方法

总结一下对DataFrame的apply操作：
当axis=0时，对每列columns执行指定函数；当axis=1时，对每行row执行指定函数。
无论axis=0还是axis=1，其传入指定函数的默认形式均为Series，可以通过设置raw=True传入numpy数组。
对每个Series执行结果后，会将结果整合在一起返回（若想有返回值，定义函数时需要return相应的值）
当然，DataFrame的apply和Series的apply一样，也能接收更复杂的函数，如传入参数等，实现原理是一样的，具体用法详见官方文档。
"""


def apply_age(x, bias):
    """
    针对series使用apply
    """
    return x + bias


def df_apply(data):
    """
    针对dataframe使用apply
    """
    # 沿着0轴（也就是列的方向）求和
    # data[["height", "weight", "age"]] = data[["height", "weight", "age"]].apply(np.sum, axis=0)
    data[["age"]] = data[["age"]].apply(np.sum, axis=0)
    # print(data[["height", "weight", "age"]])
    print(data[["age"]])
    # 沿着0轴（也就是列的方向）取对数
    # data[["height", "weight", "age"]] = data[["height", "weight", "age"]].apply(np.log, axis=0)
    # print(data[["height", "weight", "age"]])


def BMI(series):
    weight = series["weight"]
    height = series["height"] / 100
    BMI = weight / height**2
    return BMI


def main():
    boolean = [True, False]
    gender = ["男", "女"]
    color = ["white", "black", "yellow"]
    data = pd.DataFrame({
        "height": np.random.randint(150, 190, 100),
        "weight": np.random.randint(40, 90, 100),
        "smoker": [boolean[x] for x in np.random.randint(0, 2, 100)],
        "gender": [gender[x] for x in np.random.randint(0, 2, 100)],
        "age": np.random.randint(15, 90, 100),
        "color": [color[x] for x in np.random.randint(0, len(color), 100)]
    }
    )

    print(data)

    # 以元组的方式传入额外的参数，实现对所有的年龄减3
    data["age"] = data["age"].apply(apply_age, args=(-3,))
    print(data)

    # 针对dataframe使用apply
    df_apply(data)
    data["BMI"] = data.apply(BMI, axis=1)
    print(data["BMI"])


if __name__ == '__main__':
    main()
