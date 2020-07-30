import pandas as pd

df = pd.DataFrame({'A':['bob','sos','bob','sos','bob','sos','bob','bob'],
              'B':['one','one','two','three','two','two','one','three'],
              'C':[3,1,4,1,5,9,2,6],
              'D':[1,2,3,4,5,6,7,8]})


# def evaluation(data):
#     prediction = data["prediction"]
#     price = data["prediction"]
#     coef = prediction / price
#     if coef > 1.2 or coef < 0.5:
#         return 0
#     elif coef < 1:
#         return 1 - ((price - prediction) / price) * 2
#     elif coef <= 1.2:
#         return 1 - ((prediction - price) / price) * 4
#     else:
#         return 0

def evaluation(data):
    prediction = data["C"]
    price = data["D"]
    coef = prediction / price
    print(coef)
    if coef > 1.2 or coef < 0.5:
        return 0
    elif coef < 1:
        return 1 - ((price - prediction) / price) * 2
    elif coef <= 1.2:
        return 1 - ((prediction - price) / price) * 4
    else:
        return 0

print(df)
df["score"] = df.apply(evaluation, axis=1)
print(df)

