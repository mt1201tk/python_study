class TestClass:
 
    # スタティックメソッド
    @staticmethod
    def sample_staticmethod(x, y):
        return x + y
 
 
# インスタンス化しないで呼び出し
print(TestClass.sample_staticmethod(10, 100))
 
# インスタンス化してからも呼び出せる
test_class = TestClass()
print(test_class.sample_staticmethod(100, 1000))

#スタティックメソッドはインスタンス化しなくても呼び出すことができますが、インスタンスからでも呼び出すことができます。
#インスタンスメソッドにはself、クラスメソッドにはclsが必要ですが、スタティックメソッドには必要ありません。
