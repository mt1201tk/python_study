f_obj = open('test.txt', 'w')
 
print('python-izm.com', file=f_obj)

#出力先を一時的にファイルへ変更する場合、Python 3系ではfile引数へ出力先となるファイルオブジェクトを渡します。





print('Pythonの学習サイト : %s' % 'python-izm.com')
print('Pythonの学習サイト : %s-%s.%s' % ('python', 'izm', 'com'))
 
test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設 %d 日目！ %s' % (test_int, test_str))

#%sは文字列、%dは数値として認識され、混在して出力することができます。
#フォーマット識別子を含んだメインの文字列の後に%を接続語としてフォーマット出力を行う値を渡します。