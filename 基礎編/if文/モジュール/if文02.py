value_1 = 'python'
value_2 = 'izm'
 
if value_1 == 'Python':
    pass
elif value_1 == 'python' and value_2 == 'izm':
    print('2番目の条件式がTrue')
elif value_1 == "IZM" or value_2 == "PYTHON":
    print('3番目の条件式がTrue')
    
#条件の組み合わせにはand、orなどを用います。
#5行目にpassという記述がありますが、これは簡単にいうと何もしませんという命令になります。