class TestClass:
 
    # インスタンスメソッド
    def sample_instancemethod(self, arg_1):
        pass
 
    # クラスメソッド
    @classmethod
    def sample_classmethod(cls, arg_1):
        pass
 
    # スタティックメソッド
    @staticmethod
    def sample_staticmethod(arg_1, arg_2):
        pass



#Pythonのクラスにおけるメソッドの種類には、インスタンスメソッド、クラスメソッド、スタティックメソッドがあります。
#インスタンスメソッド いわゆる通常のメソッドです。
#クラスメソッド クラスをインスタンス化しなくても呼び出すことができるメソッドです。
#スタティックメソッド クラスをインスタンス化しなくても呼び出すことができるメソッドです。またselfやclsなどのインスタンスやクラスを表す変数を必要としません。
