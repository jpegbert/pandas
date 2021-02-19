import pandas as pd
import numpy as np

# https://zhuanlan.zhihu.com/p/100064394
"""
pandas中pandas中针对Series而言，map函数的使用方法
"""


def map_by_dict(data):
    """
    使用字典进行映射
    """
    data["gender"] = data["gender"].map({"男": 1, "女": 0})


def gender_map(x):
    """
    使用函数映射
    """
    gender = 1 if x == "男" else 0
    return gender


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

    # 方法1：使用字典映射
    map_by_dict(data)
    print(data)

    # 方法2：使用函数映射
    # 注意这里传入的是函数名，不带括号
    data["gender"] = data["gender"].map(gender_map)
    print(data)


if __name__ == '__main__':
    main()
