class TestClass:
 
    def __init__(self, code, name):
        self.code = code
        self.name = name
 
 
classes = []
classes.append(TestClass(1, 'テスト１'))
classes.append(TestClass(2, 'テスト２'))
 
for test_cls in classes:
    print('===== Class =====')
    print('code --> ' + str(test_cls.code))
    print('name --> ' + test_cls.name)

#self.xxといった形で自身が保持する情報へアクセスする事ができます。
#クラスを作成した側からはインスタンス名.codeやインスタンス名.nameでアクセスすることができます
#インスタンスごとに異なる情報を設定することができます
