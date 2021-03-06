import datetime


today = datetime.date.today()
todaydetail = datetime.datetime.today()

# 今日の日付
print('----------------------------------')
print(today)
print(todaydetail)

# 今日に日付：それぞれの値
print('----------------------------------')
print(today.year)
print(today.month)
print(today.day)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.hour)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)

# 日付のフォーマット
print('----------------------------------')
print(today.isoformat())
print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))

#標準ライブラリであるdatetimeを使用しましょう。このように標準ライブラリやサードパーティライブラリなど、特定の機能を使用したい場合はimportを用います。
