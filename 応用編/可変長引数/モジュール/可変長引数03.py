def test_func(code, name, *countries):
    print(code, name)
    print(countries)
 
test_func(100, 'python-izm', 'JP', 'US')

#なお引数名は必ずしも*argsでなくてはならないわけではありません。