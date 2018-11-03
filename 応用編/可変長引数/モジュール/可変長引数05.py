def test_func(code, name, kana, *args, **kwargs):
    print(code, name, kana)
    print(args)
    print(kwargs)
 
test_func(
    100, 'python-izm', u'パイソンイズム',
    'JP', 'US', 
    email='xxxx', city='Tokyo'
)

#通常の引数と併用することができ、さらに「 * 」を使用した可変長引数と併用することも可能です。
こちらの引数名も同様に、必ずしも**kwargsでなくてはならないわけではありません。