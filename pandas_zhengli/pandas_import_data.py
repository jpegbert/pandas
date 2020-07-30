import pandas as pd
import pymysql


# https://blog.csdn.net/qq_41562377/article/details/90203805
# https://www.cnblogs.com/zhaohuanhuan/p/9177277.html


def import_data_from_csv(): # 从csv文件导入数据
    # engine="python"可以避免文件路径中有中文, encoding="utf_8_sig"可以使读取的内容中有中文
    df = pd.read_csv("./test.csv", engine="python", encoding="utf_8_sig")


def import_data_from_table(): # 从table导入数据
    # sep表示分隔符，header=None表示第一行不是列名，是数据，这样不会损失第一行的数据
    df = pd.read_table("./1.txt", sep="\t", header=None)
    print(df)


def import_data_from_excel(): # 从excel中导入数据
    # sheetname表示要读取的sheet，header=None表示第一行不是表头， encoding编码方式
    df = pd.read_excel("./example.xls", sheetname='Sheet1', header=None, encoding="utf_8_sig")


def import_data_from_sql(): # sql表/库中导入数据
    con = pymysql.connect(host="127.0.0.1", user="username", password="password", database="dbname", charset='utf8',
                          use_unicode=True)
    sql_cmd = "select * from users limit 10;"
    df = pd.read_sql(sql_cmd, con)


def import_data_from_json(): # 从json字符串中导入数据
    json_data = '[{"col 1":"a","col 2":"b"},{"col 1":"c","col 2":"d"}]'
    df = pd.read_json(json_data)

    json_data = '{"city":{"guangzhou":"20","zhuhai":"20"},"home":{"price":"5W","data":"10"}}'
    df = pd.read_json(json_data)

    json_data = '[["a",1],["b",2]]'
    df = pd.read_json(json_data)
    print(df)


def main():
    # import_data_from_csv() # 从csv文件导入数据
    # import_data_from_table() # 从table导入数据，即txt文件
    # import_data_from_excel() # 从excel中导入数据
    # import_data_from_sql() # sql表/库中导入数据
    import_data_from_json() # 从json字符串中导入数据
    # 从字典中导入数据


if __name__ == '__main__':
    main()
