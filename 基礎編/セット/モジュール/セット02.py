test_set_1 = set()
 
test_set_1.add('python')
test_set_1.update({'-', 'izm', '.', 'com'})
 
print(test_set_1)

#単一の要素を追加する場合はadd、他のセットやリスト、タプルなどから要素を追加する場合はupdateを使用します。





test_set_1 = {'python', '-', 'izm', '.', 'com'}
 
test_set_1.remove('-')
test_set_1.discard('.')
 
print(test_set_1)

#セットから要素を削除する場合はremove、discardを使用します。





test_set_1 = frozenset({'python', '-', 'izm', '.', 'com'})
 
# test_set_1.remove('-')
# test_set_1.discard('.')
 
print(test_set_1)

#frozensetはfrozenset関数を使用して通常のsetのように作成できます。
