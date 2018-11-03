def test_func(**kwargs):
    print(kwargs)
 
test_func(code=100, name='python-izm')

#引数名の前に「 ** 」を付与することでも可変長引数となります。