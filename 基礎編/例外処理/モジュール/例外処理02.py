def exception_test(value_1, value_2):
 
    print('＝＝＝＝計算開始＝＝＝＝')
 
    result = 0
 
    try:
        result = value_1 + value_2
    except:
        print('計算出来ませんでした！')
        raise
    finally:
        print('計算終了')
 
    return result
 
 
try:
    print(exception_test(100, 100))
    print(exception_test(200, 200))
    print(exception_test(300, '300'))
except:
    print('エラーを受け取りました')
    
#呼び出し元にエラーを上げ、そのエラー処理を任せた方が良いケースもあります。それを実現するのがraiseです。
#exception_testで例外（エラー）発生時にraiseするように記述しているので、それが呼び出し元のtryの方へ伝播します。