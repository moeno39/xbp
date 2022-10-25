print("あなたは授業で居眠りをしていて目が覚めると教室に閉じ込められていた！")
print("...? 自分以外に誰かいるようだ。")
name=input("A君 あなたの名前は？")

print("A君 閉じ込められてるみたいだけど、どうする？？")
print("１周りを見渡す")
print("２諦めて寝る")
print("３目の前にあるお菓子を食べる")

selecta=int(input("1~3の中から選んでね！"))

if selecta==1:
    print("教室の中に道用先生のパソコンを見つけた！")

elif selecta==2:
    print("気が付いたら朝になっていた！")

elif selecta==3:
    print("お菓子の食べ過ぎで動けなくなってしまった！")


print("パソコンのパスワードを入れてみよう！")
print("１道用先生の誕生日")
print("２道用先生の身長")
print("３道用先生の体重")

selectb=int(input("1~3の中から選んでね！"))

if selectb==3:
    print("教室のドアからガチャという音がした！")

elif selectb==1:
    print("パスワードが違うようだ")

elif selectb==2:
    print("パスワードが違うようだ")

print("教室から出ると、下の階が火事になっていた！")


print("どうしよう！")
print("１上の階に行く")
print("２下の階に行く")

selecta=int(input("1~2の中から選んでね！"))

if selecta==1:
    print("屋上に出ることができた！")

elif selecta==2:
    print("火に囲まれて逃げられなくなった！")

print("自分のスマホの充電が切れていることに気づいた！")
print("しかし、A君のスマホも充電が残り2%しかない！")
print("一回しか電話をかけられない")
print("誰にかける？")
print("1 消防署に電話して助けを求める")
print("2 友達に電話して助けを求める")
print("3 親に電話して最後のお別れをする")

selectb=int(input("1~3の中から選んでね！"))

if selectb==2:
    print("友達は大富豪でヘリコプターを呼んでくれて助かった！")

elif selectb==1:
    print("消火が間に合わず助からなかった")

elif selectb==3:
    print("親に電話をかけようとした途端充電が切れた")