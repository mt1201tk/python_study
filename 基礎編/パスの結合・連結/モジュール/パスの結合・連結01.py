import os


PROJECT_DIR = 'C:?python-izm'
SETTINGS_FILE = 'settings.ini'

print(os.path.join(PROJECT_DIR, SETTINGS_FILE))
print(os.path.join(PROJECT_DIR, 'settings_dir', SETTINGS_FILE))

#Pythonではパスの結合や連結を行う関数が用意されています。
#パスを結合・連結するにはos.path.joinを使用します。

