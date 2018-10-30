value = 2
 
if value == 1:
    print('valueの値は1です')
elif value == 2:
    print('valueの値は2です')
elif value == 3:
    print('valueの値は3です')
else:
    print('該当する値はありません')
    
#ifを記述後に条件式を記述し、その条件がTrueであれば条件配下の処理が実行される仕組みとなります。
#別の条件式を定義する際にはelifを使用します。どの条件にも該当しない場合の処理を定義する場合はelseを使用しましょう。