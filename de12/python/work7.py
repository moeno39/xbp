waist_list=[] #waist_listというリストを作る
for i in range(1,4):
    print(i,"人目")

    name=input("名前を教えて下さい")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))


    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if age>=40 and waist>=85:
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        print(name,"さん、腹囲は問題ありません")


        waist=float(input("腹囲は？"))

        waist_list.append(waist) #ここでwaistという変数の値をリストに追加している

    print(waist_list)

    l=len(waist_list) 
    s=sum(waist_list) 
    mean=s/l #平均は合計/件数