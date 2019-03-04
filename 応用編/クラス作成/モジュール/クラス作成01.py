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
    
    
    
#classと記述し、後にクラス名が続きます（今回の例ではTestClassがクラス名になります）。
#クラス名の後には必ず「 : 」（コロン）を付けましょう。