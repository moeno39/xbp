print("あなたは授業で居眠りをしていて目が覚めると教室に閉じ込められていた！")
print("...? 自分以外に誰かいるようだ。")
name=input("A君 あなたの名前は？")

print("A君",name,"さんだね！")
print("A君 閉じ込められてるみたいだけど、どうする？？")
print("１周りを見渡す")
print("２諦めて寝る")
print("３目の前にあるお菓子を食べる")

for selecta in range(2 and 3):
    selecta=int(input("1~3の中から選んでね!"))

    if selecta==1: 
        print("教室の中に道用先生のパソコンを見つけた！")
        break
        

    elif selecta==2:
        print("気が付いたら朝になっていた！")
        print("もう一度選んでみよう！")
        continue
        
       
    elif selecta==3:
        print("お菓子の食べ過ぎで動けなくなってしまった！")
        print("もう一度選んでみよう！")
        continue

    


print("パソコンのパスワードを入れてみよう！")
print("１道用先生の誕生日")
print("２道用先生の身長")
print("３道用先生の体重")

for selectb in range(1 and 2):
    selectb=int(input("1~3の中から選んでね!"))

    if selectb==3:
        print("教室のドアからガチャという音がした！")
        break

    elif selectb==1:
        print("パスワードが違うようだ")
        print("もう一度選んでみよう！")
        continue

    elif selectb==2:
        print("パスワードが違うようだ")
        print("もう一度選んでみよう！")
        continue


print("教室から出ると、下の階が火事になっていた！")


print("どうしよう！")
print("１上の階に行く")
print("２下の階に行く")

for selectc in range(2):
    selectc=int(input("1~2の中から選んでね!"))

    if selectc==1:
        print("屋上に出ることができた！")
        break

    elif selectc==2:
        print("火に囲まれて逃げられなくなった！")
        print("もう一度選んでみよう！")
        continue

print("自分のスマホの充電が切れていることに気づいた！")
print("しかし、A君のスマホも充電が残り2%しかない...")
print("一回しか電話をかけられないが、誰にかける？")
print("１消防署に電話して助けを求める")
print("２友達に電話して助けを求める")
print("３親に電話して最後のお別れをする")

for selectd in range(1 and 3):
    selectd=int(input("1~3の中から選んでね!"))

    if selectd==2:
        print("友達は大富豪でヘリコプターを呼んでくれて助かった！")
        print("脱出成功！！")
        break

    elif selectd==1:
        print("消火が間に合わず助からなかった...")
        print("もう一度選んでみよう！")
        continue

    elif selectd==3:
        print("電話をかけた途端充電がなくなってしまった...")
        print("もう一度選んでみよう！")
        continue