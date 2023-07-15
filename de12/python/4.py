nedan = {"草もち": 80, "せんべい": 120, "アメ": 10,"だんご": 200}
kosu = {}

# 入力データの読み込み
while True:
    data = input().split()
    if data[0] == "-":
        break
    item = data[0]
    quantity = int(data[1])
    if item in kosu:
        kosu[item] += quantity
    else:
        kosu[item] = quantity

# 総売り上げ金額の計算
total_sales = 0
for item in kosu.keys():
    total_sales += nedan[item] * kosu[item]

print("総売り上げ金額:", total_sales, "円")
