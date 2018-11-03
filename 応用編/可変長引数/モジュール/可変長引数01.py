def test_func(*args):
    print(args)
 
test_func(1, 2, 3, 4, 5)

#引数名の前に「 * 」を付与することで可変長引数となります。