print("あなたは授業で居眠りをしていて目が覚めると教室に閉じ込められていた！")
print("...? 自分以外に誰かいるようだ。")
name=input("A君 あなたの名前は？")

print("どうしよう！")
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

