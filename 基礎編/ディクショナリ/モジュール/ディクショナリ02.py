test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}

print(test_dict_1)

print('=================================')

print(test_dict_1['YEAR'])
# print(test_dict_1['YEARS'])

print('---------------------------------')

print(test_dict_1.get('YEAR'))
print(test_dict_1.get('YEARS'))

print('---------------------------------')

print(test_dict_1.get('YEAR', 'NOT FOUND'))
print(test_dict_1.get('YEARS', 'NOT FOUND'))

# getを使用する利点は、ディクショナリ内に対応するkeyが存在しなくてもエラーにはならないことです。
