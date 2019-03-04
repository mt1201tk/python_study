# 新スタイルクラス
class NewStyleClassBase(object):
 
    def test_method(self, msg):
        print('NewStyleClassBase: {}'.format(msg))
 
 
# 新スタイルのクラスを継承
class NewStyleClass(NewStyleClassBase):
 
    def test_method(self, msg):
        print('NewStyleClass: {}'.format(msg))
        super().test_method(msg)
        # super(NewStyleClass, self).test_method(msg)
        # NewStyleClassBase.test_method(self, msg)
 
 
new = NewStyleClass()
new.test_method('method call')



#新クラススタイルの場合はsuper関数を使用します。
#super(自クラス名).メソッド名(引数)のような形で呼び出しますが、旧クラススタイルの呼び出し方法も利用可能です。