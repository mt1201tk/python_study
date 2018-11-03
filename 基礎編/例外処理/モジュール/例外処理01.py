def exception_test(value_1, value_2):
 
    print('＝＝＝＝計算開始＝＝＝＝')
 
    result = 0
 
    try:
        result = value_1 + value_2
    except:
        print('計算出来ませんでした！')
    finally:
        print('計算終了')
 
    return result
     
 
print(exception_test(100, 200))
print(exception_test(100, '200'))

#処理中に例外（エラー）が発生しなければexcept配下の処理は実行されません。
#二回目の呼び出しの際の引数は片方が文字列ですので、足し算を実行することができずexcept配下の処理が実行される流れです。