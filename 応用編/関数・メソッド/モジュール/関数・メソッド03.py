def test_func(num_1, num_2, oprn=1):
 
    if oprn == 1:
        print('足し算開始')
        print(num_1 + num_2)
 
    elif oprn == 2:
        print('引き算開始')
        print(num_1 - num_2)
 
    elif oprn == 3:
        print('掛け算開始')
        print(num_1 * num_2)
 
    elif oprn == 4:
        print('割り算開始')
        print(num_1 / num_2)
 
    else:
        print('不明なオペレーション指定です')
 
test_func(100, 10)

#引数は初期値を指定すると、関数を呼び出す際に省略する事が可能です。