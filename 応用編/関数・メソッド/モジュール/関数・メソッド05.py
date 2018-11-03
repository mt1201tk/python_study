# 関数
def test_func():
    print('call test_func')
  
  
class TestClass:
    # メソッド
    def test_method():
        print('call test_method')
 
print('------------------------')
print(test_func)
print(TestClass.test_method)
 
print('------------------------')
print(type(test_func))
print(type(TestClass.test_method))
 
print('------------------------')
t = TestClass()
print(test_func)
print(t.test_method)

#Pythonでは関数（function）とメソッド（method）があります。
#モジュール内にdefで定義されているものが関数、クラス内にdefで定義されているものがメソッドになります