import sys
 
sys.path.append('c:/python')
 
import com.pythonizm.calc
print(com.pythonizm.calc.plus_value(1, 1))

#3行目で検索パスの追加を行っており、これでそのパスをインタプリタが探してくれるようになります。
#5行目はパッケージ内に配置されているモジュールのインポートです。
#6行目でモジュール内のplus_value関数を呼び出し、結果を取得・表示しています。
