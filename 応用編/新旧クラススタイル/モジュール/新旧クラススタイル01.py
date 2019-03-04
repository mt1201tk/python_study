# -*- coding: utf-8 -*-
 
 
# 旧スタイルクラス
class OldStyleClass:
    pass
 
 
# 新スタイルクラス
class NewStyleClass(object):
    pass
 
 
print type(OldStyleClass)
print type(NewStyleClass)



#Python 2系（2.2以降）では新クラススタイルと旧クラススタイルの両者から選ぶことができます。