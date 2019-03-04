def plus_value(num_1, num_2):
    return num_1 + num_2
 
 
print(plus_value(10, 100))
 
l_func = lambda num_1, num_2: num_1 + num_2
print(l_func(10, 100))

#Pythonでは名前の無い関数を作成することができ無名関数や匿名関数とも呼ばれます。
#lambda式はlambdaの後に引数を指定し、「：」（コロン）の後に処理を記述します。
