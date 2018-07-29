import datetime


def get_today():

    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)

    return value


test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])

#タプルの特徴は作成した後の変更が不可能という点です。複数の値を返す関数の戻り値などをタプルにすると良いでしょう。
