import pandas as pd
import pymysql

# https://www.jianshu.com/p/23f897d855cf
# https://www.cnblogs.com/zhaohuanhuan/p/9177277.html
df = pd.DataFrame({'A': [3, 4, 8, 9], 'B': [1.2, 2.4, 4.5, 7.3], 'C': ["aa", "bb", "cc", "dd"]})


def export_data_to_csv():
    # 参数encoding="utf_8_sig"编码后，可以防止写入csv的中文出现乱码
    df.to_csv("./test.csv", encoding="utf_8_sig")


def export_data_to_excel():
    # encoding编码方式，sheet_name表示要写到的sheet名称， 默认为0， header=None表示不含列名
    df.to_excel("./test.xlsx", encoding="utf_8_sig", sheet_name=0, header=None)


def export_data_to_table():
    con = pymysql.connect(host="127.0.0.1", user="username", password="password", database="dbname", charset='utf8',
                          use_unicode=True)
    df.to_sql(name='table_name', con=con, if_exists='append', index=False)


def export_data_to_json():
    df.to_json("test.txt")


def main():
    export_data_to_csv() # 导出数据到CSV文件
    export_data_to_excel() # 导出数据到Excel文件
    export_data_to_table() # 导出数据到SQL表
    export_data_to_json() # 以Json格式导出数据到文本文件


if __name__ == '__main__':
    main()
