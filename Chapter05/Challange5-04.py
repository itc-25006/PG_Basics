my_features={"height": "163.0",
             "weight": "60.0"}
n=input("特徴を入力してください。")
if n in my_features:
    features=my_features[n]
    print(features)
else:
    print("見つかりません。")

