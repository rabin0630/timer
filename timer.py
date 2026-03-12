from time import sleep
import sys
from InquirerPy import prompt
import os
from plyer import notification

#作業時間の選択(Select_Time)
def ST():
    question = {
        "type": "list",
        "name": "work_time", # prompt関数の仕様上、nameキーが必要
        "message": "作業時間",
        "choices": [
            {"name": "30分", "value": 30},
            {"name": "60分", "value": 60},
            {"name": "90分", "value": 90},
            {"name": "120分", "value": 120},
            {"name": "150分", "value": 150},
            {"name": "Exit", "value": None}
        ],
        "default": None,
    }

    answer = prompt(question)
    # answerは {"work_time": 30} のような辞書で返るため、値だけを抽出
    return answer.get("work_time")

#時間をセットに変換(Convert_Time)
def CT(minutes):
    return minutes // 30

#通知の設定
def notify_macos(title, message):
    script = f'display notification "{message}" with title "{title}" sound name "Pluck"'
    os.system(f"osascript -e '{script}'")

    
def main(A):
    for i in range(1500,0,-1):
        os.system("clear")
        minutes = i // 60
        seconds = i % 60
        print(f"{A}セット目:{minutes:02}:{seconds:02}")
        sleep(1)

    for a in range(300,0,-1):
        minutes = i // 60
        seconds = i % 60
        print(f"{b}セット目(休憩):{minutes:02}:{seconds:02}")
        sleep(1)
#
if __name__ == "__main__" :
    #Select time
    a = ST()
    #Convert Time
    x = CT(a)
    #作業開始の通知
    notify_macos("timer","作業開始")
    for a in range(x):
        main(a)
        
    sys.exit()