import schedule
import time

#時間設定
print("スリープBGMを再生する時間を指定してください")
hour = input("時間（hour）:")
minute = input("分（minute）:")
target = f"{hour.zfill(2)}:{minute.zfill(2)}"
print(target+"に再生時間を設定しました")

#defは「定義」ということ
def job():
    import webbrowser
    #再生したい動画を指定
    webbrowser.open("https://youtu.be/8GYpz-QesEQ")

schedule.every().day.at(target).do(job)

#時間待ち
while True:
  schedule.run_pending()
  time.sleep(60)