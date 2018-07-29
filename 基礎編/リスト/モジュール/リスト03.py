test_list_1 = ['python', 'izm', 'com']
print(test_list_1)

print('--------------------------------')

test_list_1.insert(1, '-')
test_list_1.insert(3, '.')

print(test_list_1)

test_list_1.insert(0, 'http://www.')

print(test_list_1)

#appendは常に末尾へ追加されますが、insertを利用するとインデックス値を指定して要素を追加することができます。
#最初の引数は追加箇所を示すインデックス値、次の引数は追加を行う要素となります。
