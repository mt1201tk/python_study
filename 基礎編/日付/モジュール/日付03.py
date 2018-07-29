import calendar

print(calendar.isleap(2015))
print(calendar.isleap(2016))
print(calendar.isleap(2017))

print(calendar.leapdays(2010, 2020))

#その年がうるう年かどうかを判定するにはcalendar.isleapを、指定期間内に何回のうるう年があるかを取得するにはcalendar.leapdaysを使用します。
